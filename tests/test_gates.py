"""Tests for the beforeShellExecution gate hook."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / ".cursor" / "hooks" / "gates.py"


def run_hook(stdin: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(HOOK)], input=stdin, capture_output=True, text=True, check=True
    )
    return json.loads(result.stdout)


class GateDecisionTest(unittest.TestCase):
    def test_read_only_command_is_allowed(self):
        self.assertEqual(run_hook(json.dumps({"command": "git status"})), {"permission": "allow"})

    def test_search_is_allowed(self):
        self.assertEqual(run_hook(json.dumps({"command": "rg -n TODO scripts"})), {"permission": "allow"})

    def test_gated_commands_ask(self):
        cases = {
            "git commit -m 'x'": "commit",
            "git -C repo push origin main": "push",
            "rm -rf build": "delete files",
            "find . -name '*.tmp' -delete": "delete files",
            "uv add requests": "change dependencies",
            "pnpm add lodash": "change dependencies",
            "pip install requests": "change dependencies",
            "terraform apply": "infrastructure change",
        }
        for command, gate in cases.items():
            with self.subTest(command=command):
                response = run_hook(json.dumps({"command": command}))
                self.assertEqual(response["permission"], "ask")
                self.assertIn(gate, response["user_message"])

    def test_gate_hides_in_a_chain(self):
        response = run_hook(json.dumps({"command": "ls && rm notes.txt"}))
        self.assertEqual(response["permission"], "ask")

    def test_non_json_stdin_is_denied(self):
        self.assertEqual(run_hook("not json")["permission"], "deny")

    def test_non_object_payload_is_denied(self):
        self.assertEqual(run_hook(json.dumps(["rm", "-rf"]))["permission"], "deny")

    def test_non_string_command_is_denied(self):
        self.assertEqual(run_hook(json.dumps({"command": ["rm", "-rf"]}))["permission"], "deny")


if __name__ == "__main__":
    unittest.main()
