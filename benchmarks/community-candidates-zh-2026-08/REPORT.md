# 社区小众写作 Skills：中文风格保持复核

> **测试时间：** 2026-08-12（GMT+8）
> **整理与执行：** Manus 1.6
> **目的：** 在社区讨论、分发与维护信号之外，用同一篇原创中文散文检查候选规则是否真的能保住文气，而非只删掉显眼措辞。

## 结论摘要

本轮优先选择了不完全依赖 Star 数的候选：有的来自开发者社区的二次推荐，有的有可审阅的评测结构，有的被明确用于声音资料库。四个规则成功完成了与上一轮完全相同的中文散文风格保持测试；`Patina` 因其完整规则上下文在本次 `gpt-5` 请求中返回 502，未被列入效果排名。

在成功候选中，低 Star 的 [`UNSLOP`][1] 表现最稳，盲态横向风格保持分为 **96/100**；高传播对照 [`no-ai-slop`][2] 为 **92/100**；小众 [`humanizer-skill`][3] 为 **88/100**；在社区中被二次推荐的 [`WRITING.md`][4] 为 **80/100**。这些数字只适用于一个原创中文散文样本、一次运行、固定版本的规则和固定模型，**不是通用排行榜**。

| 候选 | GitHub Stars（2026-08-12） | 社区或工程信号 | 本轮中文风格测试 | 建议定位 |
| --- | ---: | --- | --- | --- |
| [UNSLOP][1] | 50 | 两阶段诊断—重建、规则验证、冻结盲测和事实保真门槛均可在仓库审阅。 | 96/100，第 1。 | **优先试用**：适合先做保真敏感的后编辑。 |
| [no-ai-slop][2] | 4,846 | 社区传播广、公开规则明确；本次作为高传播对照。 | 92/100，第 2。 | **对照型选择**：适合需要透明禁用模式与改动说明的团队。 |
| [humanizer-skill][3] | 158 | 53 模式、声音选择和多 Agent 适配；近期维护。 | 88/100，第 3。 | **值得试验**：本轮中文表现不错，但独立讨论证据仍较少。 |
| [WRITING.md][4] | 344 | r/ClaudeCode 中被非作者推荐，相关作者表示会吸收其规则；有版本、compact/mini 形态与 MIT 许可。 | 80/100，第 4。 | **结构化编辑规则集**：适合做团队基线后再本地化。 |
| [Patina][5] | 315 | 四语模式、中文触发示例、人物声音/文档类型模块及活跃工程维护。 | 未排名：完整规则导致本次请求 502。 | **中文优先观察项**：先小样、逐段校对后再接入。 |
| [unslop-text][6] | 439（宿主仓库） | r/ClaudeAI 有约 80 条公开讨论；基于社区文本模式的数据和扫描器。讨论意见分裂。 | 未测。 | **研究型观察项**：适合拿自己的文本做前后对照，不能据此宣称已证实最佳。 |
| [EveryDay-Writer][7] | 28 | 多声音 profile、个人/客户资料隔离、13 个子 Skill、MIT。 | 未测。 | **早期声音资料库候选**：最适合把自己的修订积累成长期声音约束。 |

## 统一测试方法

测试输入是本仓库原创短文《小站》，而不是任何在世或已发表作者的文本。它采用克制亲情叙事、第一人称回忆、具体物件和停顿承载情感的写法。所有成功候选使用同一输入、`gpt-5`、同一输出上限和同一保真约束；六个材料点、风格量表和原文均在 [`input.md`](input.md) 与 [`rubric.md`](rubric.md) 中公开。

> 评审关注的不是“能否绕过检测”，而是**是否保住叙述视角、雨地意象、未说出口的情感、中文搭配和关键动作**。盲态评审者只看到 `candidate_1` 至 `candidate_4`，在给出唯一排名后才显示规则名称。

| 排名 | Skill | 风格保持分 | 盲态评审的关键发现 |
| ---: | --- | ---: | --- |
| 1 | UNSLOP | 96 | 基本保留白描、停顿和物件，只把“灯光一照”略改为更实的比喻落点，细部漂移最小。 |
| 2 | no-ai-slop | 92 | 时序与含蓄收束稳定；“把我肩上的行李袋提了提”稍微说实了父亲替我整理的动作。 |
| 3 | humanizer-skill | 88 | 材料和克制关系完整，但“灯光斜落”“一面给我盛饭”等修饰/句法使改写痕迹更明显。 |
| 4 | WRITING.md | 80 | 故事未丢，但“雨后初凉”“还挂着下午的水气”“绕开别的”等表达更修饰或更解释化，削弱白描。 |

完整的匿名映射、分数、证据引语和令牌记录见 [`comparative_style_review.json`](comparative_style_review.json) 与 [`generation_results.json`](generation_results.json)。四份输出可逐篇对照：[`UNSLOP`](outputs/unslop.md)、[`no-ai-slop`](outputs/no-ai-slop.md)、[`humanizer-skill`](outputs/humanizer-skill.md)、[`WRITING.md`](outputs/writing-md.md)。

## 社区讨论给出的更重要结论

社区讨论并不支持“找一个万能 Humanizer，然后套到所有文本上”。在 [r/ClaudeCode 的实际讨论][8] 中，用户把后期编辑分成“先补声音、再扫常见模式、最后自审”，也有人主张把约束放在生成时而非只靠后处理。另一则 [r/WritingWithAI 讨论][9] 显示，严格禁词或禁句法规则可能毁掉抒情性的作者声音；在 [r/claudeskills 的比较帖][10] 中，用户更推荐从多个规则中提取有用部分，再用手工修订的 before/after 样本建立自己的声音资料库。

因此，本轮新增资源分成两类。**审校器**（UNSLOP、no-ai-slop、humanizer-skill、Patina、unslop-text）用于找出模板化、解释化或重复模式；**声音资料库/工作流**（WRITING.md、EveryDay-Writer）用于在长期创作中吸收自己的修订偏好。前者不能替代后者。对中文散文、小说和具有作者声音的文章，应当先让审校器输出修改建议或对比稿，再由人决定是否采纳，而非直接覆盖原稿。

## 可复现性与失败记录

五份上游规则均按 [`upstream_commits.tsv`](upstream_commits.tsv) 所列提交从 GitHub 获取，规则快照的 SHA-256 见 [`skill_checksums.tsv`](skill_checksums.tsv)。第三方规则原文不随本仓库提交；这避免镜像他人内容，也让读者能够直接审阅上游最新许可与更新。

第一次统一生成在已完成 `UNSLOP` 与 `WRITING.md` 后，处理 46KB 的 Patina `SKILL.md` 时遇到代理 502。为避免混入不完整或靠截断规则得到的结果，Patina 没有进入排名；随后单独完成 `no-ai-slop` 与 `humanizer-skill`。失败脚本与恢复脚本均保留，便于他人改用更大上下文服务或其他模型重新测试。**未成功跑通不等于 Patina 效果差。**

## 参考资料

[1] [theclaymethod/unslop](https://github.com/theclaymethod/unslop)

[2] [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)

[3] [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill)

[4] [Anbeeld/WRITING.md](https://github.com/Anbeeld/WRITING.md)

[5] [devswha/patina](https://github.com/devswha/patina)

[6] [JCarterJohnson/vibecoded-design-tells 的 unslop-text](https://github.com/JCarterJohnson/vibecoded-design-tells/tree/main/unslop-ai-text)

[7] [Deupaxx/EveryDay-Writer](https://github.com/Deupaxx/EveryDay-Writer)

[8] [r/ClaudeCode：Humanizer 与替代写作规则讨论](https://www.reddit.com/r/ClaudeCode/comments/1sy4137/the_most_useful_claude_skill_i_ever_created/)

[9] [r/WritingWithAI：Deslopping Claude prose](https://www.reddit.com/r/WritingWithAI/comments/1uqkvla/deslopping_claude_prose/)

[10] [r/claudeskills：What’s the best humanizer skill out there?](https://www.reddit.com/r/claudeskills/comments/1v8wa5r/whats_the_best_humanizer_skill_out_there/)
