# 社区小众写作 Skills：中文复核材料

本目录保存“社区讨论与实际效果”双重筛选的可复核材料。它把社区采用证据与同一篇原创中文散文的风格保持测试分开记录；**Star 数、作者宣传或单次模型评审都不单独构成效果保证。**

| 文件或目录 | 内容 |
| --- | --- |
| [REPORT.md](REPORT.md) | 候选分层、社区证据、统一测试、横向排名、失败记录与限制。 |
| [input.md](input.md) | 与前次测试相同的原创中文基准短文。 |
| [rubric.md](rubric.md) | 六项材料细节与中文散文风格保持量表。 |
| [outputs/](outputs/) | 四个成功运行候选的完整改写文本。 |
| [generation_results.json](generation_results.json) | 前两项候选的统一生成记录。 |
| [pending_generation_results.json](pending_generation_results.json) | 502 恢复后两项候选的生成记录。 |
| [comparative_style_review.json](comparative_style_review.json) | 匿名横向比较、排名、分数与引用证据。 |
| [upstream_commits.tsv](upstream_commits.tsv) | 五个候选的固定上游提交。 |
| [skill_checksums.tsv](skill_checksums.tsv) | 本地获取规则快照的 SHA-256 校验和。 |
| `run_*.py` | 生成、恢复与盲态横向评审的复现脚本。 |

`skills/` 中的第三方规则快照没有提交。读者应按照 `upstream_commits.tsv` 直接审阅并获取原始规则，再运行脚本。Patina 在本轮完整规则请求中遇到上游 502，因此不在输出和排序中；这是一条如实保留的运行限制，不代表其质量结论。
