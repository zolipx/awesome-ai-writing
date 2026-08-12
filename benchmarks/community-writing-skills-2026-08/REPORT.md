# 社区写作 Skills 统一改写基准

> **基准时间：** 2026-08-12（GMT+8）
> **整理与执行：** Manus 1.6
> **结论范围：** 本报告只比较一个公开英文 ELI5 样本上的一次受控改写。它不是通用排行榜，也不用于证明检测规避能力。

## 摘要

这项微型基准测试对五个社区常用写作 Skills 使用了**同一公开 AI 生成文本、同一生成模型、同一事实保真约束和相同输出上限**。所有五个输出均通过了七项材料事实检查，且事实审计没有标出不受原文支持的新增主张。五个输出都比原文短 **30.4%–40.7%**。在独立盲评中，`Humanizer`、`avoid-ai-writing` 与 `humanize` 得到 5/5 的整体评分；`Stop Slop` 与 `plain-writing` 得到 4/5，盲评理由是其项目符号表达略显清单化，且对 ELI5 语气的适配较弱。

> **不应把这个结果理解为“某个 Skill 必然最好”。** 这里的输入很适合说明性改写，而且一次运行无法衡量跨模型稳定性、中文表现、长文编辑、特定作者声音保持或误删风险。

| 维度 | 固定设置 |
| --- | --- |
| 测试对象 | [Humanizer][2]、[Stop Slop][3]、[avoid-ai-writing][4]、[plain-writing-skill][5]、[humanize][6] |
| 基准输入 | HC3 `all/train/row_idx=12` 的公开 `chatgpt_answers[0]`，即关于电影布景与实景拍摄的英文 ELI5 回答。[1] |
| 生成模型 | `gpt-5`；五个候选均使用相同模型和 `max_completion_tokens=1400`。 |
| 生成约束 | 保留材料事实；不得加入事实、例子、统计、来源、建议或“规避检测”主张。 |
| 盲评模型 | `claude-opus-4-7`；评审只看到 `candidate_1` 至 `candidate_5`，映射在评审后才写入结果。 |
| 事实审计模型 | `gpt-5.5`，高推理设置；逐项审计七个从原文拆出的材料事实。 |

## 受控设计

原文、上游规则快照的提交定位、每个候选输出、模型调用记录和审计结果都保存在当前目录。`input.md` 记录了输入文本；`source_manifest.md` 说明数据集许可和选样依据；`upstream_commits.tsv` 固定五个上游规则的提交哈希；`generation_results.json` 记录生成模型、令牌用量与统一约束。

为避免把“文本更像人”误写成检测规避，本测试只评估以下内容：**材料事实保留、覆盖度、清晰度、自然度、非专业读者适配度与简洁性**。它不会调用检测器，也不输出任何绕过检测的提示或评分。

| 审计清单 | 原文中必须保留的材料点 |
| --- | --- |
| 1 | 布景让制作团队控制环境的外观与感觉。 |
| 2 | 此类控制对虚构世界或特定氛围尤其重要。 |
| 3 | 长期租赁实景可能昂贵。 |
| 4 | 使用或改造实景可能产生额外费用。 |
| 5 | 人群、噪声、干扰与基础资源不足会造成现场后勤问题。 |
| 6 | 交通、不稳定地面和恶劣天气会造成安全风险。 |
| 7 | 布景前期成本较高，但更强控制、较少延误和意外成本可能使其长期更划算。 |

## 结果

### 确定性文本指标

下表来自 `deterministic_metrics.json`。压缩率按空格分词后的词数计算；原文为 280 词。追溯信号仅检查候选中是否出现与七项材料点相对应的词汇或短语，**不是语义质量分**；语义判断由下方盲评与事实审计补充。

| Skill | 输出词数 | 相对压缩率 | 句数 | 项目符号行 | 七项追溯信号 |
| --- | ---: | ---: | ---: | ---: | ---: |
| [Humanizer][2] | 176 | 37.1% | 11 | 4 | 7/7 |
| [Stop Slop][3] | 169 | 39.6% | 11 | 4 | 7/7 |
| [avoid-ai-writing][4] | 167 | 40.4% | 11 | 4 | 7/7 |
| [plain-writing-skill][5] | 195 | 30.4% | 17 | 4 | 7/7 |
| [humanize][6] | 166 | 40.7% | 12 | 0 | 7/7 |

### 盲评与事实保真

独立盲评以 1–5 分评价事实保真、覆盖度、清晰度、自然度、读者适配度与简洁性。由于评审服务对其中一个候选没有返回 `naturalness` 字段，表格将该项标为“未返回”，而不是擅自补分。完整原始结果见 [`blinded_judgments.json`](blinded_judgments.json)；七项事实审计与逐条证据见 [`fact_audit.json`](fact_audit.json)。

| Skill | 事实保真 | 覆盖度 | 清晰度 | 自然度 | ELI5 适配 | 简洁性 | 整体 | 盲评关键观察 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Humanizer | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 保留四类原因与成本限定；用语简单。 |
| Stop Slop | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 内容完整，但“shaky ground”等表达与项目符号形式略显清单化。 |
| avoid-ai-writing | 5 | 5 | 5 | 未返回 | 5 | 5 | 5 | 保留四类原因和成本限定；短句、清晰项目符号。 |
| plain-writing-skill | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 清晰且保真；但盲评认为其较机械化，较少 ELI5 对话感。 |
| humanize | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 保真、简洁且节奏较口语化；唯一一个没有使用项目符号的候选。 |

事实审计将每个输出的七个材料点均标为 `present`，并未发现材料性新增。审计证据会再用候选原文做直接子串核对；除 Humanizer 的一个多引号分隔符格式问题外，其余核对均为 7/7。这个格式差异不会改变语义审计结论，但说明模型评审的“证据格式”也应被审查，不能只接受自动评分。

### 输出风格的可观察差异

`Humanizer`、`Stop Slop`、`avoid-ai-writing` 与 `plain-writing-skill` 都保留了四项目符号结构，主要优化是缩短句子、去掉开场套话和压缩重复解释。`humanize` 改成了短段落，因此在这个 ELI5 样本里呈现出更连续的口语节奏。这个差异描述的是**本次输出**，而不是这些项目在所有场景下的固定行为。

| 适合优先尝试的目标 | 本次样本中较匹配的候选 | 原因与限定 |
| --- | --- | --- |
| 在保留原有解释框架的同时缩短文字 | `avoid-ai-writing`、`Stop Slop` | 都压缩约 40%，并保留四个显式原因；`Stop Slop` 的语气在本次盲评中略偏清单化。 |
| 追求直接、简洁的编辑结果 | `plain-writing-skill` | 压缩最少，但显性保留信息最多；代价是本次样本中口语感较弱。 |
| 希望从列表改成简短叙述段落 | `humanize` | 不使用项目符号，压缩率最高；应另以中文和长文样本验证是否稳定。 |
| 希望使用社区中安装/分发较广的通用上游规则 | `Humanizer`、`Stop Slop` | 本次均保持事实和覆盖；实际选择还要看语言、Agent 容器和团队写作规范。 |

## 局限与下一步

这个基准只含**一个英文、说明性、短篇 ELI5 输出**；上游规则和生成模型也都可能随版本变化。一次运行不支持统计显著性结论，也不应外推到中文公文、中文小说、学术写作、营销文案、长文编辑或特定个人文风。

后续扩展应至少采用多个公开样本，按体裁与语言分层；固定每个上游 Skill 的提交哈希；多次重复运行；由不同模型和人工评审共同复核；同时单列“遗漏材料点”“无根据新增”“格式退化”和“作者声音损失”。对于中文写作，应另建具有明确许可与来源的中文样本集，而不是将英文结果直接迁移。

## 复现说明

1. 先运行 `extract_hc3_sample.py` 固定公开 HC3 输入。
2. 运行 `bash fetch_upstream_skills.sh`，按 [`upstream_commits.tsv`](upstream_commits.tsv) 中固定的提交哈希从各上游仓库拉取对应 `SKILL.md` 快照到 `skills/`（该目录不随本基准分支提交，以避免镜像第三方规则文件）。
3. 运行 `run_generation_benchmark.py`、`run_blinded_judges.py`、`run_fact_audit.py` 和 `analyze_outputs.py`。
4. 比较生成的 JSON、输出文本与本报告中的表格。模型目录应在运行前重新获取；本次实测模型配置见 [`generation_results.json`](generation_results.json)、[`blinded_judgments.json`](blinded_judgments.json) 与 [`fact_audit.json`](fact_audit.json)。

## 参考资料

[1] [Hello-SimpleAI/HC3 数据集卡（CC BY-SA 4.0）](https://huggingface.co/datasets/Hello-SimpleAI/HC3)

[2] [blader/humanizer](https://github.com/blader/humanizer)

[3] [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

[4] [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)

[5] [docwriter-org/plain-writing-skill](https://github.com/docwriter-org/plain-writing-skill)

[6] [harshaneel/humanize](https://github.com/harshaneel/humanize)
