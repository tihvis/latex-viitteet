import unittest
from entities.citation import CitationFactory


class TestCitation(unittest.TestCase):
    def setUp(self) -> None:
        fields = {
            "type": "book",
            "title": "The Red Book of Westmarch",
            "year": "1234",
            "author": "Bilbo Baggins\r\nFrodo Baggins\r\nSamwise Gamgee",
            "publisher": "Shire University Press",
        }
        self.citation = CitationFactory.create(fields)

    def test_author_returns_correct_list(self):
        expected = ["Bilbo Baggins", "Frodo Baggins", "Samwise Gamgee"]
        output = self.citation.author
        self.assertEqual(expected, output)

    def test_citation_key_returns_correct_citation_key(self):
        expected = "Baggins1234"
        output = self.citation.citation_key
        self.assertEqual(expected, output)

    def test_year_returns_int(self):
        self.assertIsInstance(self.citation.year, int)

    def test_title_returns_correct_title(self):
        expected = "The Red Book of Westmarch"
        output = self.citation.title
        self.assertEqual(expected, output)

    def test_publisher_returns_correct_publisher(self):
        expected = "Shire University Press"
        output = self.citation.publisher
        self.assertEqual(expected, output)

class TestArticleCitation(unittest.TestCase):
    def setUp(self) -> None:
        fields = {
            "type": "article",
            "author":"Tero Karras\r\nSamuli Laine\r\nTimo Aila" ,
            "title": "A Style-Based Generator Architecture for Generative Adversalial Networks",
            "journal": "IEEE Explore",
            "year": "2020",
            "volume": "1",
            "pages": "15--25",
        }
        self.citation = CitationFactory.create(fields)

    def test_author_returns_correct_list(self):
        expected = ["Tero Karras", "Samuli Laine", "Timo Aila"]
        output = self.citation.author
        self.assertEqual(expected, output)

    def test_citation_key_returns_correct_citation_key(self):
        expected = "Karras2020"
        output = self.citation.citation_key
        self.assertEqual(expected, output)

    def test_year_returns_int(self):
        self.assertIsInstance(self.citation.year, int)

    def test_title_returns_correct_title(self):
        expected = "A Style-Based Generator Architecture for Generative Adversalial Networks"
        output = self.citation.title
        self.assertEqual(expected, output)

    def test_journal_returns_correct_journal(self):
        expected = "IEEE Explore"
        output = self.citation.journal
        self.assertEqual(expected, output)

    def test_volume_returns_correct_volume(self):
        expected = "1"
        output = self.citation.volume
        self.assertEqual(expected, output)

    def test_pages_returns_correct_pages(self):
        expected = "15--25"
        output = self.citation.pages
        self.assertEqual(expected, output)
