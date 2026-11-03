# Templates

这些模板是待填写骨架，**不是学习者真实数据**。只有真实活动发生或阶段门槛满足后才复制到目标目录，替换 `{{占位符}}`，删除不适用段落；不能把模板行直接写入 CSV 或当作完成记录。

| 模板 | 实例位置与触发 |
| --- | --- |
| [session.md](session.md) | 实际日期的 `sessions/YYYY/MM/YYYY-MM-DD.md`；同日追加 Session |
| [assessment-report.md](assessment-report.md) | 首次诊断实际完成后 `assessments/initial-report.md`；后续报告用新 ASM ID |
| [learning-plan.md](learning-plan.md) | 诊断有证据后 `progress/plan-NNNNNN.md`；STATE 指向当前版本 |
| [periodic-review.md](periodic-review.md) | 约 7 个实际学习日后 `progress/periodic-review-NNNNNN.md` |
| [material.md](material.md) | 实际采用时 `materials/MAT-NNNNNN.md`，同步登记来源 |

CSV 字段骨架直接使用已建立的七张空表，定义见 [DATA_MODEL](../DATA_MODEL.md)，不再复制第二套错误/词汇模板。项目维护任务追加 [CHANGELOG](../CHANGELOG.md)，学习过程写 Session，两者分开。
