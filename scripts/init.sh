#!/usr/bin/env bash
# scripts/init.sh — session check for the harness.
#
# Run it when a session starts and before a phase closes (Plan, Implement, Verify).
# One line per check, prefixed [OK], [WARN] or [FAIL]. Exit 1 on any [FAIL].
# Values from .env are never printed, only variable names.
#
# Usage: ./scripts/init.sh

set -u
cd "$(dirname "$0")/.." || exit 1

# ---- PROJECT CONFIG: the only block you edit when installing the harness ----
TOOLS=(python3 git)
TEST_CMD="python3 -m unittest discover tests"
PROJECT_FILES=()
# ---- end PROJECT CONFIG ----

HARNESS_FILES=(
  AGENTS.md
  .cursor/hooks.json
  .cursor/hooks/gates.py
  .cursor/agents/planner.md
  .cursor/agents/test-writer.md
  .cursor/agents/implementer.md
  .cursor/agents/validator.md
  .cursor/agents/reviewer.md
  scripts/knowledge_index.py
  docs/README.md
  docs/knowledge/README.md
  docs/work/0000-template.md
  docs/decisions/0000-template.md
)

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'
EXIT_CODE=0

ok()      { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()    { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
fail()    { printf "${RED}[FAIL]${NC}  %s\n" "$1"; EXIT_CODE=1; }
section() { printf "\n== %s\n" "$1"; }

section "1. Tooling"
for tool in "${TOOLS[@]}"; do
  if command -v "$tool" >/dev/null 2>&1; then
    ok "$tool found"
  else
    fail "$tool is not installed"
  fi
done
if [ "$EXIT_CODE" -ne 0 ]; then
  printf "\nEnvironment is NOT ready. Fix the failures above.\n"
  exit 1
fi

section "2. Harness and project files"
for file in "${HARNESS_FILES[@]}" ${PROJECT_FILES[@]+"${PROJECT_FILES[@]}"}; do
  if [ -f "$file" ]; then
    ok "exists $file"
  else
    fail "missing $file"
  fi
done

section "3. Environment file (names only)"
if [ ! -f .env.example ]; then
  ok "no .env.example: the project declares no variables"
elif [ ! -f .env ]; then
  warn ".env is missing. Copy .env.example and fill the values"
else
  missing=$(comm -23 \
    <(grep -v '^#' .env.example | grep '=' | cut -d= -f1 | sort -u) \
    <(grep -v '^#' .env | grep '=' | cut -d= -f1 | sort -u))
  if [ -n "$missing" ]; then
    warn "names in .env.example but not in .env: $(echo "$missing" | tr '\n' ' ')"
  else
    ok "every name in .env.example is set in .env"
  fi
fi

section "4. Tests"
if $TEST_CMD; then
  ok "tests are green"
else
  fail "tests have failures"
fi

section "Summary"
if [ "$EXIT_CODE" -eq 0 ]; then
  ok "Environment is ready."
else
  fail "Environment is NOT ready. Fix the failures above before advancing."
fi
exit "$EXIT_CODE"
