# 参考文献与核验登记

核验日期：2026-11-01。此表记录本次**实际可访问范围**，不将“页面返回成功”“书目已确认”写成“全文已审查”。优先请求出版方或作者材料；遇到访问失败后，使用明确标注的书目／摘要索引。暂不在仓库复制第三方全文；以下链接与书目信息便于继续核对。

原讨论的机构图标不具备完整引文信息。R1、R2 是根据原讨论描述定位的对应研究；R3、R4 是具名方法来源；R5、R6 是本次补充的可核对文献，**不是声称恢复了原讨论中所有未具名引用**；R7 是编辑新增的迁移边界参考。

<a id="r1"></a>
## R1：科学摘要的过度泛化

- Peters, Uwe; Chin-Yee, Benjamin. (2025). *Generalization bias in large language model summarization of scientific research*. Royal Society Open Science, 12, 241776.
- DOI：[10.1098/rsos.241776](https://doi.org/10.1098/rsos.241776)。
- 实际取得：[Crossref 登记记录](https://api.crossref.org/works/10.1098/rsos.241776)，包括标题、作者、日期及出版方提交的摘要；[出版方页面](https://royalsocietypublishing.org/doi/10.1098/rsos.241776)返回 HTTP 403。
- 已核对：登记摘要明确报告 10 个模型、4,900 份生成摘要与原科学文本的比较，以及受测模型过度泛化的现象。
- 未核对：全文方法、各实验子样本、标注流程及结果表。首版不传播脱离任务条件的固定错误率，也不据此断言所有当前模型表现。
- 对应正文：[优势与风险](../docs/reading/02-benefits-and-risks.md)、[理论与证据](../docs/reading/06-theory-and-evidence.md)。

<a id="r2"></a>
## R2：长摘要的位置偏差与忠实性

- Wan, David; Vig, Jesse; Bansal, Mohit; Joty, Shafiq. (2025). *On Positional Bias of Faithfulness for Long-form Summarization*. NAACL-HLT 2025, Volume 1: Long Papers, pp. 8791–8810.
- [ACL Anthology 正式页面](https://aclanthology.org/2025.naacl-long.442/)、[正式 PDF](https://aclanthology.org/2025.naacl-long.442.pdf)。
- 实际取得：页面和 20 页 PDF；转文本后阅读摘要、引言、研究问题与发现表、结论、局限等相关部分。未运行代码，未逐项复验全部实验、图像和附录。
- 已核对：论文研究位置、顺序与长摘要忠实性的关系，报告特定任务中的 U 形和开头偏向等模式；局限承认未覆盖全部模型和数据。
- 边界：忠实性与覆盖度并非同一指标；不能将受测结果概括为“所有模型都必然忽略中间部分”。
- 对应正文：[理论与证据](../docs/reading/06-theory-and-evidence.md)。

<a id="r3"></a>
## R3：横向阅读

- Wineburg, Sam; McGrew, Sarah. (2019). *Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information*. Teachers College Record, 121(11).
- DOI：[10.1177/016146811912101102](https://doi.org/10.1177/016146811912101102)。
- 实际取得：[Crossref 的书目及结构化摘要](https://api.crossref.org/works/10.1177/016146811912101102)；[SAGE 出版方页面](https://journals.sagepub.com/doi/10.1177/016146811912101102)返回 HTTP 403。未读全文。
- 已核对：摘要描述 45 位参与者，包括 10 位历史学者、10 位专业核查人员与 25 位学生；报告核查人员的横向核验做法及任务表现。
- 边界：专家与新手观察比较，不是 AI 工作流的因果试验，也不是所有网页评估的统一效果估计。
- 对应正文：[来源核验](../docs/shared/source-verification.md)、[横向阅读](../docs/reading/06-theory-and-evidence.md#lateral-reading)。

<a id="r4"></a>
## R4：三遍阅读法

- Keshav, S. *How to Read a Paper*. 作者版本，封面注明 Version of February 17, 2016。
- [作者机构托管 PDF](https://svr-sk818-web.cl.cam.ac.uk/keshav/papers/07/paper-reading.pdf)。
- 实际取得并阅读：2 页 PDF 转文本全文。版本日期从文内核对；URL 路径中的 `07` 不用于推定本次读取的是早期版本。
- 已核对：第一遍概览、第二遍理解主要内容、第三遍尝试重建，并根据需要决定是否继续；全文还讨论文献调研。
- 边界：经验方法文章，不是对“三遍法最佳”的实验验证。手册中 AI 分工由编辑新增。
- 对应正文：[三遍阅读法](../docs/reading/06-theory-and-evidence.md#three-pass)。

<a id="r5"></a>
## R5：提取练习综述

- Roediger, Henry L., III; Butler, Andrew C. (2011). *The critical role of retrieval practice in long-term retention*. Trends in Cognitive Sciences, 15(1), 20–27.
- DOI：[10.1016/j.tics.2010.09.003](https://doi.org/10.1016/j.tics.2010.09.003)。
- 实际取得：[Crossref 书目](https://api.crossref.org/works/10.1016/j.tics.2010.09.003)和 [Europe PMC 收录摘要](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.tics.2010.09.003&format=json&resultType=core)，PMID 20951630。DOI 转向出版方的请求遇到 403，未读全文。
- 已核对：综述摘要报告提取练习相对于重复学习对长期保持的益处，以及反馈和不同情境提取的讨论。
- 边界：不能据此保证一次自测、每种 AI 提示词或本手册六步流程的效果。
- 原讨论的 Annual Reviews 未具名综述仍未定位；本条是明示补充，不将期刊和年份移植给原引用。
- 对应正文：[提取练习](../docs/reading/06-theory-and-evidence.md#retrieval-practice)。

<a id="r6"></a>
## R6：自我解释元分析

- Bisra, Kiran; Liu, Qing; Nesbit, John C.; Salimi, Farimah; Winne, Philip H. (2018). *Inducing Self-Explanation: a Meta-Analysis*. Educational Psychology Review, 30, 703–725.
- DOI：[10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)。
- 实际取得：[Springer 出版方页面及摘要](https://link.springer.com/article/10.1007/s10648-018-9434-x)，正文需要订阅；未获取全文。
- 已核对：摘要报告 64 份研究报告中的 69 个效应量，以及自我解释提示的总体正向结果。
- 边界：不将总体结果当作每种任务都有效，不把 AI 代写解释等同于学习者生成解释。首版不借摘要推断未经检查的子组结果。
- 对应正文：[自我解释](../docs/reading/06-theory-and-evidence.md#self-explanation)。

<a id="r7"></a>
## R7：学习迁移的条件与分类

- Barnett, Susan M.; Ceci, Stephen J. (2002). *When and where do we apply what we learn? A taxonomy for far transfer*. Psychological Bulletin, 128(4), 612–637.
- DOI：[10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)。
- 实际取得：[Crossref 书目](https://api.crossref.org/works/10.1037/0033-2909.128.4.612)及 [Europe PMC 收录摘要](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1037%2F0033-2909.128.4.612&format=json&resultType=core)，PMID 12081085。APA 页面只返回动态加载壳，未取得正文。
- 已核对：摘要提出多维迁移框架，并反对忽略条件而笼统估计远迁移。
- 边界：不据此证明 AI 阅读必然带来迁移；本手册的新情境练习是实践建议。
- 对应正文：[学习迁移](../docs/reading/06-theory-and-evidence.md#transfer)。

## 待继续核实的内容

1. S001 中未具名的 Annual Reviews 综述及“+1”所代表的另一来源。
2. R1、R3、R5、R6、R7 的全文方法与具体限制；首版已有陈述仅使用可取得范围。
3. 特定 AI 协同阅读方式对长期独立思考、依赖与迁移的直接证据。原讨论的风险提醒不作为已证明的因果结论。

网络与访问错误只说明本次访问结果，不证明文献不存在。未来核验后应更新条目、正文边界及重要变化记录。
