"""Unit tests for strict inbox promotion."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("promote_agent_inbox", Path(__file__).resolve().parents[1] / "scripts/promote_agent_inbox.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def sample(role="growth", run_mode="TECHNICAL_SMOKE_TEST"):
    meta = {"schema_version": "1.0", "role": role, "report_id": "OPS007-PILOT-V5-2026-10-16",
            "run_date": "2026-10-16", "run_mode": run_mode,
            "payload_type": "SYNTHETIC_TEST", "task_reference": "OPS-007 technical check",
            "source_conversation_url": None, "source_evidence": ["https://github.com/hatif007/shalom-lamalka-agent-registry"],
            "scope": "INFRASTRUCTURE_ONLY", "owner_approval": "Owner authorizes synthetic report"}
    return ("<!-- REPORT_ARCHIVE_V1\n" + json.dumps(meta, separators=(",", ":"))
            + "\nREPORT_ARCHIVE_V1 -->\n# SYNTHETIC TEST\n"
            + "SYNTHETIC technical smoke test only; never proof of actual agent invocation or business data.\n").encode()


class Promotion(unittest.TestCase):
    def test_copy_preserves_exact_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            source = sample()
            args = ("growth", "2026-10-16", "OPS007-PILOT-V5-2026-10-16")
            first = p.promote(*args, source, Path(d))
            self.assertEqual("CREATED", first["status"])
            self.assertEqual(source, (Path(d) / first["archive_path"]).read_bytes())
            self.assertEqual("UNCHANGED", p.promote(*args, source, Path(d))["status"])

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            result = p.promote("growth", "2026-10-16", "OPS007-PILOT-V5-2026-10-16", sample(), Path(d), True)
            self.assertEqual("VALIDATED_ONLY", result["status"])
            self.assertFalse((Path(d) / result["archive_path"]).exists())

    def test_identity_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "Metadata/path mismatch"):
                p.promote("seo", "2026-10-16", "OPS007-PILOT-V5-2026-10-16", sample(), Path(d))

    def test_bad_mode_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "Unsupported"):
                p.promote("growth", "2026-10-16", "OPS007-PILOT-V5-2026-10-16",
                          sample(run_mode="INSTALLED_AGENT_TEST"), Path(d))

    def test_conflicting_archive_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            args = ("growth", "2026-10-16", "OPS007-PILOT-V5-2026-10-16")
            r = p.promote(*args, sample(), Path(d))
            (Path(d) / r["archive_path"]).write_text("DIFFERENT", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "CONFLICT"):
                p.promote(*args, sample(), Path(d))

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            p.paths("growth", "2026-10-16", "../SECRET")

    def test_installed_agent_cannot_be_falsely_verified(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "Synthetic tests"):
                p.promote("growth", "2026-10-16", "OPS007-PILOT-V5-2026-10-16",
                          sample(run_mode="INSTALLED_AGENT_VERIFIED"), Path(d))


if __name__ == "__main__":
    unittest.main()
