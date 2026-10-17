"""No-network checks for the single-trigger Data Agent API diagnostic."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ops007_data_api_probe as probe


class SingleDataProbeTests(unittest.TestCase):
    def test_one_api_request_with_no_tools_or_mutating_instruction(self):
        with patch.object(probe, "request_json", return_value=(202, {
            "agent_trigger_run_id": "apirun_demo",
        })) as req:
            probe.run_probe("agtch_valid123", "39015661621", "dummy-token")
        req.assert_called_once()
        args, kwargs = req.call_args
        self.assertEqual(args[0], "POST")
        self.assertIn("/agtch_valid123/trigger", args[1])
        self.assertEqual(kwargs["headers"]["OpenAI-Beta"], "workspace_agent_runs=v1")
        self.assertIn("NO tools", kwargs["payload"]["input"])
        self.assertIn("Do not create any GitHub reports", kwargs["payload"]["input"])
        self.assertIn("Do not", kwargs["payload"]["input"])

    def test_invalid_agent_id_fails_before_trigger(self):
        with patch.object(probe, "request_json") as req:
            with self.assertRaises(ValueError):
                probe.run_probe("data_channel", "39015661621", "dummy-token")
            req.assert_not_called()

    def test_missing_workspace_token_fails_before_trigger(self):
        with patch.object(probe, "request_json") as req:
            with self.assertRaisesRegex(RuntimeError, "missing"):
                probe.run_probe("agtch_valid123", "39015661621", "")
            req.assert_not_called()

    def test_rejected_http_response_is_not_called_success(self):
        with patch.object(probe, "request_json", return_value=(409, {})):
            with self.assertRaisesRegex(RuntimeError, "HTTP 409"):
                probe.run_probe("agtch_valid123", "39015661621", "dummy-token")


if __name__ == "__main__":
    unittest.main()
