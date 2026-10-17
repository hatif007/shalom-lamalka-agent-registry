"""No-network checks for native Workspace Agents API orchestration safety."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ops007_workspace_agents_e2e as e2e


class NativeAgentE2ETests(unittest.TestCase):
    def test_source_paths_are_per_role_and_new_per_cycle(self):
        for role in ("data", "seo", "website", "growth"):
            rid, path = e2e.report_location("OPS007-NATIVE-123", "2026-10-16", role)
            self.assertEqual(f"OPS007-NATIVE-123-{role}", rid)
            self.assertEqual(f"reports/runs/2026-10-16/{role}/{rid}.md", path)

    def test_bad_cycle_path_rejected(self):
        with self.assertRaises(ValueError):
            e2e.report_location("../../../secrets", "2026-10-16", "growth")

    def test_specialist_request_is_synthetic_and_role_limited(self):
        message = e2e.specialist_message("OPS007-NATIVE-123", "2026-10-16", "data")
        self.assertIn("SYNTHETIC_TEST", message)
        self.assertIn("TECHNICAL_SMOKE_TEST", message)
        self.assertIn("report/inbox-data", message)
        self.assertIn("Do not read Wix/GA4/GSC", message)

    def test_growth_request_includes_verified_sources(self):
        sources = [{"role": "data", "sha": "ab34", "url": "https://github.com/example/data"},
                   {"role": "seo", "sha": "cd34", "url": "https://github.com/example/seo"},
                   {"role": "website", "sha": "ef34", "url": "https://github.com/example/website"}]
        text = e2e.growth_message("OPS007-NATIVE-123", "2026-10-16", sources)
        for s in sources:
            self.assertIn(s["url"], text)
            self.assertIn(s["sha"], text)
        self.assertIn("#business-insights", text)
        self.assertIn("Growth Manager PILOT", text)

    def test_four_distinct_workspace_channels_required(self):
        valid = {
            "data": "agtch_data123",
            "seo": "agtch_seo123",
            "website": "agtch_website123",
            "growth": "agtch_growth123",
        }
        self.assertIsNone(e2e.validate_channels(valid))
        duplicate = {**valid, "website": valid["growth"]}
        with self.assertRaisesRegex(ValueError, "Duplicate Workspace Agent channel IDs"):
            e2e.validate_channels(duplicate)
        with self.assertRaisesRegex(ValueError, "start with agtch_"):
            e2e.validate_channels({**valid, "website": "website_channel"})

    def test_duplicated_channel_aborts_before_any_agent_api_call(self):
        args = [
            "runner", "--cycle", "OPS007-NATIVE-123",
            "--data-channel", "agtch_data123",
            "--seo-channel", "agtch_seo123",
            "--website-channel", "agtch_same123",
            "--growth-pilot-channel", "agtch_same123",
        ]
        with patch.object(sys, "argv", args), patch.object(e2e, "trigger") as mocked:
            with self.assertRaisesRegex(ValueError, "Duplicate Workspace Agent channel IDs"):
                e2e.main()
            mocked.assert_not_called()

    def test_api_http_conflict_reports_sanitized_details(self):
        import io
        import json
        import urllib.error
        error_body = json.dumps({
            "error": {
                "code": "agent_not_runnable",
                "message": "Agent not published; token=sk-ABCDEFGHIJKLMNOPQRSTUVWX123456",
            }
        }).encode()
        def reject(request, timeout):
            raise urllib.error.HTTPError(
                request.full_url, 409, "Conflict", {},
                io.BytesIO(error_body),
            )
        with patch.object(e2e.urllib.request, "urlopen", side_effect=reject):
            with self.assertRaises(RuntimeError) as capture:
                e2e.request_json("POST", "https://api.chatgpt.com/v1/workspace_agents/agtch_test/trigger", "secret", {"input": "hello"})
        diagnostic = str(capture.exception)
        self.assertIn("HTTP 409", diagnostic)
        self.assertIn("agent_not_runnable", diagnostic)
        self.assertNotIn("sk-ABCDEFGHIJKLMNOPQRSTUVWX123456", diagnostic)
        self.assertNotIn("secret", diagnostic)

    def test_api_http_non_json_response_remains_redacted(self):
        import io
        import urllib.error
        def reject(request, timeout):
            raise urllib.error.HTTPError(request.full_url, 409, "Conflict", {}, io.BytesIO(b"unexpected raw secret"))
        with patch.object(e2e.urllib.request, "urlopen", side_effect=reject):
            with self.assertRaises(RuntimeError) as capture:
                e2e.request_json("POST", "https://api.chatgpt.com/v1/workspace_agents/agtch_test/trigger", "secret", {"input": "hello"})
        self.assertNotIn("raw secret", str(capture.exception))

    def test_api_trigger_requires_verifiable_run_id(self):
        with patch.object(e2e, "request_json", return_value=(202, {"conversation_url": "https://chatgpt.com/c/1"})):
            with self.assertRaisesRegex(RuntimeError, "verifiable beta run ID"):
                e2e.trigger("agtch_demo", "unused-secret", "OPS007-NATIVE-123", "SYNTHETIC", "growth")

    def test_trigger_uses_accepted_id_and_no_duplicate_event(self):
        with patch.object(e2e, "request_json", return_value=(202, {"agent_trigger_run_id": "apirun_demo"})) as request:
            rid = e2e.trigger("agtch_demo", "secret", "OPS007-NATIVE-123", "SYNTHETIC", "data")
            self.assertEqual("apirun_demo", rid)
            headers = request.call_args.kwargs["headers"]
            self.assertEqual("OPS007-NATIVE-123-data-initial", headers["Idempotency-Key"])
            self.assertEqual("workspace_agent_runs=v1", headers["OpenAI-Beta"])


if __name__ == "__main__":
    unittest.main()
