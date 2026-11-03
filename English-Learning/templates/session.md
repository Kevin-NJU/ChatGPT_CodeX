# {{YYYY-MM-DD}} · Learning Log

> 模板，尚未发生学习。创建真实日期文件时替换占位符；同日后续从 Session 段追加，不重新覆盖整份文件。未知数据明确 unknown / 留空，不能猜测。

- Timezone: Asia/Shanghai
- 当日预算及来源：{{minutes / 用户确认；未提供则 unknown}}
- 当日实际总投入：{{仅汇总可确认时长；列缺失范围}}
- 当日状态：{{in_progress / paused / completed}}

<a id="{{session_anchor}}"></a>

## Session {{session_id}}

- Phase / Assessment / Plan：{{实际阶段及已有 ID；没有则 none}}
- 开始/结束时间：{{仅可确认时记录带偏移时间}}
- Available minutes / Actual minutes / Time source：{{预算 / 实际或 unknown / 来源}}
- Learning activity：{{yes/no；教师出题而未实际参与为 no}}
- 本次恢复来源：{{旧文件锚点 / first session}}
- 允许工具与独立作答约定：{{约定；实际偏离在 attempt 注明}}

### Today’s Plan

- Today’s Goal：{{能力目标}}
- Review Tasks：{{已存在的到期 REV ID；空队列则 none}}
- Main Practice：{{任务及 Accuracy / Fluency Mode}}
- Estimated Time：{{估计，不是实际耗时}}
- Expected Outcome：{{可观察表现，不是固定题量}}
- 用户调整：{{实际调整及原因}}

<a id="{{task_anchor}}"></a>

### Task {{task_id}}

- Module / Mode：{{module / accuracy 或 fluency}}
- Source：{{MAT ID 或题目直接保存在此；来源及可访问范围}}
- Status：{{issued / awaiting_answer / answered / reviewed / paused / skipped}}
- 初次/补测/反馈后迁移：{{baseline / probe / post_feedback}}
- 任务要求、允许工具、时间边界、评分维度：{{开题前明确；不要预写答案}}

**Original Prompt**

````text
{{本次实际出示的完整题目；材料正文另有文件时链接精确版本}}
````

<a id="{{attempt_anchor}}"></a>

### Attempt {{attempt_id}} · belongs to {{task_id}}

- 类型：{{独立首答 / 提示后作答 / 修订 / 迁移}}
- Assistance：{{none / hint / model / external，具体帮助是什么}}
- 可确认的实际耗时与来源：{{用户自报/明确测量；否则 unknown}}
- 原答保存时间：{{可确认的时间；不是用来推算阅读时长}}

**My Original Answer — verbatim**

````text
{{逐字保存当前可见回答，包括错误；若原文有围栏，外层选更长围栏}}
````

**Feedback**

- Corrected Version：{{必要修正；保留原意，标明可接受变体}}
- Explanation：{{依据、语境和原因；假设标记待验证}}
- Natural Alternative / Common Mistake：{{按需，区分错误与风格偏好}}
- Scoring Evidence：{{实际得分/满分、维度和原句证据；未测不打零}}
- Follow-up Practice：{{实际布置的后续任务 ID；尚未回答仍未完成}}
- 用户后续修订：{{另建新 attempt，链接此处，不能覆盖原答}}

### Reading Measurement（只在实际阅读任务使用）

- RDG ID / MAT ID / 条件：{{实际 ID / 首读或重读、难度、工具}}
- 正文词数及计词版本：{{可复算值；不含标题题目}}
- 阅读秒数 / 来源 / 中断：{{真实值或 unknown}}
- WPM：{{有秒数才算 word_count × 60 / seconds}}
- 客观理解题：{{correct / scored；跳过/未答/不可评分单列}}
- Accuracy：{{scored > 0 才算；附原答和判断依据}}
- 句法/逻辑开放题：{{单独量规，不混入客观题正确率}}
- 可能障碍及证据：{{观察 / 假设 / 待验证，分别写}}

### Review & Data Updates

| 实际事件/目标 ID | 原表现与证据 | 旧值 → 新值 | 原因 / 下次复习 |
| --- | --- | --- | --- |
| {{仅实际发生后填写}} | {{attempt 引用}} | {{层级/状态/间隔；不变也说明}} | {{真实日期或待安排}} |

同步范围：{{实际已更新的 CSV 和行 ID；未成功同步的列待办}}

<a id="{{checkpoint_anchor}}"></a>

### Checkpoint {{checkpoint_id}}

- 已保存到：{{最后完整题目/attempt 锚点；精确位置}}
- 已完成 / 未完成：{{区分真实完成、已布置、未开始}}
- 当前等待方：{{learner / tutor / external_input}}
- 当前题目与下一步：{{题目 ID、具体步骤和恢复入口}}
- 提示/答案暴露：{{无或具体范围；影响独立测量须说明}}
- 待验证假设：{{与证据对应；没有则 none}}
- 待同步索引：{{无或具体表/行；不能笼统写已保存}}
- 下一次：{{同日可用时间是否仍适用；跨日须重新确认}}

### End-of-Session Summary（实际结束时填写）

- 今天实际完成：{{未完成任务不得列为完成}}
- 当前证据支持的能力/掌握变化：{{本次表现与跨日稳定性分开}}
- 值得注意的错误：{{ERR ID 及证据}}
- 复习：{{已执行事件和仍到期项分别列}}
- 下次建议与状态：{{待办、推荐重点、paused / completed}}
- Actual minutes：{{可确认才填，不拿预算补齐}}

追加下一 Session 或下一检查点时保留以上全部历史。
