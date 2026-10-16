#!/usr/bin/env python3
"""Copy exact bytes from allowlisted inbox branches to canonical report archive."""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import date
from pathlib import Path

ROLES = {"data", "seo", "website", "growth"}
MODES = {"CHATGPT_SCHEDULED_TASK", "INSTALLED_AGENT_VERIFIED", "COORDINATOR", "TECHNICAL_SMOKE_TEST"}
PAYLOADS = {"FULL_GENERATED_REPORT", "RECOVERED_EXCERPT", "SYNTHETIC_TEST"}
REQUIRED = {"schema_version", "report_id", "role", "run_date", "run_mode",
            "payload_type", "task_reference", "source_conversation_url",
            "source_evidence", "scope", "owner_approval"}
HEADER = re.compile(r"\A<!-- REPORT_ARCHIVE_V1\n(?P<meta>\{[^\n]+\})\nREPORT_ARCHIVE_V1 -->\n(?P<body>.*)\Z", re.S)
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{4,100}\Z")


def paths(role, day, report_id):
    if role not in ROLES or not SAFE_ID.fullmatch(report_id):
        raise ValueError("Invalid role or report_id")
    if date.fromisoformat(day).isoformat() != day:
        raise ValueError("Invalid date")
    suffix = f"{day}/{role}/{report_id}.md"
    return f"reports/runs/{suffix}", Path("operations/management-system/reports/runs") / suffix


def validate(data, role, day, report_id):
    try:
        raw = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ValueError("Report must be UTF-8") from e
    m = HEADER.fullmatch(raw)
    if m is None:
        raise ValueError("REPORT_ARCHIVE_V1 header missing or malformed")
    meta = json.loads(m["meta"])
    if not REQUIRED.issubset(meta):
        raise ValueError(f"Missing metadata: {sorted(REQUIRED - set(meta))}")
    if tuple(meta[k] for k in ("schema_version", "role", "run_date", "report_id")) != ("1.0", role, day, report_id):
        raise ValueError("Metadata/path mismatch")
    if meta["run_mode"] not in MODES or meta["payload_type"] not in PAYLOADS:
        raise ValueError("Unsupported mode or payload type")
    synthetic = meta["payload_type"] == "SYNTHETIC_TEST"
    if synthetic != (meta["run_mode"] == "TECHNICAL_SMOKE_TEST"):
        raise ValueError("Synthetic tests require TECHNICAL_SMOKE_TEST (and vice versa)")
    if meta["run_mode"] == "INSTALLED_AGENT_VERIFIED" and not meta.get("runtime_run_id"):
        raise ValueError("Missing verified runtime_run_id")
    if meta["source_conversation_url"] is not None and not str(meta["source_conversation_url"]).startswith("https://"):
        raise ValueError("Invalid conversation URL")
    sources = meta["source_evidence"]
    if not isinstance(sources, list) or not sources or any(not isinstance(s, str) or not s.startswith("https://") for s in sources):
        raise ValueError("Missing HTTPS source evidence")
    if any(not isinstance(meta[k], str) or not meta[k].strip() for k in ("task_reference", "scope", "owner_approval")):
        raise ValueError("Missing provenance text")
    body = m["body"].strip()
    if len(body) < (40 if synthetic else 200):
        raise ValueError("Report body too short")
    if synthetic and "SYNTHETIC" not in body.upper():
        raise ValueError("Synthetic test not marked SYNTHETIC")
    return meta


def promote(role, day, report_id, data, root, dry_run=False):
    source, target_rel = paths(role, day, report_id)
    meta = validate(data, role, day, report_id)
    target = root / target_rel
    if target.exists():
        if target.read_bytes() != data:
            raise ValueError("CONFLICT: canonical archive differs; will never overwrite")
        outcome = "UNCHANGED"
    elif dry_run:
        outcome = "VALIDATED_ONLY"
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        if target.read_bytes() != data:
            raise ValueError("Readback failed")
        outcome = "CREATED"
    return {"status": outcome, "source_path": source, "archive_path": str(target_rel),
            "source_sha256": hashlib.sha256(data).hexdigest(),
            "payload_type": meta["payload_type"], "run_mode": meta["run_mode"]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--role", choices=sorted(ROLES), required=True)
    p.add_argument("--run-date", required=True)
    p.add_argument("--report-id", required=True)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    source, _ = paths(a.role, a.run_date, a.report_id)
    ref = f"refs/remotes/origin/report/inbox-{a.role}"
    data = subprocess.check_output(["git", "-C", str(root), "show", f"{ref}:{source}"])
    result = promote(a.role, a.run_date, a.report_id, data, root, a.dry_run)
    result["source_ref"] = ref
    result["source_commit"] = subprocess.check_output(["git", "-C", str(root), "rev-parse", ref], text=True).strip()
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
