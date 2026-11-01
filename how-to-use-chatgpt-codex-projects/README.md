# 如何更好地使用 ChatGPT 与 Codex 的项目功能

**ChatGPT & Codex Project Usage and Management Guide** · v0.1.0 · 2026-11-01

这是持续维护的个人知识库与实践手册：用 ChatGPT 讨论和研究，用 Codex 处理可验证文件工作，用 Git/GitHub 保存历史和审查成果。核心是降低重复劳动、保存重要上下文、提高长期工作可靠性；不是一套应用，也不要求每个项目搭建复杂框架。

## 快速开始

1. 不清楚几个“项目”的区别，先读 [产品概念](docs/01-concepts.md)；准备新任务，先用 [选型决策表](docs/02-project-decisions.md)。
2. 建立新项目：读 [架构](docs/03-project-architecture.md)，复制 [初始化提示词](prompts/01-initialize-project.md)，按规模选择模板。
3. 隔天继续：复制 [恢复提示词](prompts/03-resume-work.md)，核对实际目录、分支、状态与来源；不要求 AI 凭记忆复述全部旧对话。
4. 做具体工作：使用 [任务执行提示词](prompts/04-execute-task.md) 和 [清单](templates/task-checklist.md)，明确路径、验收和 Git 授权。
5. 接手本库：先读 [AGENTS](AGENTS.md)、[当前状态](management/STATUS.md) 及相关决定，再按需读章节；结束按独立用户任务记日志。

可直接发给下一次 Codex 会话：

```text
请维护 how-to-use-chatgpt-codex-projects/，先核对 Git 状态并读取本目录 AGENTS.md、management/STATUS.md 及与任务有关的决定。
本次目标：[目标]；只改本目录，优先更新现有章节。按需查官方来源，区分事实、实测、建议与待核验。
完成相关内容和链接检查，按一次独立用户任务追加 TASK_LOG，并报告结果、证据、限制和下一步。本次仅本地，不提交或推送。
```

## 内容和证据边界

首版已含可阅读正文、实际可复制的提示词与模板。官方功能按 **2026-11-01** 取得的资料核验，受套餐、工作区、客户端和版本影响；不能把文档访问当作用户账号界面实测。正文明确区分官方功能、推荐实践、本项目约定和待核验内容，来源见 [SOURCES](references/SOURCES.md)。

三个通用案例是教学演练；[本库案例](examples/04-this-guide.md) 记录实际建设过程。真实跨日、跨设备和复杂并行仍列为 [后续研究](management/ROADMAP.md)。当前结构检查结果见 [VALIDATION](management/VALIDATION.md)，不宣称“所有平台行为均通过”。

## 最终目录结构

```text
how-to-use-chatgpt-codex-projects/
├── README.md                 项目入口与唯一总索引
├── AGENTS.md                 本目录的 Codex 工作约定
├── docs/                     九章理论与操作指南
├── prompts/                  九类可复制任务提示词
├── templates/                六份文件与检查模板
├── examples/                 三个教学演练与一个实际案例
├── references/SOURCES.md     官方资料、核验日期和边界
└── management/               状态、路线图、任务、变更、决策与验证
```

## 完整文件索引

下面覆盖本项目全部文件；新增章节也必须从这里或相关章节入口可达，不另维护重复总目录。

### 项目入口

- [README：本页](README.md)
- [AGENTS：持续工作规范](AGENTS.md)

### 系统指南

- [1. 产品概念与边界](docs/01-concepts.md)
- [2. 项目选型、拆分与合并](docs/02-project-decisions.md)
- [3. 文件架构与职责](docs/03-project-architecture.md)
- [4. 上下文、记忆与文件管理](docs/04-context-memory-files.md)
- [5. 长期指令与提示词设计](docs/05-instructions-prompts.md)
- [6. 执行、跨日恢复与失败处理 SOP](docs/06-execution-recovery.md)
- [7. 协作、安全与成本](docs/07-collaboration-security-cost.md)
- [8. 案例选择与检查清单](docs/08-cases-and-checklists.md)
- [9. 如何维护本知识库](docs/09-maintaining-this-guide.md)

### 可复制提示词

- [项目初始化](prompts/01-initialize-project.md)
- [需求分析](prompts/02-analyze-requirements.md)
- [跨日期继续工作](prompts/03-resume-work.md)
- [任务执行与验收](prompts/04-execute-task.md)
- [知识库扩展与去重](prompts/05-expand-knowledge-base.md)
- [定期检查](prompts/06-periodic-review.md)
- [项目复盘](prompts/07-retrospective.md)
- [迁移与交接](prompts/08-handoff.md)
- [安全检查](prompts/09-security-review.md)

### 文件与日志模板

- [ChatGPT Project Instructions](templates/chatgpt-project-instructions.md)
- [最小 AGENTS.md](templates/agents.md)
- [当前状态](templates/status.md)
- [决策条目](templates/decision-record.md)
- [任务日志条目](templates/task-log-entry.md)
- [任务检查清单](templates/task-checklist.md)

### 完整案例

- [长期学习与学术研究](examples/01-research.md)
- [Codex 维护代码工程](examples/02-code-project.md)
- [持续扩展个人知识库](examples/03-knowledge-base.md)
- [本知识库的实际管理示范](examples/04-this-guide.md)

### 来源与管理

- [SOURCES：官方资料登记](references/SOURCES.md)
- [STATUS：当前状态与下一步](management/STATUS.md)
- [ROADMAP：未来候选与完成条件](management/ROADMAP.md)
- [TASK_LOG：逐用户任务执行事实](management/TASK_LOG.md)
- [CHANGELOG：读者可见的重要变更](management/CHANGELOG.md)
- [DECISIONS：长期选择及理由](management/DECISIONS.md)
- [VALIDATION：首版检查证据与限制](management/VALIDATION.md)

## 维护与版本规则

优先更新现有章节，只有独立问题才新增；新内容更新索引和相关交叉引用。每条独立任务必须有执行摘要与日志，其他管理记录按职责更新，避免机械复制。产品说明有新版本时复查来源、标明失效或替代关系；AGENTS 保留短而稳定的规则，细节留在章节。

沿用 `ChatGPT_CodeX` 根 Git，不创建嵌套仓库，不自动修改其他项目。是否提交、推送或创建 PR 以当前任务授权为准；未获额外授权不合并默认分支、不强推、不发布环境或部署。指南可迁移到其他项目，但目录与日志规则是管理选择，不是平台统一强制要求。
