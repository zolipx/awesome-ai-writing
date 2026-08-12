import json
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
MODEL = "gpt-5.5"
SKILL_IDS = ["unslop", "writing-md", "no-ai-slop", "humanizer-skill"]
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
                    "rank": {"type": "integer", "minimum": 1, "maximum": 4},
                    "style_preservation_score": {"type": "integer", "minimum": 0, "maximum": 100},
                    "strength": {"type": "string"},
                    "material_loss_or_drift": {"type": "string"},
                    "quoted_evidence": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["candidate_id", "rank", "style_preservation_score", "strength", "material_loss_or_drift", "quoted_evidence"],
                "additionalProperties": False,
            },
            "minItems": 4,
            "maxItems": 4,
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

system = """你是一位严格的中文散文编辑，做盲态横向风格保持评审。原文是一篇克制亲情散文；候选是对同一原文的改写。你必须给四个候选唯一排名，不得并列。评分评价相对原文的风格保持，而非通顺度或“是否像某位现实作者”。重点审查：第一人称回忆与时序；具体物件和雨地意象；未说出口的情感；自然的中文搭配；不把具象比喻压扁成解释；不添加原文没有的动作、动机或心理诊断。即使候选保留六项材料点，也必须因说明化、删去开场、刻意口语、句法过度整理或不自然搭配扣分。每个候选至少引用一个原文片段证据。只输出严格匹配 JSON Schema 的 JSON。"""
user = f"""## 原文

{source}

## 匿名候选

{candidates}
"""
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
    max_completion_tokens=2500,
    extra_body={"reasoning": {"effort": "high"}},
    response_format={"type": "json_schema", "json_schema": {"name": "community_candidate_style_review", "strict": True, "schema": schema}},
)
review = json.loads(response.choices[0].message.content)
usage = response.usage
result = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "review_model": MODEL,
    "blinding": "The reviewer saw candidate_1 through candidate_4 only; mappings were revealed after review.",
    "candidate_mapping_revealed_after_review": {f"candidate_{i}": skill_id for i, skill_id in enumerate(SKILL_IDS, start=1)},
    "review": review,
    "usage": {"prompt_tokens": getattr(usage, "prompt_tokens", None), "completion_tokens": getattr(usage, "completion_tokens", None), "total_tokens": getattr(usage, "total_tokens", None)},
}
(ROOT / "comparative_style_review.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
