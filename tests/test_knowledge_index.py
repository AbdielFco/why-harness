"""Tests for the in-memory BM25 knowledge search."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts import knowledge_index as ki

ROOT = Path(__file__).resolve().parents[1]


class FrontmatterTest(unittest.TestCase):
    def test_flat_block_is_parsed(self):
        data, body = ki.parse_frontmatter("---\nid: order\nstatus: active\n---\n# Order\n")
        self.assertEqual(data, {"id": "order", "status": "active"})
        self.assertEqual(body, "# Order\n")

    def test_missing_or_unclosed_block_returns_text(self):
        self.assertEqual(ki.parse_frontmatter("# Title\n"), ({}, "# Title\n"))
        self.assertEqual(ki.parse_frontmatter("---\nid: x\n"), ({}, "---\nid: x\n"))


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        folder = root / "docs" / "knowledge" / "entities"
        folder.mkdir(parents=True)
        (folder / "order.md").write_text(
            "---\nid: order\nstatus: active\n---\n# Order\n\n## Ciclo de vida\n\nUna orden pasa por creada, pagada y enviada.\n\n## Fuente\n\nTabla orders.\n",
            encoding="utf-8",
        )
        (folder / "customer.md").write_text(
            "---\nid: customer\nstatus: active\n---\n# Customer\n\n## Qué es\n\nQuien compra.\n",
            encoding="utf-8",
        )
        self.index = ki.build_index(ki.load_docs(root))

    def tearDown(self):
        self.tmp.cleanup()

    def test_hit_points_at_the_section(self):
        hits = ki.search(self.index, "orden pagada")
        self.assertEqual(hits[0]["path"], "docs/knowledge/entities/order.md")
        self.assertEqual(hits[0]["heading"], "Ciclo de vida")
        self.assertEqual(hits[0]["line"], 7)

    def test_frontmatter_values_are_searchable(self):
        hits = ki.search(self.index, "customer")
        self.assertEqual(hits[0]["path"], "docs/knowledge/entities/customer.md")

    def test_no_match_and_empty_query_return_nothing(self):
        self.assertEqual(ki.search(self.index, "zzzz"), [])
        self.assertEqual(ki.search(self.index, "  "), [])

    def test_empty_knowledge_returns_nothing(self):
        self.assertEqual(ki.search(ki.build_index([]), "orden"), [])

    def test_ranking_is_deterministic(self):
        self.assertEqual(ki.search(self.index, "orden"), ki.search(self.index, "orden"))


class CliTest(unittest.TestCase):
    def test_usage_errors_exit_2(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(ki.main([]), 2)
            self.assertEqual(ki.main(["search"]), 2)

    def test_repo_examples_are_findable(self):
        hits = ki.search(ki.build_index(ki.load_docs(ROOT)), "ciclo de vida orden")
        self.assertTrue(hits)
        self.assertTrue(hits[0]["path"].startswith("docs/knowledge/"))


if __name__ == "__main__":
    unittest.main()
