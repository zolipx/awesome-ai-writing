import json
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
MODEL = "gpt-5.5"
SKILL_IDS = ["humanizer", "stop-slop", "avoid-ai-writing", "plain-writing", "humanize"]
source_md = (ROOT / "input.md").read_text(encoding="utf-8")
source_answer = source_md.split("## 待改写原文\n\n", 1)[1].strip()
client = OpenAI()

checklist = [
    "Creative control over the look and feel of the environment.",
    "Creative control matters for a fantastical or fictional world, or a specific mood or atmosphere.",
    "A real location can be costly, especially when rented for a long period.",
    "Real locations can require extra payment to use or alter them for the production.",
    "Real locations create logistical problems such as crowds, noise, distractions, or missing utilities/equipment.",
    "Real locations create safety risks such as traffic, unstable terrain, or bad weather.",
    "Sets can cost more upfront but can be more cost-effective over time through control and fewer delays or unexpected costs.",
]

schema = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "criterion_index": {"type": "integer", "minimum": 1, "maximum": 7},
                    "status": {"type": "string", "enum": ["present", "partial", "absent"]},
                    "evidence": {"type": "string"},
                },
                "required": ["criterion_index", "status", "evidence"],
                "additionalProperties": False,
            },
            "minItems": 7,
            "maxItems": 7,
        },
        "unsupported_additions": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
    },
    "required": ["items", "unsupported_additions", "summary"],
    "additionalProperties": False,
}

system = """You are a strict blinded fact-preservation auditor. You will receive the source answer, a fixed seven-item checklist of material claims drawn from that source, and one candidate revision. Do not infer content that is not stated. Mark a checklist item 'present' only if its whole proposition is conveyed; mark it 'partial' if only a weaker or incomplete version appears; mark it 'absent' if it does not appear. For each item, provide a short exact quote or 'none' as evidence. Identify unsupported additions only when the candidate states a material claim not supported by the source. Return JSON matching the schema exactly."""

records = []
for index, skill_id in enumerate(SKILL_IDS, start=1):
    candidate = (ROOT / "outputs" / f"{skill_id}.md").read_text(encoding="utf-8").strip()
    checklist_text = "\n".join(f"{i}. {item}" for i, item in enumerate(checklist, start=1))
    user = f"""Source answer:
{source_answer}

Checklist:
{checklist_text}

Candidate {index}:
{candidate}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_completion_tokens=1800,
        extra_body={"reasoning": {"effort": "high"}},
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "fact_audit", "strict": True, "schema": schema},
        },
    )
    audit = json.loads(response.choices[0].message.content)
    usage = response.usage
    records.append({
        "candidate_id": f"candidate_{index}",
        "skill_id_mapping_revealed_after_audit": skill_id,
        "audit": audit,
        "finish_reason": response.choices[0].finish_reason,
        "prompt_tokens": getattr(usage, "prompt_tokens", None),
        "completion_tokens": getattr(usage, "completion_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
    })

result = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "audit_model": MODEL,
    "blinding": "The auditor saw candidate numbers only; mapping was revealed only after each audit was saved.",
    "checklist": checklist,
    "records": records,
}
(ROOT / "fact_audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
