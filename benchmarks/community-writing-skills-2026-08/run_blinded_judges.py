import json
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
MODEL = "claude-opus-4-7"
SKILL_IDS = ["humanizer", "stop-slop", "avoid-ai-writing", "plain-writing", "humanize"]

source_md = (ROOT / "input.md").read_text(encoding="utf-8")
source_answer = source_md.split("## 待改写原文\n\n", 1)[1].strip()
question = json.loads((ROOT / "input_metadata.json").read_text(encoding="utf-8"))["question"]
client = OpenAI()

schema = {
    "type": "object",
    "properties": {
        "factual_fidelity": {"type": "integer", "minimum": 1, "maximum": 5},
        "coverage": {"type": "integer", "minimum": 1, "maximum": 5},
        "clarity": {"type": "integer", "minimum": 1, "maximum": 5},
        "naturalness": {"type": "integer", "minimum": 1, "maximum": 5},
        "reader_fit": {"type": "integer", "minimum": 1, "maximum": 5},
        "concision": {"type": "integer", "minimum": 1, "maximum": 5},
        "overall": {"type": "integer", "minimum": 1, "maximum": 5},
        "missing_or_weakened_points": {"type": "array", "items": {"type": "string"}},
        "unsupported_additions": {"type": "array", "items": {"type": "string"}},
        "rationale": {"type": "string"},
    },
    "required": [
        "factual_fidelity", "coverage", "clarity", "naturalness", "reader_fit",
        "concision", "overall", "missing_or_weakened_points", "unsupported_additions", "rationale",
    ],
    "additionalProperties": False,
}

system = """You are an independent, blinded evaluator for a writing-revision benchmark. You will receive one candidate revision without its originating tool name. Evaluate the candidate against the supplied source answer only. Do not reward any claim that is absent from the source, do not infer author identity, and do not treat fewer AI-like phrases as proof of quality. The reader asked for an explanation suitable for a curious non-expert. Use a strict 1–5 scale where 5 is excellent. Score factual fidelity by whether meaning is preserved and nothing unsupported is added; coverage by retention of the source's four distinct reasons and its cost caveat; clarity/naturalness/reader fit/concision by the actual candidate prose. Return JSON matching the schema."""

records = []
for index, skill_id in enumerate(SKILL_IDS, start=1):
    candidate = (ROOT / "outputs" / f"{skill_id}.md").read_text(encoding="utf-8").strip()
    candidate_id = f"candidate_{index}"
    user = f"""Original reader question:
{question}

Source answer:
{source_answer}

Blinded candidate revision ({candidate_id}):
{candidate}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_tokens=1600,
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "writing_skill_judgment", "strict": True, "schema": schema},
        },
    )
    judgment = json.loads(response.choices[0].message.content)
    usage = response.usage
    records.append({
        "candidate_id": candidate_id,
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
    "blinding": "The judge saw only candidate_1 through candidate_5. The mapping was retained by the runner and revealed only in this results file.",
    "rubric": {
        "factual_fidelity": "Meaning preserved and no unsupported additions.",
        "coverage": "Retains the four reasons and the cost caveat in the source answer.",
        "clarity": "Understandable organization and wording.",
        "naturalness": "Avoids mechanical or templated prose without mistaking stylistic difference for quality.",
        "reader_fit": "Suitable for a curious non-expert / ELI5 request.",
        "concision": "Removes needless repetition without losing material content.",
        "overall": "Holistic quality under the benchmark constraints.",
    },
    "records": records,
}
(ROOT / "blinded_judgments.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, indent=2))
