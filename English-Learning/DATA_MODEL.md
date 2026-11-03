# Data Model · schema v1

本文件是字段、ID、空值及更新规则的权威。规则与过程用 Markdown，小型状态/索引用 UTF-8 CSV；不需要数据库。CSV 用标准逗号分隔与双引号转义，保持这里规定的列名和顺序，优先使用 Python `csv` 模块读写，不能手工用 `split(',')` 处理含逗号的答案。

## 权威来源与缺失值

| 事实 | 唯一权威来源 | 其他位置的用途 |
| --- | --- | --- |
| 原题、原答、修订、提示、反馈、评分、检查点 | `sessions/YYYY/MM/YYYY-MM-DD.md` | 其他表只保存摘要并引用具体锚点 |
| 学习者自述与当前证据画像 | `PROFILE.md` | 自述与观察分区，不互相覆盖 |
| 当前阶段、等待方、恢复位置、当前计划指针 | `STATE.md` | 不能取代原始历史或实时 Git 状态 |
| 当前词汇、错误、复习安排 | 各 CSV | 旧值及变更理由留在对应学习记录 |
| 复习事件 | `reviews/events.csv` + 对应原始记录 | 事件追加；队列是最近事件的结果 |
| Session 清单、阅读原始指标、素材来源 | 对应索引 CSV | 统计从索引计算，解释回看原始证据 |
| 当前训练策略与阶段门槛 | `ROADMAP.md` + `STATE.md` 指向的计划版本 | 旧计划保留，不覆盖历史优先级 |

所有日期用 `YYYY-MM-DD`，解释为 `Asia/Shanghai` 的当地日期；精确时间用带 `+08:00` 的 ISO 8601。未测、未知或不适用的 CSV 字段留空，不能填 `0`、`N/A` 或臆测值；状态字段使用规定枚举。真实零分、零次和空缺有不同含义。Markdown 用 `unknown`、`not assessed`、`not_started` 等明确文字。

初始化七张 CSV **只有表头，没有真实数据或示例行**。模板里的占位符不是学习数据，不能直接写入数据表。

## 稳定 ID 与证据引用

- `ASM-000001` 首次诊断；后续 `ASM-000002` 等。计划 `PLAN-000001`，周期回顾 `PRG-000001`。
- 词汇 `VOC-000001`；错误 `ERR-000001`；复习项 `REV-000001`；复习事件 `RVE-000001`；阅读测量 `RDG-000001`；材料 `MAT-000001`。数字至少六位，同类型递增、永不复用。
- Session：`SES-YYYYMMDD-NN`，当天从 `01` 递增；题目：`SES-YYYYMMDD-NN-T001`；attempt：`SES-YYYYMMDD-NN-A001`。题目与 attempt 的流水号分别在 Session 内递增。跨日继续旧题保持旧题 ID，新 attempt 使用新 Session 前缀并显式关联旧题。
- 原始记录用小写 ID 作 HTML 锚点，例如 `<a id="ses-YYYYMMDD-01-a001"></a>`，真实使用时替换日期。用户每次修订分配新 attempt；反馈与原答同段保存，反馈更正另追加。
- CSV 中 `*_ref` 一律相对 **English-Learning 根目录**，用 `/` 分隔，无前导 `/`、无 `..` 逃逸。例如文件建成后使用 `sessions/YYYY/MM/YYYY-MM-DD.md#ses-YYYYMMDD-01-a001`。证据引用必须指向已存在的真实记录锚点；Markdown 普通导航则相对所在文件。
- 不预填未来 ID 的数据行。新增前扫描当前表和相关记录，取同类型最大号加一；ID 分配并发冲突时重新读取并协调，不能同时保存不同内容的同 ID。

## 七张 CSV 的字段

### 1. `vocabulary/items.csv` · 当前词汇条目

| 字段 | 类型 / 规则 |
| --- | --- |
| vocab_id | 唯一 `VOC-…` |
| lemma, pos, sense | 非空词形、词性、当前语境义；不同词性/义项必要时独立记录 |
| collocations, example_sentence | 当前已确认的搭配/例句；多值可用 `; ` 分隔，不编造学习者成功表现 |
| original_error | 确有原始错误时逐字保留；没有观察到错误则留空 |
| level | `unassessed` 或 `L0`–`L4`，含义见 [vocabulary](vocabulary/README.md) |
| status | `learning` / `reviewing` / `stable` / `archived` |
| first_seen, last_practiced | 首次实际接触日期、最近实际练习日期；后者不早于前者 |
| review_id | 对应复习队列的 `REV-…`；暂未排程可空 |
| evidence_ref | 最近支持当前判断的原答锚点；历史变化及旧证据留在原学习记录 |

“下次复习日期”由 `review_id` 关联 `reviews/queue.csv.due_on` 查询，不在两张表重复维护日期。条目层级变化须在当日记录写出旧值 → 新值、依据和范围；不把教师例句当作学习者会用的证据。

### 2. `error-bank/errors.csv` · 当前错误及模式

| 字段 | 类型 / 规则 |
| --- | --- |
| error_id | 唯一 `ERR-…` |
| module | `vocabulary` / `grammar` / `reading` / `writing` / `translation`；明确启用后可用 `listening` / `speaking` |
| error_type, knowledge_point | 可检索的类别和知识点；不确定时用明确的“待分类/待验证”描述 |
| original_answer, corrected_version | 逐字原表达及当前认可修正；不抹除其他可接受版本 |
| cause_hypothesis | 暂定原因或“待验证”，不是未经证据支持的心理判断 |
| pattern_status | `single_observation` / `recurring` / `systematic_candidate` / `confirmed_pattern` |
| first_seen, last_seen | 首次和最近独立出现日期 |
| occurrence_count | 正整数；不同独立任务中出现同模式才累加，同题修订不重复计数 |
| status | `open` / `improving` / `resolved` / `archived` |
| first_evidence_ref, latest_evidence_ref | 首次及最近独立出现的 attempt 锚点；具体各次出现和改正证据保留在日志 |

一个错误可有多个知识点，但尽量选主要原因而非为同一现象大量拆行。改变归因保留旧假设及修订理由。`resolved` 表示当前追踪范围内已稳定改进，不是永久不会再错。

### 3. `reviews/queue.csv` · 当前复习队列

| 字段 | 类型 / 规则 |
| --- | --- |
| review_id | 唯一 `REV-…` |
| target_type, target_id | `vocabulary` + VOC ID；`error` + ERR ID；或 `task` + 原题 ID |
| status | `scheduled` / `paused` / `retired`；同一目标至多一条非 retired 项 |
| created_on, last_reviewed, due_on | 创建日、最近实际复习日（未复习可空）、下次复习日；paused 保留原 due_on，不伪称到期完成 |
| interval_days | 正整数，日历天；初次安排默认 1，后续见复习规则 |
| success_streak | 非负整数；连续无提示成功次数，不等于掌握层级 |
| last_outcome | 未复习可空；其余 `again` / `hard` / `good` / `easy` |
| evidence_ref | 触发排程或最近复习的原答锚点；task 目标须指回已有原题所在记录 |

### 4. `reviews/events.csv` · 追加式复习历史

`review_event_id`（唯一 RVE ID）、`review_id`（已存在队列项）、`session_id`（实际复习 Session）、`reviewed_on`（实际日期）、`outcome`（`again/hard/good/easy/not_completed`）、`assistance`（`none/hint/model/external`）、`next_due_on`（本次结算后日期）、`evidence_ref`（实际尝试锚点）。

新的真实尝试逐条追加。`not_completed` 不改变队列日期/连续成功数；若有提示或范文，不可给无提示成功的 `good/easy`。若发现既有事件录入或评分错误，先在学习日志追加该事件 ID、原值、新值、更正理由和日期，再用**同一事件 ID**更新索引并重核当前队列；原始尝试及旧判断保留在日志/Git 历史。更正不是新的复习尝试，不另增次数，不能静默改历史。

### 5. `progress/sessions.csv` · Session 索引

`session_id`（唯一 SES ID）、`date`、`phase`（`initial_day1/initial_day2/daily/followup_assessment/long_term`）、`status`（`in_progress/paused/completed/abandoned`）、`available_minutes`（确认的预算，正数或空）、`actual_minutes`（可确认实际时长，正数或空）、`actual_time_source`（`learner_reported/measured/unknown`）、`learning_activity`（`yes/no`）、`record_ref`（该 Session 锚点）。

仅有教师出题时 `learning_activity=no`；出现真实回答、检索或有记录的实际学习才为 yes。学习日数是 `learning_activity=yes` 的不同日期数，不是 completed 行数；同日多 Session 只计一天，部分完成也可算实际学习日。初始化、文件整理、未答题不计入。actual 为空时来源为 unknown；不要把预算当实际值。

### 6. `progress/reading.csv` · 阅读测量原始值

`reading_id`（唯一 RDG ID）、`session_id`、`material_id`、`mode`（`baseline/practice/reread/transfer`）、`word_count`（正整数）、`reading_seconds`（实际阅读秒数，正数或空）、`timing_source`（`learner_reported/measured/unavailable`）、`correct`、`scored`（客观理解题正确数/可评分题数，非负整数或同时为空）、`assistance`（`none/hint/model/external`）、`evidence_ref`（作答及计时依据）。

词数必须和该材料登记一致；改文章内容须新建 MAT ID。`correct <= scored`，仅 scored > 0 才算准确率。未答、取消或不可评分题单列日志，不进入分母；确实作答但错误可计 0。非客观题用日志中的评分量规，不能混入此处正确题数。阅读词数不含题目、标题、来源说明；正文按 `[A-Za-z]+(?:['’-][A-Za-z]+)*` 分词，缩写/带连字符词按该规则，数字不计；保存精确正文和规则，便于复算。

`WPM = word_count × 60 / reading_seconds`；`accuracy = correct / scored × 100%`。不存重复 wpm 列防止漂移，在当次日志和报告中展示原始量、计算式与取一位小数的结果。未知计时保持空，不用聊天时间间隔替代。只有相近难度/长度、相同计时边界、首读/重读、提示条件和题型的测量才可比较；其余并列展示，不算进步百分比。

### 7. `materials/registry.csv` · 来源登记

`material_id`（唯一 MAT ID）、`title`、`origin_type`（`tutor_authored/user_provided/external`）、`source_locator`（创作说明、用户提供定位或可核验 URL）、`access_scope`（`full_text/excerpt/metadata_only/unavailable`）、`rights_note`（版权/使用范围说明）、`added_on`、`content_ref`（本地材料正文锚点；没有可访问正文可空）、`word_count`（仅计词材料填写正整数，否则空）。

外链成功不等于读过全文。自编素材标记自编，不能冒充真题/官方文章。只保存有权保留的范围；外部全文受限时用链接与必要摘录，缺失正文不能用于可复算的计时阅读。

## 更新、复习结算与迁移

1. 先保存原始学习记录，再分配 ID、更新索引和当前状态；同一检查点已写入的事件不得再插入。
2. 当前状态 CSV 可更新，但每次层级、归因、状态和改期的旧值、新值与理由保存在学习日志；Session 原答与新尝试保持追加，事件索引的事实更正按上文留痕，不制造重复尝试。写 CSV 时先读最新文件、验证行数/ID，写同目录临时文件后原子替换；保留 Git 差异以便恢复，不用过期副本覆盖并发更新。
3. 不物理删除历史行，退出追踪用 archived/retired。重复/合并条目保留旧 ID，在日志记录关联与后继 ID，不能重编号。
4. schema 变更先更新本说明、模板和检查器；记录 v1 → v2 等迁移、字段映射及缺失值处理，迁移前保留可恢复版本，迁移后核对记录数、引用与统计。不得把无法恢复的数据补成已知值。

## 校验边界

`python3 English-Learning/tools/check.py` 验证当前结构、CSV 表头/枚举、ID 唯一、引用可达、日期与数值基本约束及跨表关联。Markdown 检查面向本项目当前的行内链接、ATX 标题和显式 HTML 锚点，不是通用渲染器；引入引用式链接、MDX 等新语法时需扩展检查。它不自动修改数据或安排复习，也不能判断原答是否真实、归因是否合理、画像是否有足够证据。维护者还须人工检查日志与评分、STATE/PROFILE/ROADMAP 一致性及停用模块边界。
