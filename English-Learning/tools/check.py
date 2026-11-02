#!/usr/bin/env python3
"""Read-only PELS schema-v1 checks. Python 3.9+ standard library only."""

import argparse
import csv
import datetime as dt
import html
import math
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


SCHEMAS = {
    "vocabulary/items.csv": "vocab_id,lemma,pos,sense,collocations,example_sentence,original_error,level,status,first_seen,last_practiced,review_id,evidence_ref",
    "error-bank/errors.csv": "error_id,module,error_type,knowledge_point,original_answer,corrected_version,cause_hypothesis,pattern_status,first_seen,last_seen,occurrence_count,status,first_evidence_ref,latest_evidence_ref",
    "reviews/queue.csv": "review_id,target_type,target_id,status,created_on,last_reviewed,due_on,interval_days,success_streak,last_outcome,evidence_ref",
    "reviews/events.csv": "review_event_id,review_id,session_id,reviewed_on,outcome,assistance,next_due_on,evidence_ref",
    "progress/sessions.csv": "session_id,date,phase,status,available_minutes,actual_minutes,actual_time_source,learning_activity,record_ref",
    "progress/reading.csv": "reading_id,session_id,material_id,mode,word_count,reading_seconds,timing_source,correct,scored,assistance,evidence_ref",
    "materials/registry.csv": "material_id,title,origin_type,source_locator,access_scope,rights_note,added_on,content_ref,word_count",
}
PREFIXES = ("VOC", "ERR", "REV", "RVE", "SES", "RDG", "MAT")
REQUIRED = (
    "lemma pos sense level status first_seen last_practiced evidence_ref",
    "module error_type knowledge_point original_answer corrected_version cause_hypothesis pattern_status first_seen last_seen occurrence_count status first_evidence_ref latest_evidence_ref",
    "target_type target_id status created_on due_on interval_days success_streak evidence_ref",
    "review_id session_id reviewed_on outcome assistance next_due_on evidence_ref",
    "date phase status actual_time_source learning_activity record_ref",
    "session_id material_id mode word_count timing_source assistance evidence_ref",
    "title origin_type source_locator access_scope rights_note added_on",
)
ENUMS = {
    "vocabulary/items.csv": {"level": "unassessed L0 L1 L2 L3 L4", "status": "learning reviewing stable archived"},
    "error-bank/errors.csv": {"module": "vocabulary grammar reading writing translation listening speaking", "pattern_status": "single_observation recurring systematic_candidate confirmed_pattern", "status": "open improving resolved archived"},
    "reviews/queue.csv": {"target_type": "vocabulary error task", "status": "scheduled paused retired", "last_outcome": "again hard good easy"},
    "reviews/events.csv": {"outcome": "again hard good easy not_completed", "assistance": "none hint model external"},
    "progress/sessions.csv": {"phase": "initial_day1 initial_day2 daily followup_assessment long_term", "status": "in_progress paused completed abandoned", "actual_time_source": "learner_reported measured unknown", "learning_activity": "yes no"},
    "progress/reading.csv": {"mode": "baseline practice reread transfer", "timing_source": "learner_reported measured unavailable", "assistance": "none hint model external"},
    "materials/registry.csv": {"origin_type": "tutor_authored user_provided external", "access_scope": "full_text excerpt metadata_only unavailable"},
}
DATE_FIELDS = {"first_seen", "last_seen", "last_practiced", "created_on", "last_reviewed", "due_on", "reviewed_on", "next_due_on", "date", "added_on"}
INTEGER_FIELDS = {"occurrence_count", "interval_days", "success_streak", "word_count", "correct", "scored"}
POSITIVE_FIELDS = {"occurrence_count", "interval_days", "word_count", "available_minutes", "actual_minutes", "reading_seconds"}
WORD_RE = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")


def markdown(text):
    """Parse the inline-link, ATX-heading and HTML-anchor syntax used by PELS."""
    anchors, links, issues = set(), [], []
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]), number)
            continue
        if re.match(r"^(<<<<<<< |=======$|>>>>>>> )", line):
            issues.append(f"line {number}: merge conflict marker")
        for explicit in re.findall(r'<a\s+(?:id|name)=[\"\x27]([^\"\x27]+)[\"\x27]', line):
            if explicit in anchors:
                issues.append(f"line {number}: duplicate explicit anchor")
            anchors.add(explicit)
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            title = re.sub(r"<[^>]+>", "", html.unescape(heading[1]))
            title = re.sub(r"!?\[([^]]+)\]\([^)]*\)", r"\1", title).replace("`", "").lower()
            slug = "".join(c for c in title if c in "-_ " or unicodedata.category(c)[0] in "LNM").replace(" ", "-")
            candidate, suffix = slug, 0
            while candidate in anchors:
                suffix += 1
                candidate = f"{slug}-{suffix}"
            anchors.add(candidate)
        line = re.sub(r"(`+).*?\1", "", line)
        for link in re.finditer(r'!?\[[^]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[\"\x27][^\n]*[\"\x27])?\s*\)', line):
            links.append((number, link[1].strip("<>")))
    if fence:
        issues.append(f"line {fence[2]}: unclosed code fence")
    return anchors, links, issues


def validate(root):
    errors, docs, tables = [], {}, {}

    def fail(where, message):
        errors.append(f"{where}: {message}")

    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
            anchors, links, issues = markdown(text)
            if not text.strip():
                issues.append("empty document")
            docs[path.resolve()] = (text, anchors, links)
            for issue in issues:
                fail(path.relative_to(root), issue)
        except (OSError, UnicodeError) as exc:
            fail(path.relative_to(root), str(exc))

    def reference(value, base, where, evidence=False):
        try:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                if evidence:
                    fail(where, "evidence must be a local file and anchor")
                return None
            target = (base / unquote(url.path)).resolve() if url.path else base.resolve()
            if not target.is_relative_to(root) or not target.exists():
                fail(where, "missing target or path outside project")
                return None
            if evidence and (not url.fragment or not target.is_file()):
                fail(where, "record reference requires a file and anchor")
            if url.fragment and (target not in docs or unquote(url.fragment) not in docs[target][1]):
                fail(where, "missing target anchor")
            return target
        except (OSError, ValueError) as exc:
            fail(where, f"invalid reference ({exc})")
            return None

    link_count = 0
    for path, (_, _, links) in docs.items():
        for line, destination in links:
            link_count += 1
            # An empty path such as #anchor resolves to the current document.
            base = path if destination.startswith("#") else path.parent
            reference(destination, base, f"{path.relative_to(root)}:{line}")

    for (filename, header), prefix, required in zip(SCHEMAS.items(), PREFIXES, REQUIRED):
        rows = []
        tables[filename] = rows
        try:
            with (root / filename).open(encoding="utf-8", newline="") as stream:
                reader = csv.reader(stream, strict=True)
                columns = header.split(",")
                if next(reader, None) != columns:
                    fail(filename, "schema-v1 header mismatch")
                    continue
                seen = set()
                for values in reader:
                    where = f"{filename}:{reader.line_num}"
                    if len(values) != len(columns):
                        fail(where, "wrong CSV field count")
                        continue
                    row = dict(zip(columns, values))
                    row["_where"] = where
                    rows.append(row)
                    item_id = values[0]
                    pattern = r"SES-\d{8}-\d{2,}" if prefix == "SES" else rf"{prefix}-\d{{6,}}"
                    if not re.fullmatch(pattern, item_id) or item_id in seen:
                        fail(where, "invalid or duplicate stable ID")
                    seen.add(item_id)
                    for key in required.split():
                        if not row[key].strip():
                            fail(where, f"missing required {key}")
                    for key, choices in ENUMS.get(filename, {}).items():
                        if row[key] and row[key] not in choices.split():
                            fail(where, f"invalid {key} enum")
                    for key, value in zip(columns, values):
                        if not value:
                            continue
                        if key in DATE_FIELDS:
                            try:
                                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                                    raise ValueError()
                                dt.date.fromisoformat(value)
                            except ValueError:
                                fail(where, f"invalid date in {key}")
                        if key in INTEGER_FIELDS or key in POSITIVE_FIELDS:
                            try:
                                number = float(value)
                                if not math.isfinite(number) or number < 0 or (key in POSITIVE_FIELDS and number == 0) or (key in INTEGER_FIELDS and not value.isdecimal()):
                                    raise ValueError()
                            except ValueError:
                                fail(where, f"invalid numeric value in {key}")
                        if key.endswith("_ref"):
                            target = reference(value, root, where, evidence=True)
                            folder = "materials" if key == "content_ref" else "sessions"
                            if target and not target.is_relative_to(root / folder):
                                fail(where, f"{key} must refer to {folder}/")
        except (OSError, UnicodeError, csv.Error) as exc:
            fail(filename, f"cannot read CSV ({exc})")

    if errors:
        return errors, len(docs), link_count, tables

    vocab, mistakes, queue, events, sessions, readings, materials = (tables[name] for name in SCHEMAS)
    by_id = [{row[next(iter(row))]: row for row in rows} for rows in (vocab, mistakes, queue, events, sessions, readings, materials)]
    vmap, emap, qmap, _, smap, _, mmap = by_id

    def require_id(row, key, mapping):
        if row[key] not in mapping:
            fail(row["_where"], f"unknown {key}")
            return None
        return mapping[row[key]]

    def ordered(row, earlier, later):
        if row[earlier] and row[later] and row[earlier] > row[later]:
            fail(row["_where"], f"{later} precedes {earlier}")

    for row in vocab:
        ordered(row, "first_seen", "last_practiced")
        if row["review_id"]:
            review = require_id(row, "review_id", qmap)
            if review and (review["target_type"], review["target_id"]) != ("vocabulary", row["vocab_id"]):
                fail(row["_where"], "review_id points to a different target")
    for row in mistakes:
        ordered(row, "first_seen", "last_seen")
        if row["pattern_status"] != "single_observation" and int(row["occurrence_count"]) < 2:
            fail(row["_where"], "repeated pattern requires multiple independent observations")
    for row in sessions:
        expected = f"sessions/{row['date'][:4]}/{row['date'][5:7]}/{row['date']}.md#{row['session_id'].lower()}"
        if row["record_ref"] != expected or row["session_id"].split("-")[1] != row["date"].replace("-", ""):
            fail(row["_where"], "session ID, date and record_ref disagree")
        if bool(row["actual_minutes"]) != (row["actual_time_source"] != "unknown"):
            fail(row["_where"], "actual duration and time source disagree")

    active_targets = set()
    profile = docs.get((root / "PROFILE.md").resolve(), ("",))[0]
    inactive = {name.lower() for name in re.findall(r"^\|\s*(\w+)\s*\|\s*inactive\s*\|", profile, re.M)}
    for row in queue:
        ordered(row, "created_on", "last_reviewed")
        ordered(row, "created_on", "due_on")
        ordered(row, "last_reviewed", "due_on")
        target = (row["target_type"], row["target_id"])
        if row["status"] != "retired":
            if target in active_targets:
                fail(row["_where"], "duplicate non-retired review target")
            active_targets.add(target)
        if target[0] in ("vocabulary", "error"):
            item = require_id(row, "target_id", vmap if target[0] == "vocabulary" else emap)
            if item and target[0] == "error" and item["module"] in inactive and row["status"] == "scheduled":
                fail(row["_where"], "inactive module review must be paused/retired")
        elif not re.fullmatch(r"SES-\d{8}-\d{2,}-T\d{3,}", target[1]) or not any(target[1].lower() in doc[1] for doc in docs.values()):
            fail(row["_where"], "task target lacks an existing task anchor")

    settled = {}
    for row in events:
        require_id(row, "review_id", qmap)
        session = require_id(row, "session_id", smap)
        if session and row["reviewed_on"] != session["date"]:
            fail(row["_where"], "review date differs from its session")
        if not row["evidence_ref"].split("#")[-1].startswith(row["session_id"].lower() + "-"):
            fail(row["_where"], "review evidence belongs to a different session")
        if row["outcome"] in ("good", "easy") and row["assistance"] != "none":
            fail(row["_where"], "assisted answer cannot count as unassisted success")
        if row["outcome"] != "not_completed":
            ordered(row, "reviewed_on", "next_due_on")
            previous = settled.get(row["review_id"])
            if previous and previous["reviewed_on"] > row["reviewed_on"]:
                fail(row["_where"], "review events must be appended chronologically")
            settled[row["review_id"]] = row
    for row in queue:
        last = settled.get(row["review_id"])
        if last:
            if (row["last_reviewed"], row["last_outcome"], row["due_on"], row["evidence_ref"]) != (last["reviewed_on"], last["outcome"], last["next_due_on"], last["evidence_ref"]):
                fail(row["_where"], "queue differs from latest settled review event")
            days = (dt.date.fromisoformat(row["due_on"]) - dt.date.fromisoformat(row["last_reviewed"])).days
            if days != int(row["interval_days"]):
                fail(row["_where"], "queue interval disagrees with actual review/due dates")
        elif row["last_reviewed"] or row["last_outcome"] or int(row["success_streak"]):
            fail(row["_where"], "queue claims review history without a settled event")

    for row in materials:
        if row["word_count"]:
            if not row["content_ref"] or row["access_scope"] not in ("full_text", "excerpt"):
                fail(row["_where"], "counted material requires accessible local content")
                continue
            text = docs[(root / unquote(urlsplit(row["content_ref"]).path)).resolve()][0]
            passage = re.search(r"^## Exact Passage\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            if not passage or len(WORD_RE.findall(passage[1])) != int(row["word_count"]):
                fail(row["_where"], "material word_count differs from Exact Passage")
    for row in readings:
        require_id(row, "session_id", smap)
        material = require_id(row, "material_id", mmap)
        if material and row["word_count"] != material["word_count"]:
            fail(row["_where"], "reading word_count differs from fixed material")
        if bool(row["reading_seconds"]) != (row["timing_source"] != "unavailable"):
            fail(row["_where"], "reading duration and timing source disagree")
        if bool(row["correct"]) != bool(row["scored"]) or (row["scored"] and int(row["correct"]) > int(row["scored"])):
            fail(row["_where"], "invalid correct/scored pair")
        if not row["evidence_ref"].split("#")[-1].startswith(row["session_id"].lower() + "-"):
            fail(row["_where"], "reading evidence belongs to a different session")
    return errors, len(docs), link_count, tables


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="PELS root (read only; useful for validating a migration copy)")
    args = parser.parse_args()
    errors, documents, links, tables = validate(args.root.resolve())
    if errors:
        for issue in errors:
            print(f"ERROR {issue}", file=sys.stderr)
        print(f"FAIL: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print(f"PASS: {documents} Markdown files, {links} inline links, {len(tables)} schema-v1 CSV tables")
    print("Rows: " + ", ".join(f"{name}={len(rows)}" for name, rows in tables.items()))
    days = {row["date"] for row in tables["progress/sessions.csv"] if row["learning_activity"] == "yes"}
    print(f"Actual study days: {len(days)} (structural validation, not a learning outcome)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
