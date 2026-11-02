# Personal English Learning System (PELS)

个人英语学习系统 · 初始化版本 v0.1.0 · 2026-11-03（Asia/Shanghai）

PELS 由学习者与 Codex 共同维护，兼顾英语教师、学习分析师与项目维护者三个角色。核心循环是 **Assessment → Planning → Practice → Feedback → Review → Adaptation**。2026 年 12 月 CET-6 是阶段目标，系统将继续服务通用、学术和专业英语能力建设，不随考试结束而终止。

当前已完成 **Phase 0** 和首次诊断 **Day 1（2026-11-03）**，正在等待另一个学习日的 Day 2。真实结果与恢复入口以 [STATE](STATE.md) 为准；完整初始报告与个性化详细计划尚未生成。Vocabulary、Grammar、Reading、Writing、Translation 为当前范围；Listening、Speaking 均为 `inactive`、`not assessed`，仅在学习者明确要求后开启。

## 开始与恢复

在全新的 Codex 对话中提供仓库并输入：

```text
请接手 English-Learning/。先检查仓库状态，读取本项目 AGENTS.md、STATE.md、PROFILE.md、ROADMAP.md 和 LEARNING_PROTOCOL.md，再按状态恢复。保留原始回答，及时保存检查点；不要假定能访问历史聊天。
```

首次启动指令为 **开始诊断 Day 1**；该阶段现已完成。当前应在另一个学习日输入 **继续诊断 Day 2**。Codex 先问 **How much time do you have for English today?**；若当天已提供时间则不重复询问。两阶段均完成并形成证据报告后，才生成正式个人计划。

日常可使用“开始今天的学习”“暂停并保存”“继续上次任务”“今天只有 15 分钟”“复习到期内容”。这些是人工交互入口，不是已经安装的命令或自动提醒服务；没有运行中的 Codex 会话时，系统不会自行授课、统计或写文件。

## 目录与文件入口

| 入口 | 功能 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 每次接手必须遵循的角色、教学、保存及 Git 规则 |
| [LEARNING_PROTOCOL.md](LEARNING_PROTOCOL.md) | 课程、测评、暂停恢复、反馈与自适应流程 |
| [DATA_MODEL.md](DATA_MODEL.md) | 数据权威来源、字段、稳定 ID、统计及更新规则 |
| [PROFILE.md](PROFILE.md) | 自述背景、偏好与证据支持的能力画像 |
| [ROADMAP.md](ROADMAP.md) | 长期阶段路线；诊断后才填入具体个人计划 |
| [STATE.md](STATE.md) | 当前阶段、未完成任务、恢复位置和下一步 |
| [CHANGELOG.md](CHANGELOG.md) | 项目文件及机制变更，独立于学习日志 |
| [assessments/](assessments/README.md) | [两天诊断方案](assessments/initial-assessment.md)、未来评估报告 |
| [sessions/](sessions/README.md) | 每个实际学习日的详细记录，同日多个 Session 追加保存 |
| [vocabulary/](vocabulary/README.md) | [词汇数据](vocabulary/items.csv)：区分识别、理解和主动运用 |
| [error-bank/](error-bank/README.md) | [错误数据](error-bank/errors.csv)：保留原答、修正及证据 |
| [reviews/](reviews/README.md) | [复习队列](reviews/queue.csv)与[复习事件](reviews/events.csv) |
| [progress/](progress/README.md) | [Session 索引](progress/sessions.csv)、[阅读指标](progress/reading.csv)与未来周期总结 |
| [materials/](materials/README.md) | [素材登记](materials/registry.csv)，区分自编、用户提供和外部材料 |
| [templates/](templates/README.md) | [学习日记录](templates/session.md)、[评估报告](templates/assessment-report.md)、[学习计划](templates/learning-plan.md)、[周期回顾](templates/periodic-review.md)、[素材](templates/material.md) |
| [tools/check.py](tools/check.py) | Python 3.9+ 标准库只读检查：链接、表结构、ID、证据、日期及跨表一致性 |

不提前创建空白日期目录、虚构词汇、错题或测评报告。真实记录出现时才创建 `sessions/YYYY/MM/YYYY-MM-DD.md`；已有 [Day 1 学习记录](sessions/2026/11/2026-11-03.md#day1-summary)。在建议结构上仅增加统一数据说明与一个检查脚本；七个 CSV 是小型索引/当前状态，不复制整段对话，不需要数据库、服务器或第三方包。

## 使用原则

- **English-first Teaching**：互动优先英文，复杂逻辑可中文解释后转回英文练习。维护文档主要用中文。
- **Accuracy Mode** 关注准确性与解释；**Fluency Mode** 先完成输出再集中反馈，默认最多一次自改加一次迁移练习，或协商短时间上限。
- 自述不等于测评；单次成功不等于掌握；自编测评不等于正式 CET-6 或 CEFR 评级。
- 原始题目、原答、修改与评分依据保存在详细历史；画像、队列和 `STATE.md` 是浓缩状态。不能以摘要替代原始证据。
- 日期按 `Asia/Shanghai`；学习日按实际活动计数，初始化不算学习日。缺失的耗时、分数与能力数据保持未知。

## 检查、版本与隐私

在仓库根目录运行：

```bash
python3 English-Learning/tools/check.py
git diff --check -- English-Learning/
git status --short --branch
```

检查脚本只验证结构和可计算的一致性，不证明英语教学内容一定正确、数据一定真实，也不进行外链访问。新增未跟踪文件须另审正文；暂存后用 `git diff --cached --check -- English-Learning/` 检查空白。

初始化时已核实 `Kevin-NJU/ChatGPT_CodeX` 为 **public**。用户随后授权推送初始化成果，已建立 PR #2；诊断对话和后续状态仍只在本地保存。未来上传前重新确认可见性、差异及授权；公开仓库上传完整学习记录还须确认公开范围，可先在本地整理脱敏版本。不要保存密码、令牌或未授权第三方材料。沿用仓库 Git，不创建嵌套仓库，不自动推送、发布或部署。
