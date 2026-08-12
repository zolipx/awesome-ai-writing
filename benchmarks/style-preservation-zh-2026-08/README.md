# 中文散文风格保持基准

本目录测试的是：社区写作 Skills 对一篇**原创中文克制亲情散文**进行改写时，是否保住叙述视角、物件意象、情感节制、中文节奏和材料细节。它不是压缩率测试，也不测试检测规避。

| 文件或目录 | 内容 |
| --- | --- |
| [REPORT.md](REPORT.md) | 完整方法、横向盲态排名、候选证据、结论与局限。 |
| [input.md](input.md) | Manus 1.6 原创测试短文《小站》。 |
| [rubric.md](rubric.md) | 六项材料细节、六个风格维度与漂移标签。 |
| [outputs/](outputs/) | 五个 Skill 在相同条件下生成的完整中文候选。 |
| [generation_results.json](generation_results.json) | 生成模型、统一约束、令牌记录和输出映射。 |
| [blinded_style_judgments.json](blinded_style_judgments.json) | 逐个匿名候选的盲态量表评分。 |
| [comparative_style_review.json](comparative_style_review.json) | 强制唯一排序的横向盲态比较与文本证据。 |
| [upstream_commits.tsv](upstream_commits.tsv) | 五个上游 Skill 的固定提交哈希。 |
| [skill_checksums.tsv](skill_checksums.tsv) | 本次运行规则快照的 SHA-256 校验和。 |
| [fetch_upstream_skills.sh](fetch_upstream_skills.sh) | 拉取固定版本 `SKILL.md` 的脚本。 |
| `run_*.py` | 统一生成、单项盲评和横向盲评的复现脚本。 |

`skills/` 是从第三方仓库拉取的运行时快照，未提交到本仓库。复现时先运行 `bash fetch_upstream_skills.sh`，再对照 `skill_checksums.tsv` 核验规则文件。
