# 中文散文风格保持测试：社区写作 Skills 的一次对照

> **测试时间：** 2026-08-12（GMT+8）
> **整理与执行：** Manus 1.6
> **核心问题：** 这些以“Humanizer”“Anti-Slop”“Plain Writing”为目标的社区 Skills，在处理一篇依靠克制、物件和停顿承载亲情的原创中文散文时，是否能保住文风，而不是只把它压短？

## 结论摘要

这次测试的答案是：**能保住叙事骨架，但不一定保得住最细的文气。** 五个候选都没有删去主要情节；但在横向盲评中，差异集中在具体比喻是否被说明化、动作是否被解释化、中文搭配是否自然，以及句法是否被整理得过于平直。

在本次单样本、单次运行下，`Humanizer` 的风格保持得最稳，得到 **88/100**；`avoid-ai-writing` 次之，为 **84/100**；`plain-writing-skill`、`Stop Slop` 与 `humanize` 分别为 **81 / 77 / 66**。这不是通用排名：它只说明这些固定版本的规则在这个输入、这个模型和这组约束下的行为。

> 本报告测试的是**风格保持与风格漂移**，不是压缩率、检测规避，也不评价文本像不像任何现实作者。输入为新写的原创短文，只取克制亲情叙事、以具体物件承载情感、少作直接抒情这些高层写作目标。

## 测试设计

| 项目 | 固定设置 |
| --- | --- |
| 输入 | 原创中文短文《小站》，见 [`input.md`](input.md)。 |
| 测试对象 | [Humanizer][1]、[Stop Slop][2]、[avoid-ai-writing][3]、[plain-writing-skill][4]、[humanize][5]。 |
| 生成模型 | `gpt-5`；所有候选使用相同模型和 `max_completion_tokens=1800`。 |
| 上游规则版本 | 五个 `SKILL.md` 均按固定 commit 拉取；见 [`upstream_commits.tsv`](upstream_commits.tsv) 和 [`skill_checksums.tsv`](skill_checksums.tsv)。 |
| 硬性约束 | 第一人称回忆时序、六项材料细节、克制亲情、自然中文散文；禁止新增事件、动机、象征阐释或“规避检测”主张。 |
| 单项盲评 | `gpt-5.5` 对每个匿名候选按量表评分；见 [`blinded_style_judgments.json`](blinded_style_judgments.json)。 |
| 横向盲评 | `gpt-5.5` 同时比较五个匿名候选，并强制唯一排序、引用候选原文证据；见 [`comparative_style_review.json`](comparative_style_review.json)。 |

输入在六个材料点上设置了强制检查：雨后小站与灯光、蓝布棉袄和黑伞、萝卜烧豆腐及未说破的辞职、牛皮纸包和拉链、雨地中的父亲、两个温热烧饼。完整量表见 [`rubric.md`](rubric.md)。

## 横向风格保持结果

单独打分时，五个候选都很容易因“情节没丢、语句通顺”而得到满分，出现明显的**天花板效应**。因此，下表以要求明确区分细微差异的横向盲评为主，并保留原始单项盲评以便复核。排序与引用均在揭示 Skill 名称之前完成。

| 排名 | Skill | 风格保持分 | 保住的优点 | 关键漂移或损失 |
| ---: | --- | ---: | --- | --- |
| 1 | [Humanizer][1] | 88 | 叙述顺序、父亲动作和大部分物件意象稳定；收束仍落在伞尖、湿地与烧饼上。 | 将“像薄薄铺了一层油”改成“薄薄一层亮光”，湿冷、油亮的触感被说明化；“怕他顺势问起工作”略多解释。 |
| 2 | [avoid-ai-writing][3] | 84 | 主要事件、父亲的沉默照拂和烧饼收束完整；仍保留“薄油似的亮”。 | 开头拆句更整齐；“他给我盛饭，又问”削弱“一面……一面……”的并行；“回望”“原处”略显整理后的书面味。 |
| 3 | [plain-writing-skill][4] | 81 | 中段关于辞职未提、父亲劝慰的克制关系保留较好。 | “像薄薄铺了一层油”变为“反着光”；新增“他迎上来”；“筷子在他手边停了一会儿”搭配不自然。 |
| 4 | [Stop Slop][2] | 77 | 蓝布棉袄、黑伞、牛皮纸包与温烧饼等物象仍在，结尾动作线基本完整。 | “我答得快，绕开工作的事”把原本的隐忍改为解释；“风从门缝里往进挤”“行李侧的小口袋”显出口语或搭配问题。 |
| 5 | [humanize][5] | 66 | 接站、热饭、塞纸包、拆烧饼等叙事骨架未丢。 | “从省城往回走”“灯光压下来”改变朴素叙述；“尽量短”把情绪处理变成策略说明；“伞尖一点一点磕在湿地上”把静态画面改为连续动作。 |

## 为什么这不是“谁写得更好”的绝对结论

五个输出都保住了六项主要材料点，但风格并不只由材料点构成。原文的效果依赖几个更细的层次：雨地被灯照出“薄薄铺了一层油”的不适感；父亲不追问工作；“我答得很快”留着没说透的局促；伞尖只是“点在湿地上”，并不制造额外动作。这些地方一旦被写成解释、动作加码或自然度较低的搭配，故事还在，**叙述的余味却变了**。

下面的例子展示测试观察到的差异；它们是候选输出中的原文片段，不是额外改写建议。

| 现象 | 候选中的证据 | 对风格的影响 |
| --- | --- | --- |
| 具象比喻被说明化 | Humanizer 的“薄薄一层亮光”；plain-writing 的“反着光”。 | 画面仍在，但“油”的黏、冷和暗光感变弱。 |
| 含蓄心理被解释化 | Stop Slop 的“绕开工作的事”；humanize 的“尽量短”。 | 读者原本可从短答和沉默中体会的心事，被提前说破。 |
| 静态画面被动作化 | humanize 的“伞尖一点一点磕在湿地上”。 | 父亲原先停在雨地里的静默，被改成更显眼的舞台动作。 |
| 无根据新增或不自然搭配 | plain-writing 的“他迎上来”；humanize 的“饭又被他回了两遍”。 | 前者新增了原文没有的迎接动作，后者破坏现代中文散文的自然度。 |

## 原始结果与复现

每个候选输出都已单独保存：[`outputs/humanizer.md`](outputs/humanizer.md)、[`outputs/stop-slop.md`](outputs/stop-slop.md)、[`outputs/avoid-ai-writing.md`](outputs/avoid-ai-writing.md)、[`outputs/plain-writing.md`](outputs/plain-writing.md) 和 [`outputs/humanize.md`](outputs/humanize.md)。生成模型配置和令牌记录在 [`generation_results.json`](generation_results.json) 中。

复现时，先执行 `bash fetch_upstream_skills.sh` 下载固定提交对应的规则快照，再依次运行 `run_style_generation.py`、`run_style_judges.py` 和 `run_comparative_style_review.py`。`skills/` 目录不随仓库提交，以避免镜像第三方规则文件；可用 `skill_checksums.tsv` 核验下载内容。评审脚本的第一次 Claude 结构化输出尝试因代理返回无效 JSON 而未用作结论；最终保留的盲评和横向评审均由 `gpt-5.5` 产生，并完整保留在 JSON 中。

## 局限

本测试只是一篇原创中文短散文的单次运行。它没有测长篇小说的一致性、不同地域汉语、复杂人物声音、不同模型、不同温度、不同版本的上游规则，或人工编辑者之间的一致性。尤其需要注意，四个核心 Skills 的原始规则主要以英文写成；它们在中文输入上的行为不应被直接推断为其官方支持范围。

要建立更有说服力的结论，下一轮应扩展为至少三种中文体裁（散文、网文叙事、非虚构说明）、多个原创样本、多次运行，并加入中文母语编辑的盲审。此处的价值是把“去 AI 味”的泛泛说法落到可检查的问题上：**哪些物件被删了、哪些含蓄被说破了、哪些句子被改平了。**

## 参考资料

[1] [blader/humanizer](https://github.com/blader/humanizer)

[2] [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

[3] [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)

[4] [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill)

[5] [harshaneel/humanize](https://github.com/harshaneel/humanize)
