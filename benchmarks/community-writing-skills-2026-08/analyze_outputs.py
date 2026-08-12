import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_IDS = ["humanizer", "stop-slop", "avoid-ai-writing", "plain-writing", "humanize"]
source_md = (ROOT / "input.md").read_text(encoding="utf-8")
source = source_md.split("## 待改写原文\n\n", 1)[1].strip()

TRACEABILITY_RULES = {
    "visual_control": r"\b(look|looks|feel|feels|mood|atmosphere)\b",
    "fiction_or_mood_context": r"\b(made-up|fictional|fantastical|specific mood|specific feeling)\b",
    "long_rental_cost": r"\b(rent|renting|rented).{0,100}\b(long|extended)\b|\b(long|extended).{0,100}\b(rent|renting|rented)\b",
    "location_use_or_alteration_cost": r"\bpay\b.{0,120}\b(use|change|alter|fit)\b",
    "logistics": r"\b(crowds?|noise|distractions?|electricity|water|equipment|gear)\b",
    "safety": r"\b(traffic|ground|terrain|weather)\b",
    "long_term_cost_caveat": r"\b(upfront|at the start|at first)\b.{0,300}\b(delay|surprise|unexpected|long run|long-run|over time)\b|\b(delay|surprise|unexpected|long run|long-run|over time)\b.{0,300}\b(upfront|at the start|at first)\b",
}


def words(text):
    return re.findall(r"[A-Za-z]+(?:['’-][A-Za-z]+)?", text)


def sentence_count(text):
    chunks = [x.strip() for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x.strip()]
    return len(chunks)


def direct_evidence_supported(evidence, candidate):
    evidence = evidence.strip().strip('"')
    if not evidence or evidence.lower() == "none":
        return evidence.lower() == "none"
    parts = [p.strip().strip('"') for p in evidence.split(";")]
    return all(part.lower() in candidate.lower() for part in parts if part)

source_word_count = len(words(source))
records = []
for skill_id in SKILL_IDS:
    candidate = (ROOT / "outputs" / f"{skill_id}.md").read_text(encoding="utf-8").strip()
    candidate_word_count = len(words(candidate))
    traceability = {
        name: bool(re.search(pattern, candidate, flags=re.IGNORECASE | re.DOTALL))
        for name, pattern in TRACEABILITY_RULES.items()
    }
    records.append({
        "skill_id": skill_id,
        "characters": len(candidate),
        "word_count": candidate_word_count,
        "word_reduction_vs_source_percent": round((1 - candidate_word_count / source_word_count) * 100, 1),
        "sentence_count": sentence_count(candidate),
        "bullet_line_count": sum(1 for line in candidate.splitlines() if line.strip().startswith(("-", "*"))),
        "traceability_flags": traceability,
        "traceability_flag_count": sum(traceability.values()),
    })

fact_audit = json.loads((ROOT / "fact_audit.json").read_text(encoding="utf-8"))
audit_qa = []
for record in fact_audit["records"]:
    skill_id = record["skill_id_mapping_revealed_after_audit"]
    candidate = (ROOT / "outputs" / f"{skill_id}.md").read_text(encoding="utf-8").strip()
    item_checks = []
    for item in record["audit"]["items"]:
        item_checks.append({
            "criterion_index": item["criterion_index"],
            "status": item["status"],
            "evidence": item["evidence"],
            "evidence_is_direct_substring": direct_evidence_supported(item["evidence"], candidate),
        })
    audit_qa.append({
        "skill_id": skill_id,
        "direct_evidence_checks": item_checks,
        "direct_evidence_pass_count": sum(x["evidence_is_direct_substring"] for x in item_checks),
        "total_items": len(item_checks),
    })

result = {
    "source_word_count": source_word_count,
    "output_metrics": records,
    "traceability_rules": TRACEABILITY_RULES,
    "fact_audit_evidence_qa": audit_qa,
    "interpretation": "Traceability flags are lexical evidence checks, not semantic scores. A false flag does not prove a missing idea; it triggers manual review. Direct-evidence QA checks whether a model auditor quoted text that actually exists in the candidate.",
}
(ROOT / "deterministic_metrics.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
