import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None

source_files = sorted((ROOT / "data-sources").glob("*.json"))
registry_files = sorted((ROOT / "registries").glob("*.json"))
if len(source_files) != 4:
    errors.append(f"Expected 4 data-source JSON files; found {len(source_files)}")
if len(registry_files) != 5:
    errors.append(f"Expected 5 registry JSON files; found {len(registry_files)}")

source_required = {
    "source_id", "status", "system", "account_owner", "authorization_status",
    "access_mode", "available_data_types", "queried_date_range",
    "freshness_status", "processing_delay", "validation_evidence",
    "slack_link", "limitations"
}
for path in source_files:
    obj = load_json(path)
    if not isinstance(obj, dict):
        errors.append(f"{path.relative_to(ROOT)}: expected JSON object")
        continue
    missing = sorted(source_required - obj.keys())
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing keys: {', '.join(missing)}")

matrix_path = ROOT / "registries" / "access-matrix.json"
matrix = load_json(matrix_path)
matrix_required = {
    "agent", "source", "permitted_purpose", "access_mode", "permitted_data_fields",
    "prohibited_data_actions", "connection_authorization_status", "last_verified_date",
    "test_result", "evidence_link", "known_limitations"
}
if not isinstance(matrix, list):
    errors.append("registries/access-matrix.json: expected JSON array")
else:
    if len(matrix) != 20:
        errors.append(f"Expected 20 agent/source pairings; found {len(matrix)}")
    for i, row in enumerate(matrix, 1):
        if not isinstance(row, dict):
            errors.append(f"access matrix row {i}: expected object")
            continue
        missing = sorted(matrix_required - row.keys())
        if missing:
            errors.append(f"access matrix row {i}: missing keys: {', '.join(missing)}")
    pairs = [(r.get("agent"), r.get("source")) for r in matrix if isinstance(r, dict)]
    if len(pairs) != len(set(pairs)):
        errors.append("access matrix contains duplicate agent/source pairings")

tests = load_json(ROOT / "registries" / "tests.json")
test_required = {"id", "operator", "status", "purpose", "source", "date_range", "sample_size", "steps_performed", "result", "limitations", "changes_made", "slack_report"}
if not isinstance(tests, list):
    errors.append("registries/tests.json: expected JSON array")
else:
    for row in tests:
        if not isinstance(row, dict):
            errors.append("tests.json contains a non-object record")
            continue
        missing = sorted(test_required - row.keys())
        if missing:
            errors.append(f"test {row.get('id', 'UNKNOWN')}: missing keys: {', '.join(missing)}")

findings = load_json(ROOT / "registries" / "findings.json")
finding_required = {"id", "classification", "statement", "source", "source_type", "date_range", "extracted_at", "freshness", "metric_definition", "confidence", "confidence_rationale", "limitations", "alternative_explanations", "business_impact", "next_step", "owner", "status", "slack_link"}
if not isinstance(findings, list):
    errors.append("registries/findings.json: expected JSON array")
else:
    allowed = {"FACT", "HYPOTHESIS", "RECOMMENDATION", "UNKNOWN"}
    for row in findings:
        if not isinstance(row, dict):
            errors.append("findings.json contains a non-object record")
            continue
        missing = sorted(finding_required - row.keys())
        if missing:
            errors.append(f"finding {row.get('id', 'UNKNOWN')}: missing keys: {', '.join(missing)}")
        if row.get("classification") not in allowed:
            errors.append(f"finding {row.get('id', 'UNKNOWN')}: invalid classification")

ga4_path = ROOT / "data-sources" / "ga4.json"
ga4 = load_json(ga4_path)
if isinstance(ga4, dict):
    if ga4.get("status") != "PARTIAL_UNRESOLVED":
        errors.append("GA4 must remain PARTIAL_UNRESOLVED until evidence supports a status change")
    if ga4.get("investigation_status") != "DEFERRED_LOW_TRAFFIC":
        errors.append("GA4 investigation_status must reflect the owner's low-traffic deferral")

if errors:
    print("REGISTRY VALIDATION: FAIL")
    for item in errors:
        print(f"ERROR: {item}")
    sys.exit(1)

print("REGISTRY VALIDATION: PASS")
print(f"Validated {len(source_files)} source files, {len(registry_files)} registry files, {len(matrix)} access pairings, {len(tests)} tests, and {len(findings)} findings.")
print("Note: this checks JSON/schema consistency only; it does not validate live integrations or agent behavior.")
