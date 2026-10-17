#!/usr/bin/env python3
"""One request to diagnose Data Agent Workspace Agent API trigger availability.

Never dispatch the other installed agents, write GitHub reports, call Slack,
or read business sources. Accepted 202 is NOT proof of agent completion.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

from ops007_workspace_agents_e2e import BASE, CHANNEL, request_json


def run_probe(channel: str, run_id: str, token: str):
    if not CHANNEL.fullmatch(channel):
        raise ValueError("Data Agent API channel must be a valid agtch_ ID")
    if not re.fullmatch(r"[0-9]{4,24}", run_id):
        raise ValueError("GitHub run ID must be numeric")
    if not token:
        raise RuntimeError("WORKSPACE_AGENTS_TOKEN is missing. NO AGENT TRIGGERED")

    cycle = f"OPS007-DATA-DIAG-{run_id}"
    print(json.dumps({
        "event": "DATA_TRIGGER_DIAGNOSTIC_START",
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "data_channel_id": channel,
        "run_id": run_id,
        "scope": "ONE_API_REQUEST_NO_OTHER_AGENTS",
    }), flush=True)

    # Exactly one API request, with no retries or user-facing business actions.
    status, payload = request_json(
        "POST",
        f"{BASE}/{channel}/trigger",
        token,
        payload={
            "conversation_key": f"{cycle}-data",
            "input": (
                "Owner-authorized one-time OPS-007 availability test of the "
                "installed Data Agent API channel. Respond with "
                "DATA_AGENT_API_TRIGGER_OK. Use NO tools. Do not read Wix, "
                "GA4, GSC, customer data or GitHub. Do not create any "
                "GitHub reports or send Slack messages. Do not change "
                "settings. This is not a business or multi-agent run."
            ),
        },
        headers={
            "OpenAI-Beta": "workspace_agent_runs=v1",
            "Idempotency-Key": f"{cycle}-data-initial",
        },
    )
    if status != 202:
        raise RuntimeError(f"Unexpected trigger response HTTP {status}, expected 202")
    trigger_id = payload.get("agent_trigger_run_id")
    if not isinstance(trigger_id, str) or not trigger_id.startswith("apirun_"):
        print(json.dumps({
            "event": "HTTP_202_ACCEPTED_NO_VERIFIABLE_RUN_ID",
            "http_status": status,
            "note": "Agent completion NOT verified",
        }), flush=True)
        return
    print(json.dumps({
        "event": "HTTP_202_ACCEPTED",
        "http_status": status,
        "agent_trigger_run_id": trigger_id,
        "note": "Accepted by API only; agent completion NOT verified",
    }), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-channel", required=True)
    parser.add_argument("--run-id", required=True)
    options = parser.parse_args()
    run_probe(options.data_channel, options.run_id, os.environ.get("WORKSPACE_AGENTS_TOKEN", ""))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Existing request_json sanitizes error details and safe support headers.
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}), file=sys.stderr)
        sys.exit(1)
