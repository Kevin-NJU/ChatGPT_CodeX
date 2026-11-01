# 案例 4：本知识库如何管理自己的首版建设

**性质：本次实际工作记录；不代表已验证所有 ChatGPT 界面。** 操作结果以 [任务 T001](../management/TASK_LOG.md#t001) 和 [验证报告](../management/VALIDATION.md) 为准，本页解释它们如何配合。

## 从需求到项目边界

用户要求建立《如何更好地使用 ChatGPT 与 Codex 的项目功能》，允许新目录内编写内容，允许工作分支提交/推送/PR，不允许额外合并、强推或发布。实际确认远程为 `Kevin-NJU/ChatGPT_CodeX`、默认分支 main、本地 `/workspace/ChatGPT_CodeX`；初始 HEAD 为 `824e358eb27b54a79b1dfe1cfd367293e5ee0441`，工作区干净。

同仓库已有 `ai-collaboration-handbook/`，其 AGENTS 只管自己的目录。本任务创建独立目录 `how-to-use-chatgpt-codex-projects/`，不修改旧项目或根导航，不创建新仓库或 worktree。分支为 `docs/chatgpt-codex-project-guide`。这就是根据目标边界选目录，而非根据同含“AI”就合并项目。

## 初始化与资料研究

首先查询 Git 远程符号 HEAD 和仓库 API，确认默认分支与访问能力，再读取现有说明和规范。官方资料通过 HTTPS 获取并读取相关正文，保留最初 URL 和重定向目标；对账号界面行为未作推断式“实测”。特别处理了项目记忆设置、Work 历史、GPTs 迁移和旧 security URL 指向不同主题的情况。

架构选择：README 兼任总索引；九章正文分主题；九份提示词是任务入口，六份模板是文件骨架；三个教学演练与本页实际案例分开；五类管理记录各有归属；额外 VALIDATION 保存本次检查证据。无需网站、包管理依赖或服务器。

## 日常使用与跨日恢复

后续用户说“查明共享项目是否能切回默认记忆”时，新会话先读 AGENTS、STATUS，再看相关决定、上下文章与 O1；它应更新原章和来源，而不是重建目录。本次首版状态不意味着所有未来功能已经核验。

可直接复制：

```text
请接手 how-to-use-chatgpt-codex-projects/。先核对 Git 状态，读本目录 AGENTS.md、management/STATUS.md 及与任务相关的决定。
本次目标是核验 [具体功能]，只在本目录更新已有章节和必要记录；区分官方正文与账号界面实测，不编造结果。
完成相关文档/链接和范围检查，按一次用户任务追加 TASK_LOG。当前仅本地，不提交或推送。
```

## 可观察的管理结果与边界

[STATUS](../management/STATUS.md) 表示现在能使用什么、下一步是什么；[日志](../management/TASK_LOG.md) 保存本次发生的事实；[决策](../management/DECISIONS.md) 解释结构与证据策略；[路线图](../management/ROADMAP.md) 留下未实测主题；[变更](../management/CHANGELOG.md) 给读者版本入口。

本次建立文件、核验来源及 Git 操作可审查；跨日真实恢复、ChatGPT 设置操作、多会话冲突演练尚未因这些文档存在就自动完成。后续首次实操可继续追加独立任务记录，再根据证据更新章节。
