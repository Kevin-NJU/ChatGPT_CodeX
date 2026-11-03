# Error Bank

[errors.csv](errors.csv) 当前为空表。为值得追踪的真实错误建立稳定 ERR ID，原答不删除，修正不回填成首答。字段与状态见 [DATA_MODEL](../DATA_MODEL.md)。教师建议换一种更自然的风格时，先说明原句是否可接受，不将所有风格建议登记为语法错误。

- `single_observation`：一次观察，不确定是偶发还是模式。
- `recurring`：同类现象在不同独立任务重现；记录各次证据，同题反复改写不增加 occurrence_count。
- `systematic_candidate`：重复表现提示可能有规则理解或自动化障碍，需解释/迁移探针。
- `confirmed_pattern`：在明确取样范围内，重复证据与针对性验证支持某一模式；原因仍可有不确定性，不概括为永久缺陷。

`open → improving → resolved` 根据真实表现调整。`resolved` 通常需要至少两个不同学习日、不同语境的无提示正确迁移，并检查近期是否仍复发；证据不足保持 improving。归档使用 archived，不删除记录。复发更新原项及新证据，不换 ID 掩盖历史。

修正方案改变时保留旧方案及理由；“粗心”“中文思维”“不懂规则”只能是待验证假设。长期反复出错时换讲解/语境，必要时回基础概念，而非无限重复同题。
