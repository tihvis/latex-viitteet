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
