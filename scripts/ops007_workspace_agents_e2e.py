#!/usr/bin/env python3
"""One bounded, genuine four-Workspace-Agent API-trigger acceptance test.

Does NOT substitute a ChatGPT Scheduled Task, coordinator-authored specialist file,
or coordinator-authored Slack message for an installed agent run.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from promote_agent_inbox import validate as validate_report

REPO = "hatif007/shalom-lamalka-agent-registry"
BASE = "https://api.chatgpt.com/v1/workspace_agents"
GITHUB = f"https://api.github.com/repos/{REPO}"
ROLES = ("data", "seo", "website")
CHANNEL = re.compile(r"agtch_[A-Za-z0-9_-]+\Z")
RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{4,100}\Z")


def request_json(method, url, token, payload=None, headers=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if data is not None:
        h["Content-Type"] = "application/json"
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Never print bearer credentials or arbitrary response bodies.
        raise RuntimeError(f"{method} request failed: HTTP {e.code} at {urllib.parse.urlsplit(url).path}") from e


def trigger(channel, token, cycle, text, label):
    status, result = request_json(
        "POST", f"{BASE}/{channel}/trigger", token,
        payload={"conversation_key": f"{cycle}-{label}", "input": text},
        headers={"OpenAI-Beta": "workspace_agent_runs=v1",
                 "Idempotency-Key": f"{cycle}-{label}-initial"},
    )
    if status != 202 or not result.get("agent_trigger_run_id"):
        raise RuntimeError(f"{label}: trigger not accepted with a verifiable beta run ID (HTTP {status})")
    value = result["agent_trigger_run_id"]
    if not value.startswith("apirun_"):
        raise RuntimeError(f"{label}: invalid API run identifier")
    print(json.dumps({"stage": label, "event": "TRIGGER_ACCEPTED",
                      "run_id": value, "conversation_url": result.get("conversation_url")}), flush=True)
    return value


def await_completion(channel, token, api_run_id, label, timeout_seconds=720):
    deadline = time.monotonic() + timeout_seconds
    last = ""
    while time.monotonic() < deadline:
        _, result = request_json("GET", f"{BASE}/{channel}/runs/{api_run_id}", token)
        state = result.get("status", "unknown")
        if state != last:
            print(json.dumps({"stage": label, "event": "RUN_STATUS", "status": state, "run_id": api_run_id}), flush=True)
            last = state
        if state == "completed":
            return
        if state in {"failed", "suspended"}:
            raise RuntimeError(f"{label}: agent run {state}; resolve its real agent approval/tool failure")
        time.sleep(12)
    raise TimeoutError(f"{label}: native API run did not complete within {timeout_seconds} seconds")


def report_location(cycle, day, role):
    report_id = f"{cycle}-{role}"
    if not RUN_ID.fullmatch(report_id):
        raise ValueError("Invalid cycle/report ID")
    return report_id, f"reports/runs/{day}/{role}/{report_id}.md"


def github_read_report(gh_token, cycle, day, role, attempts=16, required_sources=None):
    report_id, path = report_location(cycle, day, role)
    ref = f"report/inbox-{role}"
    url = f"{GITHUB}/contents/{path}?ref={urllib.parse.quote(ref, safe='')}"
    for attempt in range(attempts):
        try:
            _, result = request_json("GET", url, gh_token, headers={"Accept": "application/vnd.github+json"})
        except RuntimeError as e:
            if "HTTP 404" not in str(e):
                raise
            if attempt == attempts - 1:
                raise RuntimeError(f"{role}: no new report at exact inbox path {path}") from e
            time.sleep(10)
            continue
        if result.get("type") != "file" or result.get("encoding") != "base64":
            raise RuntimeError(f"{role}: report response is not a base64 file")
        data = base64.b64decode(result["content"])
        meta = validate_report(data, role, day, report_id)
        if required_sources:
            body = data.decode("utf-8")
            for source in required_sources:
                if source["url"] not in body or source["sha"] not in body:
                    raise RuntimeError("Growth report missing actual specialist source link or SHA")
        if meta["payload_type"] != "SYNTHETIC_TEST" or meta["run_mode"] != "TECHNICAL_SMOKE_TEST":
            raise RuntimeError(f"{role}: wrong metadata for test")
        calculated = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if result.get("sha") != calculated:
            raise RuntimeError(f"{role}: GitHub blob SHA mismatch")
        browser_url = f"https://github.com/{REPO}/blob/{ref}/{path}"
        item = {"role": role, "path": path, "branch": ref, "sha": calculated, "url": browser_url}
        print(json.dumps({"stage": role, "event": "GITHUB_READBACK_VERIFIED", **item}), flush=True)
        return item
    raise RuntimeError(f"{role}: report unavailable")


def specialist_message(cycle, day, role):
    rid, path = report_location(cycle, day, role)
    return f"""OPS-007 owner-authorized native Workspace-Agent API test.
Cycle: {cycle}. Your role: {role}. Date (Asia/Jerusalem): {day}.
This is SYNTHETIC TEST ONLY, not business analytics. Do not read Wix/GA4/GSC or change any business system.
Use existing GitHub Writer permissions ONLY: repository {REPO},
branch report/inbox-{role}, exact new file {path}.
Read the REPORT_ARCHIVE_V1 contract from main before writing.
Create a concise identity report with valid JSON header, role={role},
run_date={day}, report_id={rid}, payload_type=SYNTHETIC_TEST,
run_mode=TECHNICAL_SMOKE_TEST. Include all contract-required metadata.
Clearly say SYNTHETIC, role name, cycle ID, whether writes/approval succeeded, and no claim of other agents running.
Try ONE authorized GitHub create_file action. Read back and report real SHA/URL.
If your active policies prohibit GitHub writing, report BLOCKED; do not bypass.
Do not send Slack, create PRs, merge, schedule new tasks or generate business data.
GROW-SEO-01=HOLD. Never claim native runtime verification based solely on the created file.
"""


def growth_message(cycle, day, sources):
    rid, path = report_location(cycle, day, "growth")
    evidence = "\n".join(
        f"- {s['role']}: {s['url']} (GitHub blob SHA {s['sha']})" for s in sources
    )
    return f"""Owner-authorized Growth Manager PILOT native API test. Cycle: {cycle}, date {day}.
Read each of these three distinct, newly generated SYNTHETIC specialist reports yourself:
{evidence}
Cross-check role, report_id, metadata, content, links and SHA. Do NOT just repeat coordinator claims.
Write a DETAILED Hebrew Growth Manager Pilot report with a per-specialist evidence table,
your own synthesis of what worked/failed, GitHub readback, approvals, remaining blockers,
tool invocation provenance and final PASS/PARTIAL/BLOCKED. Never invent business findings.
Save exactly ONE synthetic Growth report under pre-existing branch report/inbox-growth,
path {path}, valid REPORT_ARCHIVE_V1 metadata:
role=growth; run_date={day}; report_id={rid};
run_mode=TECHNICAL_SMOKE_TEST; payload_type=SYNTHETIC_TEST.
Read it back and verify the GitHub URL and SHA.
Only after the report is successfully stored, use YOUR OWN authorized Slack tool
to send ONE message in #business-insights with the exact cycle {cycle}, status and
link to the actual Growth report. Check for duplicate cycle first.
Return a real Slack permalink; if Slack action unavailable or approval blocked, report NOT_POSTED.
Never edit Wix, GA4, GSC, orders, products, prices, settings or other agent permissions.
GROW-SEO-01=HOLD. No coordinator-generated message may stand in for your Slack send.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cycle", required=True)
    ap.add_argument("--data-channel", required=True)
    ap.add_argument("--seo-channel", required=True)
    ap.add_argument("--website-channel", required=True)
    ap.add_argument("--growth-pilot-channel", required=True)
    a = ap.parse_args()
    if not RUN_ID.fullmatch(a.cycle):
        raise ValueError("Invalid cycle identifier")
    channels = {"data": a.data_channel, "seo": a.seo_channel,
                "website": a.website_channel, "growth": a.growth_pilot_channel}
    if any(not CHANNEL.fullmatch(c) for c in channels.values()):
        raise ValueError("All four real Workspace Agent channel IDs must start with agtch_")
    token = os.environ.get("WORKSPACE_AGENTS_TOKEN", "")
    gh_token = os.environ.get("GH_READ_TOKEN", "")
    if not token or not gh_token:
        raise RuntimeError("Missing WORKSPACE_AGENTS_TOKEN or GitHub Actions GH_READ_TOKEN. NO AGENTS TRIGGERED")
    day = datetime.now(ZoneInfo("Asia/Jerusalem")).date().isoformat()
    print(json.dumps({"cycle": a.cycle, "date": day, "stage": "PREFLIGHT_PASS"}), flush=True)
    active = {}
    for role in ROLES:
        active[role] = trigger(channels[role], token, a.cycle,
                               specialist_message(a.cycle, day, role), role)
    for role in ROLES:
        await_completion(channels[role], token, active[role], role)
    reports = [github_read_report(gh_token, a.cycle, day, role) for role in ROLES]
    growth_run = trigger(channels["growth"], token, a.cycle,
                         growth_message(a.cycle, day, reports), "growth-pilot")
    await_completion(channels["growth"], token, growth_run, "growth-pilot")
    growth = github_read_report(gh_token, a.cycle, day, "growth", required_sources=reports)
    print(json.dumps({"overall": "PARTIAL_UNTIL_SLACK_PERMALINK_VERIFIED",
                      "native_agent_runs": {**active, "growth": growth_run},
                      "reports": reports, "growth_report": growth,
                      "slack": "VERIFY_WITH_SLACK_CONNECTOR_AND_PERMALINK"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Fail closed. Do not create a Growth report or Slack message in this coordinator.
        print(json.dumps({"overall": "BLOCKED", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
