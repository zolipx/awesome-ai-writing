# 社区写作 Skills 基准材料

本目录保存 `REPORT.md` 所述的可复核材料。该测试比较五个上游写作 Skills 对同一公开 HC3 英文回答的改写效果；它不是通用排行榜，也不测试任何检测规避能力。

| 文件或目录 | 内容 |
| --- | --- |
| [REPORT.md](REPORT.md) | 方法、结果、局限与引用。 |
| [input.md](input.md) | 固定的公开基准输入。 |
| [source_manifest.md](source_manifest.md) | 数据来源、许可、选样原则与可复核定位。 |
| [outputs/](outputs/) | 五个统一条件下的改写结果。 |
| [generation_results.json](generation_results.json) | 生成模型、统一约束、令牌记录和输出映射。 |
| [blinded_judgments.json](blinded_judgments.json) | 独立盲评的原始记录。 |
| [fact_audit.json](fact_audit.json) | 七项材料事实的逐项审计与引用证据。 |
| [deterministic_metrics.json](deterministic_metrics.json) | 词数、压缩率、结构与证据核对。 |
| `*.py` | 提取输入、执行改写、执行评审和生成指标的复现脚本。 |
| [upstream_commits.tsv](upstream_commits.tsv) | 五个上游规则文件的固定提交哈希。 |
| [fetch_upstream_skills.sh](fetch_upstream_skills.sh) | 按固定提交哈希获取运行时 `SKILL.md` 快照的脚本。 |
| [skill_checksums.tsv](skill_checksums.tsv) | 本次运行所用规则快照的 SHA-256 校验和。 |

`skills/` 仅作为本地运行时快照使用，已在提交前排除，避免镜像第三方项目的规则文件。复现时请运行 `bash fetch_upstream_skills.sh`，它会按 `upstream_commits.tsv` 中的固定提交哈希直接获取对应 `SKILL.md`；随后可使用 `skill_checksums.tsv` 验证快照未发生变化。
