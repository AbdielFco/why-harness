"""Ask for human confirmation before shell commands that cross a human gate.

Cursor runs this as a beforeShellExecution hook. Stdin is the hook payload (JSON),
stdout is the hook response. A payload that cannot be read is denied, never allowed.

The hook only sees the shell command text. It cannot see a file edit, a write done
inside a running process, or a delete done from code.

Edit only the GATES tuple when installing the harness in a project.
"""

import json
import logging
import re
import sys

logger = logging.getLogger(__name__)

# PROJECT: (regex, gate name). Mirror the "Human gates" section of AGENTS.md.
GATES = (
    (r"\bgit(\s+\S+){0,4}\s+commit\b", "commit"),
    (r"\bgit(\s+\S+){0,4}\s+push\b", "push"),
    (r"\bgit\s+reset\s+--hard\b", "discard work"),
    (r"\bgit\s+clean\b", "delete files"),
    (r"\bgit\s+rm\b", "delete files"),
    (r"\brm\s", "delete files"),
    (r"-delete\b", "delete files"),
    (r"\buv\s+(add|remove)\b", "change dependencies"),
    (r"\b(uv\s+)?pip3?\s+install\b", "change dependencies"),
    (r"\bpoetry\s+(add|remove)\b", "change dependencies"),
    (r"\b(npm|pnpm|yarn|bun)\s+(add|remove|uninstall|install|i)\b", "change dependencies"),
    (r"\bcargo\s+(add|remove)\b", "change dependencies"),
    (r"\bdeploy\b", "deploy"),
    (r"\bterraform\s+(apply|destroy)\b", "infrastructure change"),
    (r"\bkubectl\s+(apply|delete)\b", "infrastructure change"),
    (r"(^|[\s/])\.cursor/hooks\b", "edit the harness gates"),
)


def decide(payload: object) -> dict:
    """Return the hook response for one payload.

    Args:
        payload: Parsed stdin. Expected: a dict with a string "command".

    Returns:
        dict: {"permission": "allow"} or an ask/deny response with messages.
    """
    if not isinstance(payload, dict):
        logger.error("[GATE] hook payload is not an object")
        return _response("deny", "unreadable hook payload")
    command = payload.get("command", "")
    if not isinstance(command, str):
        logger.error("[GATE] hook command is not a string")
        return _response("deny", "unreadable hook payload")
    for pattern, gate in GATES:
        if re.search(pattern, command):
            return _response("ask", gate)
    return {"permission": "allow"}


def _response(permission: str, gate: str) -> dict:
    return {
        "permission": permission,
        "user_message": f"Human gate: {gate}",
        "agent_message": f"Command stopped at gate '{gate}'. Wait for confirmation.",
    }


def main() -> None:
    """Read the payload from stdin and print the decision."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        logger.exception("[GATE] hook stdin is not JSON")
        payload = None
    print(json.dumps(decide(payload)))


if __name__ == "__main__":
    main()
