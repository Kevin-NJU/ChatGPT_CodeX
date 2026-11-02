# Consolidated Learning State

更新：2026-11-03（Asia/Shanghai） · 检查点：`INIT-000001`

## 当前状态

| 字段 | 当前值 |
| --- | --- |
| 项目 | Personal English Learning System (PELS) |
| 已完成阶段 | Phase 0 · Project Initialization |
| 下一阶段 | Phase 1 · Initial English Assessment，尚未开始 |
| 等待方 | learner |
| 下一条启动指令 | **开始诊断 Day 1** |
| Day 1 / Day 2 | not_started / not_started |
| Day 1 完成日期 | unknown（尚未开始） |
| 当前评估 ID | `ASM-000001`，已保留给首次诊断，仅方案存在 |
| 当前 Session / 题目 / 最后 attempt | none / none / none |
| 最近学习日 / 完整记录位置 | none / none |
| 已完成实际学习日 | 0；由 Session 索引实际活动的不同日期核算 |
| 上次周期回顾 | none；满约 7 个实际学习日后触发首次回顾 |
| 当前个性化计划 / 评估报告 | none / none |
| 今日可用时间 / 实际耗时 | unknown / unknown |
| 已登记词汇 / 错误 / 复习项 | 0 / 0 / 0 |
| Listening / Speaking | inactive / inactive；两者 not assessed |

## 下一步与恢复位置

收到启动指令后：

1. 读取[诊断方案](assessments/initial-assessment.md)，核对本状态与[Session 索引](progress/sessions.csv)，确认没有正在进行的记录。
2. 问 **How much time do you have for English today?**；已经给出当天时间则直接复用。
3. 用[模板](templates/session.md)在实际日期下创建学习日文件及首个 Session，登记预算与 `ASM-000001`。仅有题目、没有学习者作答时，不计为实际学习日。
4. 简要展示 Day 1 目标、时间与独立作答约定，先给一小批 Vocabulary 题。当前不提前生成题目或答案。

Day 1 完成后记录完成日期、证据和待验证假设，等待另一个学习日输入 **继续诊断 Day 2**。中途暂停优先恢复当前阶段，不因输入 Day 2 而跳过未完成部分。

## 待完成、假设与边界

- 五个启用模块全部 `not assessed`。当前“词汇不扎实”“阅读慢”等仅为[用户自述](PROFILE.md)，不是测评结论。
- 没有到期复习；开始后按队列实际日期查询，不从空表生成任务。
- 未遗留学习题、用户原答或修订；没有需要导入的历史聊天。
- 公开仓库已核实；本地初始化提交与远程同步状态由 Git 实时查询，不能把本文件当作实时 Git 输出。本次无远程上传授权。

## 后续检查点必须保存的内容

保留当前阶段、日期、Session/题目/attempt ID、最后写入位置、谁在等待谁、是否已给提示或答案、当前题的未完成步骤、已完成/缺失覆盖、下次入口及待同步索引。已完成数据从原记录核对后再浓缩，不只写“继续学习”。检查点修订用新的标识并保留详细记录中的旧检查点。
