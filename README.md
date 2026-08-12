# Awesome AI Writing

一个以**中文创作**为重点、兼收英文资源的开源项目索引，集中收录 **AI 小说、中文网文、长篇叙事、AI 写作工作台、故事生成、写作 Agent、Prompt/工作流**，以及 **改善文本自然度的编辑与审校工具**。

> **最近一次策展整理：2026-08-12（GMT+8），由 Manus 1.6 完成。**本轮优先补充近期仍有维护、公开可访问且能服务简体中文或繁体中文写作的项目、Skills 与研究资料。

> 本仓库是链接目录，不复制、镜像或打包被收录项目的源码。请在使用前自行核查许可证、隐私政策、依赖、模型服务条款和维护状态。

## 目录

- [中文写作精选（近期核验）](#中文写作精选近期核验)
- [AI 小说与长篇叙事](#ai-小说与长篇叙事)
- [AI 写作工作台与编辑器](#ai-写作工作台与编辑器)
- [故事、短剧与多媒体叙事](#故事短剧与多媒体叙事)
- [AI 写作研究与基础设施](#ai-写作研究与基础设施)
- [去除 AI 味道与文本人类化](#去除-ai-味道与文本人类化)
- [收录标准](#收录标准)
- [提交项目](#提交项目)

## 中文写作精选（近期核验）

下表优先列出本轮实际核验过公开仓库、维护记录和项目说明的中文资源。它们适合小说连载、公众号/博客等内容创作、编辑改稿和繁体中文本地化；并非对文本来源或任何检测结果作出保证。

| 资源 | 面向场景 | 核心特点 |
| --- | --- | --- |
| [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 中文长篇/短篇网文 | 以 Skill 包串联扫榜、拆文、写作、审校、文本自然化与封面图流程，并适配多种 Agent CLI。 |
| [AI-Novel-Writer](https://github.com/EthanYoQ/AI-Novel-Writer) | 中文长篇小说 | 本地小说工作台，提供大纲、角色、章节蓝图、审稿修稿、知识库和本地模型支持。 |
| [InkWise 墨智](https://github.com/scpuny/inkwise) | 文章、专栏与多平台发布 | 中文桌面编辑器，支持富文本/Markdown、可扩展写作 Skills、上下文索引、全文检索与微信/头条发布。 |
| [human-writing](https://github.com/KKKKhazix/human-writing) | 中文创作与改稿 | 通用写作 Skill，覆盖公众号、知乎、博客、论坛、小说等文体，并提供修订流程和检测脚本。 |
| [speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw) | 繁体中文内容、行销与办公文本 | 针对繁体中文的改稿 Skill，支持台湾用语与标点本地化，并按写作场景调整处理力度。 |

## AI 小说与长篇叙事

| 项目 | 简介 | 语言 |
| --- | --- | --- |
| [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 面向中文长篇与短篇网文的全流程 Skill 包，包含扫榜、拆文、写作、审校、文本自然化与封面图流程，兼容 Claude Code、Codex CLI、OpenCode、OpenClaw、ZCode 和 Reasonix。 | JavaScript |
| [web-novel-writing-guidance-skill](https://github.com/HZ-KMNO/web-novel-writing-guidance-skill) | 面向连载中文网文的便携式写作 Skill，覆盖章节蓝图、角色自主性、连贯性、分稿修订与长期项目管理。 | Markdown |
| [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) | 多章节长篇小说生成，处理上下文衔接与伏笔。 | Python |
| [AI-Novel-Writing-Assistant](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant) | AI Native 长篇小说创作系统，包含 Agent、世界观、RAG 和整本生产流程。 | TypeScript |
| [AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels) | AI 小说生产力工具，包含拆书、书名简介、正文生成和润色。 | JavaScript |
| [MaliangAINovalWriter](https://github.com/Deng-m1/MaliangAINovalWriter) | 面向中文网文的多智能体小说创作平台，支持三级大纲、知识图谱一致性和长篇连载。 | 未标注 |
| [Ai-Novel](https://github.com/inliver233/Ai-Novel) | AI 小说创作网站。 | Python |
| [show-me-the-story](https://github.com/Nigh/show-me-the-story) | 自托管小说生成器，支持大纲、逐章写作、审稿、伏笔和事实检查。 | Go |
| [MuMuAINovel](https://github.com/xiamuceer-j/MuMuAINovel) | AI 智能小说创作助手。 | Python |
| [ai_novel](https://github.com/duoyang666/ai_novel) | AI 小说实验项目。 | Svelte |
| [AI_Novel](https://github.com/kele-tao/AI_Novel) | 支持世界观、思维库和任务管理的 AI 小说创作系统。 | Python |

## AI 写作工作台与编辑器

| 项目 | 简介 | 语言 |
| --- | --- | --- |
| [InkWise 墨智](https://github.com/scpuny/inkwise) | 面向中文写作者的桌面应用，支持富文本/Markdown、续写/改写/润色等写作 Skills、文章与项目上下文、SQLite FTS5 检索及微信/头条发布。 | TypeScript |
| [AI-Novel-Writer](https://github.com/EthanYoQ/AI-Novel-Writer) | 本地中文小说写作工作台，支持大纲、角色关系、章节蓝图、审稿修稿、知识库和本地模型，并提供 Windows/macOS 客户端。 | TypeScript |
| [vela](https://github.com/heider-x/vela) | 本地优先、隐私友好的 AI 小说写作 IDE，支持本地模型、RAG 和 BYOK。 | TypeScript |
| [storyforge](https://github.com/yuanbw2025/storyforge) | AI 小说创作工作台。 | TypeScript |
| [flymd](https://github.com/flyhunterl/flymd) | Markdown 笔记工具，包含本地知识库和 AI 小说引擎。 | JavaScript |

## 故事、短剧与多媒体叙事

| 项目 | 简介 | 语言 |
| --- | --- | --- |
| [ai_story](https://github.com/xhongc/ai_story) | AI 视频、动漫、短剧和漫剧自动化生成工具。 | Python |
| [clapper](https://github.com/jbilcke-hf/clapper) | 面向 AI 电影时代的视频合成与编排工具。 | TypeScript |

## AI 写作研究与基础设施

研究资源用于理解中文 AI 生成文本的文体特征、质量评估与检测边界；它们不应被解读为规避平台规则或绕过检测的教程。已有研究指出，中文社交文本的人类与 AI 文体存在可分析差异，而短文本、可解释性与真实数据集仍是重要挑战。[1] [2] 另见本仓库的[中文 AI 写作与文本自然化研究线索](research/中文AI写作与文本自然化.md)。

| 资源 | 简介 | 类型 |
| --- | --- | --- |
| [Linguistic Differences between AI and Human Comments in Weibo](https://aclanthology.org/2025.ccl-1.64/) | CCL 2025 论文。基于真实微博评论数据研究中文 AI 与人类短文本的文体特征，并提出可解释的轻量检测方法。 | 研究论文 |
| [Research on AI-generated Chinese text detection method based on deep learning](https://www.aimspress.com/article/doi/10.3934/bdia.2025016?viewType=HTML) | 2025 年公开论文，探索结合 RoBERTa 语义表征与文本统计特征的中文 AI 生成文本检测方法。 | 研究论文 |
| [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | AI 研究写作与润色资源集合。 | 资源目录 |
| [Ollama](https://github.com/ollama/ollama) | 本地运行大语言模型的基础设施，适合构建私有写作工作流。 | Go |
| [Langfuse](https://github.com/langfuse/langfuse) | 开源 LLM 工程平台，提供 Prompt、数据集、评估和可观测性。 | TypeScript |
| [SiYuan](https://github.com/siyuan-note/siyuan) | 开源、隐私优先、自托管的知识工作空间，可作为写作知识库。 | TypeScript |

## 去除 AI 味道与文本人类化

这一类资源用于识别或减少模板化、套话、过度规整、机械连接词、翻译腔等 AI 写作特征。**“更自然”不等于规避检测器**；应把这些资源作为编辑、风格审校和可读性辅助工具，并由作者保留事实核查、引文核对、价值判断和最终责任。特别是在学术、新闻、求职和商业沟通中，不能将改写视为替代原创或替代披露义务。

| 项目 | 简介 | 语言 |
| --- | --- | --- |
| [human-writing](https://github.com/KKKKhazix/human-writing) | 面向中文创作与改稿的通用 Agent Skill，覆盖多种中文写作场景，附修订流程、体裁规则和检查脚本。 | Python |
| [speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw) | 繁体中文改稿 Skill，覆盖内容创作、行销文案和办公文本；支持台湾用语、标点本地化与情境分级。 | Python |
| [Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW) | 基于已有 Humanizer 规则的繁体中文 Agent Skill 翻译与本地化版本。 | 未标注 |
| [writing-humanizer](https://github.com/shyuan/writing-humanizer) | 面向台湾正体中文的 Claude Code 插件，用于审校并改善机械化的 AI 写作痕迹。 | JavaScript |
| [ai-to-human-zh](https://github.com/Holden323/ai-to-human-zh) | 面向简体中文文本的编辑工具包，提供检查与改写工作流。 | Python |
| [humanizer](https://github.com/blader/humanizer) | 去除 AI 生成文本痕迹的通用 Agent Skill。 | Python |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | 减少 AI 套话和常见写作习惯的 Skill。 | 未标注 |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | Humanizer 的中文版本。 | 未标注 |
| [humanize-text](https://github.com/lynote-ai/humanize-text) | 提升 AI 草稿可读性和自然节奏的开源流程。 | Python |
| [humanize](https://github.com/harshaneel/humanize) | 基于研究资料的 LLM 无关文本自然化 Skills。 | HTML |
| [humanizer-ru](https://github.com/smixs/humanizer-ru) | 面向俄语文本的 AI 写作痕迹审计与自然化 Skill。 | Python |
| [humanizer-de](https://github.com/marmbiz/humanizer-de) | 面向德语文本的 AI 写作模式审计与证据安全改写。 | Python |
| [AI-Text-Humanizer-App](https://github.com/DadaNanjesha/AI-Text-Humanizer-App) | 将 AI 文本改写为更自然的正式或学术表达。 | Python |
| [AI-content-detector-Humanizer](https://github.com/DadaNanjesha/AI-content-detector-Humanizer) | AI 内容检测与自然化改写 Web 应用。 | Python |
| [StealthHumanizer](https://github.com/rudra496/StealthHumanizer) | 多语言文本自然化工具，支持多种提供商、风格和语气。 | TypeScript |
| [humanize-ai](https://github.com/sanjaysah101/humanize-ai) | 使用 NLP 和模型处理 AI 文本自然度的系统。 | TypeScript |
| [AI-Human](https://github.com/wx5352/AI-Human) | AI 写作去痕工具。 | TypeScript |
| [humanize-ai-writing](https://github.com/haidrrrry/humanize-ai-writing) | 减少 AI 写作特征的系统 Prompt 与 Skill。 | JavaScript |
| [anti-ai-writing-claude-skill](https://github.com/avikbal-dm/anti-ai-writing-claude-skill) | 面向 Claude 的 AI 写作自然化 Skill。 | 未标注 |
| [humanizer-workbench](https://github.com/aprempeh-tech/humanizer-workbench) | CLI 与 Claude Code Skill，用于发现 AI 写作模式并改善语气和节奏。 | Python |
| [humanize-writing](https://github.com/aaaronmiller/humanize-writing) | 去除 AI 写作习惯、调整语气。 | JavaScript |
| [humanizer-AI-writing](https://github.com/Hessevalentino/humanizer-AI-writing) | 基于 AI 写作特征清单的自然化写作工具。 | 未标注 |

## 收录标准

- 项目必须有公开可访问的代码、文档或 Skill 仓库链接。
- 优先收录具有明确用途、可运行说明、许可证或近期维护记录的项目。
- 对于中文资源，优先收录能明确说明其服务简体中文、繁体中文、中文网文、中文长文写作或中文本地化需求的项目。
- 收录描述只用于导航，不代表本仓库维护者为项目质量、输出内容、版权归属、隐私或合规性背书。
- 不收录明显窃取内容、恶意软件、虚假检测保证，或以绕过平台规则、学术诚信规则为主要目的的项目。
- 项目状态会变化；提交 PR 时请补充项目当前用途、许可证和最后维护情况。

## 提交项目

请通过 [Issue 模板](https://github.com/zolipx/awesome-ai-writing/issues/new?template=add-project.md) 或 Pull Request 提交。请提供：

1. 项目完整公开链接。
2. 项目所属类别与服务的中文写作场景（如适用）。
3. 一句话功能说明。
4. 主要语言或运行方式。
5. 许可证（如能确认）。
6. 最后维护时间或可核验的活跃信号。
7. 为什么它对 AI 小说、中文创作或 AI 写作有帮助。

## 参考资料

[1] [Li, Z. & Zhang, Q. (2025). *Linguistic Differences between AI and Human Comments in Weibo: Detect AI-Generated Text through Stylometric Features*. CCL 2025.](https://aclanthology.org/2025.ccl-1.64/)

[2] [Research on AI-generated Chinese text detection method based on deep learning (2025). *Big Data and Information Analytics*.](https://www.aimspress.com/article/doi/10.3934/bdia.2025016?viewType=HTML)

## 许可证

本目录内容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布。被收录项目的代码、名称、商标和许可证仍归各自项目所有。
