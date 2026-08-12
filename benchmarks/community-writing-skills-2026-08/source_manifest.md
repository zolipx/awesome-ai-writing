# 基准来源清单

| 字段 | 内容 |
| --- | --- |
| 数据集 | [HC3: A Human-ChatGPT Comparison Corpus](https://huggingface.co/datasets/Hello-SimpleAI/HC3) |
| 许可证 | CC BY-SA 4.0 |
| 使用目的 | 从数据集中选取一条公开的 ChatGPT 生成回答，作为所有 Skill 共用的同一改写输入；不使用自行生成或随机模拟的测试文本。 |
| 可用语言 | 英文、中文 |
| 数据集规模 | 数据卡显示 all 子集约 24.3k 行，包含 question、human_answers、chatgpt_answers、source 等字段。 |
| 选样原则 | 选择一条非敏感、英文、说明性回答，且其文本呈现社区 Skills 旨在处理的模式，例如泛化开头、固定编号结构与冗余解释。 |
| 数据卡核验时间 | 2026-08-12（GMT+8） |

该数据集用于比较改写行为与可读性指标，不用作“是否 AI 生成”或“是否规避检测”的证明。
