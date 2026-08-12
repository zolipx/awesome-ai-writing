import json
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
MODEL = "gpt-5.5"
SKILL_IDS = ["humanizer", "stop-slop", "avoid-ai-writing", "plain-writing", "humanize"]
source = (ROOT / "input.md").read_text(encoding="utf-8").split("## 小站\n\n", 1)[1].strip()
rubric = (ROOT / "rubric.md").read_text(encoding="utf-8")
client = OpenAI()

schema = {
    "type": "object",
    "properties": {
        "narrative_viewpoint_and_time": {"type": "integer", "minimum": 1, "maximum": 5},
        "restrained_affection": {"type": "integer", "minimum": 1, "maximum": 5},
        "concrete_imagery": {"type": "integer", "minimum": 1, "maximum": 5},
        "sentence_rhythm": {"type": "integer", "minimum": 1, "maximum": 5},
        "chinese_naturalness": {"type": "integer", "minimum": 1, "maximum": 5},
        "detail_fidelity": {"type": "integer", "minimum": 1, "maximum": 5},
        "overall_style_preservation": {"type": "integer", "minimum": 1, "maximum": 5},
        "drift_tags": {"type": "array", "items": {"type": "string"}},
        "strongest_preserved_feature": {"type": "string"},
        "most_material_style_or_detail_loss": {"type": "string"},
        "evidence": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "narrative_viewpoint_and_time", "restrained_affection", "concrete_imagery",
        "sentence_rhythm", "chinese_naturalness", "detail_fidelity", "overall_style_preservation",
        "drift_tags", "strongest_preserved_feature", "most_material_style_or_detail_loss", "evidence",
    ],
    "additionalProperties": False,
}

system = """你是一位独立、盲态的中文散文编辑。你将看到原创原文、评审量表和一个不知道来源的候选改写。请只评估候选相对原文的风格保持与漂移，而不是把文字是否“像某位现实作者”当作指标。严格按 1–5 分评审：5 表示几乎完整保持，3 表示部分保持但有明确漂移或弱化，1 表示严重改变。重点核对第一人称回忆、克制亲情、具体意象、句法节奏、中文自然度和六项材料细节。若候选删去开篇场景或关键物件，即使其余文字流畅，也应明显降低具体意象和细节保真。候选身份对你不可见。只输出符合 JSON Schema 的 JSON。"""

records = []
for index, skill_id in enumerate(SKILL_IDS, start=1):
    candidate = (ROOT / "outputs" / f"{skill_id}.md").read_text(encoding="utf-8").strip()
    user = f"""## 原创原文

{source}

## 评审量表

{rubric}

## 候选 {index}

{candidate}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_completion_tokens=2200,
        extra_body={"reasoning": {"effort": "high"}},
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "zh_style_judgment", "strict": True, "schema": schema},
        },
    )
    judgment = json.loads(response.choices[0].message.content)
    usage = response.usage
    records.append({
        "candidate_id": f"candidate_{index}",
        "skill_id_mapping_revealed_after_judgment": skill_id,
        "judgment": judgment,
        "finish_reason": response.choices[0].finish_reason,
        "prompt_tokens": getattr(usage, "prompt_tokens", None),
        "completion_tokens": getattr(usage, "completion_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
    })

result = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "judge_model": MODEL,
    "blinding": "The judge saw candidate_1 through candidate_5 only. Skill mappings were retained by the runner and exposed only in this result file.",
    "note": "The original Claude structured-output attempt returned invalid JSON from the proxy, so this rerun uses gpt-5.5 with strict JSON-schema output and high reasoning.",
    "records": records,
}
(ROOT / "blinded_style_judgments.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
