# 官方来源与核验登记

核验日期：**2026-11-01（Asia/Shanghai）**。本次通过保留 TLS 校验的 HTTPS 请求获取资料，检查实际响应和相关正文；没有浏览器登录用户账户实测设置。

## 如何解释证据

- **官方文档已核验**：取得对应正文并核对本库使用的相关段落；不是对所有段落、套餐和客户端做全面验证。
- **本次实测**：本地/Git/网络操作实际执行，见 [VALIDATION](../management/VALIDATION.md)；不能拿它替代产品界面实验。
- **推荐实践**：作者为实现长期维护目标提出的方法，不是平台强制功能。
- **本项目约定**：用户要求的管理机制，例如逐任务日志，落实于 [AGENTS](../AGENTS.md)。
- **待核验**：证据或权限不足；进入 [ROADMAP](../management/ROADMAP.md)，不以猜测填补。

每条记录保留最初 URL、实际目标、访问范围、可支持论断及边界。页面“最近更新”是访问时的动态展示，不能当永久版本号；本表记录核验日期而不推算不可靠的精确更新时间。官方当日说明也不是保证未来不变化的契约。

<a id="o1"></a>

## O1：Projects in ChatGPT

- 原始链接：[Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：项目容器、指令、分享、记忆及套餐边界。
- 读到的结论：正文明确当前可更改记忆设置；共享固定 project-only，且 project-only 不提供 Work。重点用于概念、上下文与协作章。
- 限制与复查条件：记忆模式、跨项目引用、分享与文件限制变化时复核；未登录用户账号界面实测。

<a id="o2"></a>

## O2：ChatGPT Work and Codex

- 原始链接：[ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：Chat/Work/Codex 区分、历史与跨端同步、上下文型号和计费入口。
- 读到的结论：Cloud Work 与 Codex 的不同视图/历史；本地与云端区分；仅作为当前入口说明，不将其泛化为文件自动同步。
- 限制与复查条件：入口、套餐、型号、额度变化快；没有验证用户订阅实际显示的选项。

<a id="o3"></a>

## O3：Iterating development workflows with Codex

- 原始链接：[Iterating development workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：示例工作流、AGENTS、harness、复盘与逐步改进。
- 读到的结论：官方 Cookbook 的示例实践，不是所有项目必须创建的文件清单。阅读了 AGENTS、计划及复盘相关段落，未在真实代码项目执行示例。
- 限制与复查条件：适用于较多阶段工程；小型文档项目应裁剪，不宣称已验证示例代码。

<a id="o4"></a>

## O4：Rethinking skills and prompts for GPT-6 Astra

- 原始链接：[Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：按需披露、精简 skills 与长期指令、明确完成边界。
- 读到的结论：官方博客署日期 2026-09-11；提倡只读所需资料，避免机械流程。是模型相关实践建议，不是所有版本的功能契约。
- 限制与复查条件：换模型或真实任务表现不符时重评；未安装或审计该文提到的 skill。

<a id="o5"></a>

## O5：Custom instructions with AGENTS.md

- 原始链接：[Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：Codex 文件发现、全局/项目指令链、override 和大小限制。
- 读到的结论：原开发者 URL 重定向到 learn.chatgpt.com；当前文档说明启动时沿根到当前目录建立链，每目录至多一份；默认上限 32 KiB 可配置。
- 限制与复查条件：按具体入口/配置检查加载情况；本次未另启动 Codex CLI 做发现规则实验。

<a id="o6"></a>

## O6：Codex Cloud

- 原始链接：[Codex Cloud](https://developers.openai.com/codex/cloud)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/cloud)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：环境准备/发布、每任务独立工作区、跨入口继续。
- 读到的结论：当前云端文档，不与 Codex Cloud (Legacy) 或本地 worktree 混用。支持复用已发布环境，不构成所有未提交内容跨任务同步的保证。
- 限制与复查条件：环境行为和客户端发布流程变化时复核；本次未重新发布环境。

<a id="o7"></a>

## O7：Memory in ChatGPT

- 原始链接：[Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-faq)。
- 实际目标：[重定向后的页面](https://help.openai.com/en/articles/8590148-memory-in-chatgpt)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：记忆来源、个性化、保存记忆与聊天记录差异。
- 读到的结论：记忆不保留每段对话每个细节；控制项依套餐/地区/入口而变，删除聊天不一定删除独立保存记忆。
- 限制与复查条件：不将旧版两个开关界面当作所有账号唯一界面；未执行记忆删除/恢复实验。

<a id="o8"></a>

## O8：Creating and editing GPTs

- 原始链接：[Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-a-gpt)。
- 实际目标：[重定向后的页面](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：自定义 GPT 配置与当前退役迁移限制。
- 读到的结论：当前文档说明个人账号停止新建/发布 GPT，部分工作区存在不同截止和迁移安排；正文给出当日计划日期。
- 限制与复查条件：迁移时间高时效；以账号/工作区通知与官方更新为准，不建议新项目依赖即将退役配置。

<a id="o9"></a>

## O9：Managing projects in the API platform

- 原始链接：[Managing projects in the API platform](https://help.openai.com/en/articles/9186755-managing-your-work-in-the-api-platform-with-projects)。
- 实际目标：[重定向后的页面](https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：API 成员、资源、密钥与支出控制边界。
- 读到的结论：与 ChatGPT Projects 分开；当前文档区分告警、监控与可选 hard limit，不能延用“所有预算都只提醒”作为通则。
- 限制与复查条件：权限与支出控制在后台可能演变；未创建 API 项目或执行付费请求。

<a id="g1"></a>

## G1：About Projects

- 原始链接：[About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：GitHub 看板/表格/路线图与 Issues、PR 关联。
- 读到的结论：GitHub Projects 是跨任务规划，不是保存代码的 repository。
- 限制与复查条件：未为本库创建看板；模板/自动化不是首版必要功能。

<a id="g2"></a>

## G2：About repositories

- 原始链接：[About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：仓库内容、协作与公开/私有访问。
- 读到的结论：用于说明 Git 仓库与 GitHub 承载服务的职责以及资料可见性。
- 限制与复查条件：未改变现有仓库可见性和分享设置。

<a id="g3"></a>

## G3：About pull requests

- 原始链接：[About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)。
- 实际目标：[重定向后的页面](https://docs.github.com/en/pull-requests/reference/pull-requests)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：工作分支评审、PR 与草稿 PR。
- 读到的结论：PR 提供审查入口，不等于合并；草稿不可直接合并。旧 URL 重定向到 reference。
- 限制与复查条件：实际提交、推送、PR 状态另查本次日志，不能从官方介绍推断已经完成。

<a id="o10"></a>

## O10：Worktrees

- 原始链接：[Worktrees](https://developers.openai.com/codex/app/worktrees)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/environments/git-worktrees)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：本地并行、工作树与 Git 分支、Handoff 边界。
- 读到的结论：当前文档区分 Local、Worktree 与移动端远程控制；工作树留在连接的电脑/远程开发环境。
- 限制与复查条件：没有在本任务创建 worktree 或测试 Handoff；云隔离任务无需默认再创建。

<a id="o11"></a>

## O11：旧 security 地址的主题变更

此条只做主题识别，不作为权限机制依据。

- 原始链接：[旧 security 地址的主题变更](https://developers.openai.com/codex/security)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/security)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：URL 核验的反例，不作为权限机制依据。
- 读到的结论：原 /codex/security 目前落到 Codex Security 漏洞扫描产品。不能因名称相同就拿它解释沙箱/审批；改查 O12、O13。
- 限制与复查条件：状态为可访问但主题不适用于原权限论断；保留记录防止以后误用。

<a id="o12"></a>

## O12：Sandbox

- 原始链接：[Sandbox](https://developers.openai.com/codex/sandboxing)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/sandboxing)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：沙箱和审批的不同职责、受限命令执行。
- 读到的结论：已阅读关于技术边界与审批策略的段落；不把一次提示词当作提升权限方式。
- 限制与复查条件：具体 OS/入口和策略不同；没有改变用户沙箱配置。

<a id="o13"></a>

## O13：Permissions

- 原始链接：[Permissions](https://developers.openai.com/codex/permissions)。
- 实际目标：[重定向后的页面](https://learn.chatgpt.com/docs/permissions)。
- 核验：2026-11-01；HTTP 200；访问层级为正文相关段落。
- 支持范围：权限 profiles、文件/网络控制。
- 读到的结论：当前文档标 beta，并区分 permission profiles 与旧 sandbox 配置；本库只解释概念，不提供未经实测的配置迁移步骤。
- 限制与复查条件：beta 语法及组合限制可能变化；未修改配置或测试 profile 迁移。

## 使用与复核规则

正文通过 O/G 编号指向这里；修改功能论断时更新其记录并追查引用页面。发现过期内容先查新官方说明，再标明替代关系，不删除仍有追溯价值的历史。

本库没有要求每个读者具有相同套餐。关键流程应在自己的账号核对模式、权限和入口；未经实际验证的限制放 ROADMAP，而不是把“没有看到按钮”推断成全平台不存在。
