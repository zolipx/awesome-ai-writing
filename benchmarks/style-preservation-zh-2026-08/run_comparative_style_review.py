import json
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
MODEL = "gpt-5.5"
SKILL_IDS = ["humanizer", "stop-slop", "avoid-ai-writing", "plain-writing", "humanize"]
source = (ROOT / "input.md").read_text(encoding="utf-8").split("## 小站\n\n", 1)[1].strip()
client = OpenAI()

schema = {
    "type": "object",
    "properties": {
        "ranked_results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "candidate_id": {"type": "string"},
                    "rank": {"type": "integer", "minimum": 1, "maximum": 5},
                    "style_preservation_score": {"type": "integer", "minimum": 0, "maximum": 100},
                    "style_strength": {"type": "string"},
                    "specific_drift_or_loss": {"type": "string"},
                    "quoted_evidence": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["candidate_id", "rank", "style_preservation_score", "style_strength", "specific_drift_or_loss", "quoted_evidence"],
                "additionalProperties": False,
            },
            "minItems": 5,
            "maxItems": 5,
        },
        "overall_observation": {"type": "string"},
    },
    "required": ["ranked_results", "overall_observation"],
    "additionalProperties": False,
}

candidates = "\n\n".join(
    f"## candidate_{i}\n{(ROOT / 'outputs' / f'{skill_id}.md').read_text(encoding='utf-8').strip()}"
    for i, skill_id in enumerate(SKILL_IDS, start=1)
)

system = """你是一位严格的中文散文编辑，正在做盲态的比较性风格审读。对五个候选进行唯一排名，不能并列。评分是相对原文的风格保持分，而不是通顺度分：100 只给几乎不改变原文叙述功能、节奏、物件意象、克制和中文搭配的文本。必须严查以下细微问题：把具象比喻改成说明句；把叙述压缩成过于平直的句法；把动作的含蓄改成解释；不自然的搭配、标点或现代口语；改变叙述者和事件的位置。即使六个材料点都存在，也应因这些风格变化扣分。每个候选必须引用至少一个候选中的短语作为证据。你不知道各候选来源。只输出符合 JSON Schema 的 JSON。"""

user = f"""## 原文

{source}

## 候选

{candidates}
"""
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
    max_completion_tokens=2800,
    extra_body={"reasoning": {"effort": "high"}},
    response_format={"type": "json_schema", "json_schema": {"name": "comparative_style_review", "strict": True, "schema": schema}},
)
review = json.loads(response.choices[0].message.content)
usage = response.usage
result = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "review_model": MODEL,
    "blinding": "The reviewer saw candidate_1 through candidate_5 only; mapping is revealed below after the review.",
    "candidate_mapping_revealed_after_review": {f"candidate_{i}": skill_id for i, skill_id in enumerate(SKILL_IDS, start=1)},
    "review": review,
    "usage": {"prompt_tokens": getattr(usage, "prompt_tokens", None), "completion_tokens": getattr(usage, "completion_tokens", None), "total_tokens": getattr(usage, "total_tokens", None)},
}
(ROOT / "comparative_style_review.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
