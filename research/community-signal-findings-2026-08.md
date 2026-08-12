# 社区写作 Skill 调研记录（2026-08）

> **整理：** Manus 1.6
> **说明：** 本文记录可复查的社区信号，并区分项目自述、外部讨论和负面反馈；它不是效果保证。

## unslop-text

- **规则与仓库位置：** [`JCarterJohnson/vibecoded-design-tells/unslop-ai-text`](https://github.com/JCarterJohnson/vibecoded-design-tells/tree/main/unslop-ai-text)。
- **公开讨论：** [r/ClaudeAI 讨论帖](https://www.reddit.com/r/ClaudeAI/comments/1udl9hg/unsloptext_a_claude_skill_that_flags_and_removes/)。帖子将其定位为让用户先明确声音、再清除常见模式的 Skill，而不是检测器。
- **可观察信号：** 该帖含约 80 条讨论，因此可作为“有公开社区讨论”的证据；评论不全是正面。
- **重要反证：** 有评论认为示例改写仍读起来像 AI 文本，并质疑它是否与 Humanizer 重复。此类反馈意味着应把它列为“值得试验的候选”，而不是宣称已被证实有效。
- **待核验：** 仓库中的实际规则文件、许可、维护状态、第三方复用以及中文适配情况。

## unslop-text：仓库核验补充

| 核验项 | 可观察结果 | 含义 |
| --- | --- | --- |
| 仓库规模 | 宿主仓库显示约 439 Stars、27 Forks、1 个 Issue。 | 热度中等，不能仅按 Star 判断。 |
| 实际文件 | 目录包含 `skill/`、`README.md`、数据说明、分析脚本、比较数据与 demo。 | 不是只有一句提示词的空壳；具有可审阅工作流与数据材料。 |
| 近期维护 | 页面显示提交 `f7c4aef`，信息为针对上传限制调整 `SKILL.md` 描述。 | 存在面向分发兼容性的近期维护信号。 |
| 讨论的边界 | Reddit 讨论中有正反两类反馈。 | 收录时需用“有争议、值得试验”而非“已验证最好”的措辞。 |

## r/ClaudeCode：Humanizer 讨论中出现的替代规则与工作流信号

| 项目 | 公开讨论中的可核验内容 | 收录价值判断 |
| --- | --- | --- |
| [`Anbeeld/WRITING.md`](https://github.com/Anbeeld/WRITING.md/blob/main/WRITING.md) | 在 [r/ClaudeCode 讨论](https://www.reddit.com/r/ClaudeCode/comments/1sy4137/the_most_useful_claude_skill_i_ever_created/) 中被非发帖者明确推荐；发帖者回复称该规则“excellent”，并打算吸收其中内容更新自己的 Skill。 | 高优先级候选：这是二次推荐加上规则作者间的具体复用信号，不依赖 Star。 |
| [`TimSimpsonJr/prose-craft`](https://github.com/TimSimpsonJr/prose-craft) | 同一讨论帖在资源列表中被分享。 | 候选：需进一步核验其规则内容、维护状态和独立使用证据。 |
| [`angelarose210/ghostwriter`](https://github.com/angelarose210/ghostwriter) | 同一讨论帖在资源列表中被分享。 | 候选：需进一步核验其是否属于可移植写作 Skill，而非泛用应用。 |
| 两阶段编辑工作流 | 讨论正文主张“先加入声音，再处理典型 AI 模式，最后自审”，评论中有人指出这类规则适合后期编辑，也有人建议直接作为生成约束；另有人偏好“更高效的生成提示 + 后编辑”。 | 可收录为实践观察，而不是单一工具的功效证明；显示社区对“生成时约束 vs 后处理”的真实分歧。 |

## Anbeeld/WRITING.md：仓库核验

| 核验项 | 可观察结果 | 收录意义 |
| --- | --- | --- |
| 社区来源 | 非作者用户在 r/ClaudeCode 讨论中主动推荐；相关 Humanizer 作者回复称规则“excellent”，并表示会吸收其中内容。 | 是可回溯的二次复用和同行认可信号。 |
| 规则形态 | 仓库不只是单一 Markdown：包含 `skills/writing`、完整版、compact、mini 版本及变更记录。 | 提供不同上下文窗口和 Agent 容器的可复用形态。 |
| 维护与发布 | 页面显示 20 次提交、11 个标签、10 个以上发布，最新版本为 v1.4.2。 | 有显式版本化与维护信号。 |
| 许可 | README 区域标为 MIT license。 | 便于目录收录与复用。 |
| 规模 | 页面显示约 344 Stars、21 Forks。 | 非头部项目，但有足够的规则维护和社区传播证据。 |

## r/WritingWithAI：规则化“去套话”工作流的有效性与风险

[讨论帖](https://www.reddit.com/r/WritingWithAI/comments/1uqkvla/deslopping_claude_prose/)并未对应一个独立开源仓库，却提供了重要的社区实践证据：发帖者使用“先生成、再逐行编辑”的规则化工作流处理 AI 首稿，并公开了完整规则和改写对照。讨论也给出了关键限制条件。一名高赞评论认为过严的禁用规则可能破坏本来具有抒情性的作者风格；另一位评论则认为不得机械禁止短句。由此可得的收录判断是：目录应该收录**可配置的审校规则**，而不是声称某一套“反 AI 词表”适用于所有文学写作。

## Patina：公开讨论与待核验事项

[r/ClaudeAI 的 Patina 讨论](https://www.reddit.com/r/ClaudeAI/comments/1s9nkst/i_catalogued_112_patterns_that_make_ai_writing/)链接到 [`devswha/patina`](https://github.com/devswha/patina)。讨论中既有用户认可其对“false nuance”等模式的识别，也有多项值得重视的质疑：有人指出发帖文案本身仍有明显模式；有人问改写前后是否改变了意思。因而 Patina 只能作为“有模式清单、获得讨论、但需严格保真审查”的候选。后续需核验仓库规则、许可、维护和外部复用，再决定是否收录。

## Patina：仓库核验补充

| 核验项 | 可观察结果 | 收录意义 |
| --- | --- | --- |
| 规模与维护 | 页面显示约 315 Stars、34 Forks、8 个 Issue、1,077 次提交、16 个标签与多分支。 | 并非大 Star 项目，但维护密度显著，适合列为“工程化候选”。 |
| 语言覆盖 | 仓库标题标为 KO/EN/ZH/JA；`patterns` 的提交说明明确提到四语模式、中文保真注记和中文触发示例。 | 与中文写作目标直接相关，优先级高。 |
| 风格控制 | 仓库有 `document-types`、`personas`、`lexicon`、`patterns`、`core` 等模块；提交说明显示文档类型、人物声音与语域被分开建模。 | 不只是禁词清单，具有风格配置和类型化编辑能力。 |
| 质量控制 | 页面提交信息公开描述了规则快照、测试夹具、发布检查和多语言词表再验证。 | 有可审阅的工程化质量信号，但不等于独立效果已被证明。 |
| 社区反证 | Reddit 讨论提出“是否改掉意思”的合理质疑。 | 目录必须提醒用户：应先在保真敏感文本上逐段试用。 |

## X：plain-writing-skill 的公开传播与复用信号

[Shreya Shankar 的公开 X 帖](https://x.com/sh_reya/status/2066674728396579101)发布 `plain-writing-skill` 时，页面显示约 66.6K 浏览、445 个喜欢与 804 个收藏。更重要的是，回复中有第三方开发者称将相关“坏写作与反模式”材料用于给 Agents 提供示例，另一位回复者称把规则吸收进自己的“更自然写作” Skill 后效果更好。该帖不能独立证明改写质量，但可证明这套规则已进入 Agent 编写者的复用与衍生讨论。它也提醒我们：社区中常见的是**规则的再组合**，而不是只安装单一 Humanizer。

## r/ClaudeAI：写作者的采用建议

[写作 Skills 讨论帖](https://www.reddit.com/r/ClaudeAI/comments/1rrsrjx/what_are_the_best_claude_skills_to_download_for/)中的有效信息不在于推荐“安装越多越好”，而在于具体采用方式：社区总结建议把长期打磨的对话、个人文章样本、履历或风格指南沉淀成**自己的小型规则集**；预制 Skill 只保留日常高频的少数几项。讨论同时明确提醒大量安装会占用上下文。这个观察支持本轮目录把工具拆成“通用审校器”和“个人声音校准模板”，并强调叠加规则应少而精。

## EveryDay-Writer：低 Star 的个人声音工作流候选

| 核验项 | 可观察结果 | 收录意义 |
| --- | --- | --- |
| 规模 | [Deupaxx/EveryDay-Writer](https://github.com/Deupaxx/EveryDay-Writer) 页面显示约 28 Stars、5 Forks。 | 符合“低 Star 但不应被直接忽略”的筛选目标。 |
| 可复用结构 | 仓库包含 `SKILL.md`、`skills/`、`core/`、`onboarding/`、`references/` 与 Claude Code/Cowork 路径。 | 不是单段提示词，具备声音资料、写作流程和持久化组织。 |
| 声音保护设计 | 最新提交引入多声音 profiles，并明确将个人/客户声音资料置于仓库外，避免插件更新或公开提交泄漏资料。 | 对“不要写成统一 AI 声音”有明确的工程化处理。 |
| 维护与许可 | 页面显示 18 次提交、开放 issue/PR、MIT 许可。 | 仍处早期，且外部使用证据较弱；应标为“早期实验候选”，而非强推荐。 |

## 候选仓库：实时元数据核验（2026-08-12）

| 仓库 | Stars / Forks | 许可 | 最近更新 | 初步判断 |
| --- | ---: | --- | --- | --- |
| [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill) | 158 / 25 | MIT | 2026-08-12 | 小众、持续维护；需补第三方效果证据。 |
| [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | 4,846 / 356 | MIT | 2026-08-12 | 不属于低 Star，但具备强传播信号，可作为对照收录。 |
| [TimSimpsonJr/copydesk](https://github.com/TimSimpsonJr/copydesk) | 65 / 4 | MIT | 2026-08-10 | 小众且近期维护；需要进一步确认其与原链接 `prose-craft` 的关系及可用性。 |
| [angelarose210/ghostwriter](https://github.com/angelarose210/ghostwriter) | 61 / 8 | MIT | 2026-08-10 | 小众声音剖析候选；需标注外部采用证据偏弱。 |
| [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills) | 397 / 57 | Apache-2.0 | 2026-08-11 | 社区创作型写作候选；重点核验声音与连续性工作流。 |
| [Deupaxx/EveryDay-Writer](https://github.com/Deupaxx/EveryDay-Writer) | 28 / 5 | MIT | 2026-08-06 | 极小众但有多声音设计；标为早期实验。 |

## r/claudeskills：从通用 Humanizer 到个人声音资料库

在 [“best humanizer skill”讨论](https://www.reddit.com/r/claudeskills/comments/1v8wa5r/whats_the_best_humanizer_skill_out_there/)中，用户的可复用经验是：从多个通用 Skill 中取规则，再用自己手工修订的 before/after 样本训练个人 Skill。该用户认为个性化资料（声音、真实样本、编辑拒绝项、认可改稿、观点和主题）比通用“去 AI 痕迹”清单更能保持写作质量；另一位用户也提到由四个通用 Skill 取长补短后建自己的 Skill。与此同时，讨论中有人明确质疑非可信 GitHub Skill 的安全性。目录的实际建议应因此是：先审阅规则，再从小批工具中提炼自己的声音配置，而不是不加审查地批量安装。

## theclaymethod/unslop：低 Star、工程化评测候选

| 核验项 | 可观察结果 | 收录意义 |
| --- | --- | --- |
| 规模与维护 | [theclaymethod/unslop](https://github.com/theclaymethod/unslop) 页面显示约 50 Stars、3 Forks、119 次提交、3 个开放 PR、5 个分支。 | 小众，但不是一次性提示词仓库。 |
| 规则与工具 | 仓库含 `SKILL.md`、`AGENTS.md`、`CLAUDE.md`、预设、参考规则、脚本和评测目录。 | 可在多个 Agent 环境中审阅和复用。 |
| 编辑机制 | 初始提交说明为“诊断 → 重建”两阶段，含禁用表达、8 项标准、声音预设和验证脚本。 | 具备可理解的风格处理路径。 |
| 保真控制 | 最新提交说明明确存在清洁 no-op、上下文扫描、冻结盲测基准和“preserved every source fact”的测试记录。 | 适合列为“强调事实保真”的实验性候选，但这些自测结果尚非独立第三方验证。 |
