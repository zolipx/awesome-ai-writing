import json
from pathlib import Path

root = Path(__file__).resolve().parent
raw = json.loads((root / "hc3_row_12.json").read_text(encoding="utf-8"))
row = raw["rows"][0]["row"]
question = row["question"]
answer = row["chatgpt_answers"][0]
source = row["source"]

sample = f"""# 基准输入

- **数据集：** HC3（Hello-SimpleAI/HC3）
- **配置：** `all` / `train` / `row_idx=12`
- **来源类别：** `{source}`
- **问题：** {question}
- **输入字段：** `chatgpt_answers[0]`

## 待改写原文

{answer}
"""
(root / "input.md").write_text(sample, encoding="utf-8")

metadata = {
    "dataset": "Hello-SimpleAI/HC3",
    "config": "all",
    "split": "train",
    "row_idx": 12,
    "source": source,
    "question": question,
    "source_field": "chatgpt_answers[0]",
    "char_count": len(answer),
    "word_count_space_delimited": len(answer.split()),
}
(root / "input_metadata.json").write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(metadata, ensure_ascii=False, indent=2))
