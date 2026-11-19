"""Knowledge base search: frontmatter parsing, in-memory BM25 index and search.

The index is built from docs/knowledge/**/*.md on every call. Nothing is written to disk,
so there is no index to regenerate or to drift from the docs.
Stdout is the command result. Usage errors go to stderr.

Usage:
    python3 -m scripts.knowledge_index search "<query>"
"""

import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = Path("docs") / "knowledge"
TOKEN = re.compile(r"[0-9a-záéíóúüñ]+", re.IGNORECASE)
K1 = 1.5
B = 0.75


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return the flat key/value block and the remaining markdown.

    Args:
        text: Full file contents.

    Returns:
        tuple: Frontmatter dict (empty when there is none) and the body.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    data = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data, text[end + 5:]


def tokenize(text: str) -> list[str]:
    """Split text into lowercase tokens.

    Args:
        text: Any string.

    Returns:
        list: Tokens, in order, including repeats.
    """
    return [token.lower() for token in TOKEN.findall(text)]


def load_docs(root: Path = ROOT) -> list[dict]:
    """Read every markdown file under docs/knowledge.

    Args:
        root: Repository root.

    Returns:
        list: One dict per file, with path, frontmatter and text.
    """
    docs = []
    for path in sorted((root / KNOWLEDGE_DIR).rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        frontmatter, _body = parse_frontmatter(text)
        docs.append({
            "path": path.relative_to(root).as_posix(),
            "frontmatter": frontmatter,
            "text": text,
        })
    return docs


def _chunks(doc: dict) -> list[dict]:
    lines = doc["text"].splitlines()
    headings = [index for index, line in enumerate(lines) if line.startswith("## ")]
    if not headings:
        headings = [0]
    chunks = []
    for position, start in enumerate(headings):
        end = headings[position + 1] if position + 1 < len(headings) else len(lines)
        heading = lines[start][3:].strip() if lines[start].startswith("## ") else lines[start].lstrip("#").strip()
        body = "\n".join(lines[start:end])
        extra = " ".join(doc["frontmatter"].values())
        tokens = tokenize(heading + "\n" + body + "\n" + extra)
        counts: dict[str, int] = {}
        for token in tokens:
            counts[token] = counts.get(token, 0) + 1
        chunks.append({
            "path": doc["path"],
            "heading": heading,
            "line": start + 1,
            "tf": counts,
            "dl": len(tokens),
        })
    return chunks


def build_index(docs: list[dict]) -> dict:
    """Build a deterministic BM25 index, one chunk per "## " section.

    Args:
        docs: Output of load_docs.

    Returns:
        dict: Chunks, document frequency, average length and chunk count.
    """
    chunks = [chunk for doc in docs for chunk in _chunks(doc)]
    frequency: dict[str, int] = {}
    for chunk in chunks:
        for token in chunk["tf"]:
            frequency[token] = frequency.get(token, 0) + 1
    total = sum(chunk["dl"] for chunk in chunks)
    average = total / len(chunks) if chunks else 0
    return {"avgdl": average, "chunks": chunks, "df": frequency, "n": len(chunks)}


def search(index: dict, query: str, k: int = 5) -> list[dict]:
    """Rank chunks for a query.

    Args:
        index: Output of build_index.
        query: Free text.
        k: Maximum hits.

    Returns:
        list: Hits with path, line, heading and score. Empty when nothing matches.
    """
    terms = tokenize(query)
    if not terms or not index["n"] or not index["avgdl"]:
        return []
    ranked = []
    for chunk in index["chunks"]:
        score = 0.0
        for term in terms:
            freq = chunk["tf"].get(term)
            if not freq:
                continue
            docs_with_term = index["df"].get(term, 0)
            idf = math.log((index["n"] - docs_with_term + 0.5) / (docs_with_term + 0.5) + 1)
            normal = freq + K1 * (1 - B + B * chunk["dl"] / index["avgdl"])
            score += idf * (freq * (K1 + 1)) / normal
        if score > 0:
            ranked.append((score, chunk))
    ranked.sort(key=lambda item: (-item[0], item[1]["path"], item[1]["line"]))
    return [
        {"path": chunk["path"], "line": chunk["line"], "heading": chunk["heading"], "score": round(score, 4)}
        for score, chunk in ranked[:k]
    ]


def main(argv: list[str]) -> int:
    """Run a search over docs/knowledge.

    Args:
        argv: Arguments after the program name. Expected: search <query>.

    Returns:
        int: Process exit code. 2 for a usage error.
    """
    if not argv or argv[0] != "search":
        print("usage: knowledge_index search <query>", file=sys.stderr)
        return 2
    query = " ".join(argv[1:])
    if not query:
        print("search needs a query", file=sys.stderr)
        return 2
    hits = search(build_index(load_docs()), query)
    if not hits:
        print("no hits")
        return 0
    for hit in hits:
        print(f"{hit['path']}:{hit['line']} {hit['heading']} {hit['score']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
