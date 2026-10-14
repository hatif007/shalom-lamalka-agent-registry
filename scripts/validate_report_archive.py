"""Validate archived reports without mistaking report text for a task transcript.

Only files actually in the Git history count as archived.
This script never reaches external services or executes agents.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "operations" / "management-system" / "reports" / "runs"
HEADER = re.compile(
    r"\A<!-- REPORT_ARCHIVE_V1\n(?P<metadata>\{[^\n]+\})\nREPORT_ARCHIVE_V1 -->\n(?P<body>.*)\Z",
    re.DOTALL,
)
ROLES = {"data", "seo", "website", "growth", "system"}
MODES = {
    "CHATGPT_SCHEDULED_TASK",
    "INSTALLED_AGENT_VERIFIED",
    "COORDINATOR",
    "TECHNICAL_SMOKE_TEST",
}
PAYLOADS = {"FULL_GENERATED_REPORT", "RECOVERED_EXCERPT", "SYNTHETIC_TEST"}
REQUIRED = {
    "schema_version",
    "report_id",
    "role",
    "run_date",
    "run_mode",
    "payload_type",
    "task_reference",
    "source_conversation_url",
    "source_evidence",
    "scope",
    "owner_approval",
}


def inspect(path):
    problems = []
    relative = path.relative_to(BASE)
    try:
        date_folder, role_folder, filename = relative.parts
        date.fromisoformat(date_folder)
    except (ValueError, TypeError):
        return [f"{relative}: expected YYYY-MM-DD/role/report-id.md"]
    except Exception:
        return [f"{relative}: expected exactly three path components"]

    raw = path.read_text(encoding="utf-8")
    match = HEADER.fullmatch(raw)
    if not match:
        return [f"{relative}: missing single-line JSON REPORT_ARCHIVE_V1 header"]
    try:
        meta = json.loads(match["metadata"])
    except (json.JSONDecodeError, ValueError) as exc:
        return [f"{relative}: invalid JSON metadata ({exc})"]

    for key in sorted(REQUIRED - set(meta)):
        problems.append(f"{relative}: missing metadata field {key}")

    name = meta.get("report_id")
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{4,100}", name):
        problems.append(f"{relative}: invalid report_id")
    elif filename != f"{name}.md":
        problems.append(f"{relative}: report_id does not match filename")

    if meta.get("schema_version") != "1.0":
        problems.append(f"{relative}: expected schema_version 1.0")
    if role_folder not in ROLES or meta.get("role") != role_folder:
        problems.append(f"{relative}: role and directory mismatch")
    if date_folder != meta.get("run_date"):
        problems.append(f"{relative}: run_date does not match folder")
    if meta.get("run_mode") not in MODES:
        problems.append(f"{relative}: unsupported run_mode")
    if meta.get("payload_type") not in PAYLOADS:
        problems.append(f"{relative}: unsupported payload_type")

    if meta.get("run_mode") == "INSTALLED_AGENT_VERIFIED" and not meta.get("runtime_run_id"):
        problems.append(f"{relative}: installed agent execution requires a verified runtime_run_id")

    if meta.get("payload_type") == "SYNTHETIC_TEST" and meta.get("run_mode") != "TECHNICAL_SMOKE_TEST":
        problems.append(f"{relative}: synthetic test must have TECHNICAL_SMOKE_TEST run_mode")
    if meta.get("run_mode") == "TECHNICAL_SMOKE_TEST" and meta.get("payload_type") != "SYNTHETIC_TEST":
        problems.append(f"{relative}: TECHNICAL_SMOKE_TEST must use SYNTHETIC_TEST")

    url = meta.get("source_conversation_url")
    if url is not None and (not isinstance(url, str) or not url.startswith("https://")):
        problems.append(f"{relative}: source_conversation_url must be null or HTTPS link")

    sources = meta.get("source_evidence")
    if not isinstance(sources, list) or not sources or any(
        not isinstance(s, str) or not s.startswith("https://") for s in sources
    ):
        problems.append(f"{relative}: source_evidence must contain at least one HTTPS link")

    for key in ("task_reference", "scope", "owner_approval"):
        if not isinstance(meta.get(key), str) or not meta[key].strip():
            problems.append(f"{relative}: {key} must be nonempty text")

    body = match["body"].strip()
    min_len = 40 if meta.get("payload_type") == "SYNTHETIC_TEST" else 200
    if len(body) < min_len:
        problems.append(f"{relative}: report body too short (<{min_len} chars)")
    if meta.get("payload_type") == "SYNTHETIC_TEST" and "SYNTHETIC" not in body.upper():
        problems.append(f"{relative}: test must be plainly labeled SYNTHETIC")
    if meta.get("payload_type") == "RECOVERED_EXCERPT" and "PARTIAL" not in body.upper():
        problems.append(f"{relative}: recovered excerpt must say PARTIAL")
    return problems


def main():
    paths = sorted(BASE.rglob("*.md"))
    failures = []
    for path in paths:
        relative = path.relative_to(BASE)
        if len(relative.parts) != 3:
            failures.append(f"{relative}: unexpected path depth")
            continue
        failures.extend(inspect(path))
    if failures:
        print("REPORT ARCHIVE VALIDATION: FAIL")
        for problem in failures:
            print("ERROR:", problem)
        sys.exit(1)
    print(f"REPORT ARCHIVE VALIDATION: PASS ({len(paths)} report(s); no agent execution claimed)")


if __name__ == "__main__":
    main()
