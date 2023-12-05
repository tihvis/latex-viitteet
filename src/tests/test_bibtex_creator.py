import unittest
from bibtex.bibtex_creator import BibteXExporter
from entities.citation import CitationFactory


class TestBibtexCreator(unittest.TestCase):
    def test_correct_bibtex(self):
        book_fields = {
            "type": "book",
            "title": "The Red Book of Westmarch",
            "year": "1234",
            "author": "Bilbo Baggins\r\nFrodo Baggins\r\nSamwise Gamgee",
            "publisher": "Shire University Press",
        }
        article_fields = {
            "type": "article",
            "title": "On computable numbers, with an application to the Entscheidungsproblem",
            "author": "A. M. Turing",
            "journal": "Proceedings of the London Mathematical Society",
            "volume": "42",
            "pages": "230-265",
            "year": "1937",
        }
        inproceedings_fields = {
            "type": "inproceedings",
            "title": "Guarded Commands, Non-Determinacy and a Calculus for the Derivation of Programs",
            "author": "Edsger W. Dijkstra",
            "year": "1975",
            "booktitle": "Proceedings of the International Conference on Reliable Software",
        }
        book = CitationFactory.create(book_fields)
        article = CitationFactory.create(article_fields)
        inproceedings = CitationFactory.create(inproceedings_fields)
        citations = [article, book, inproceedings]
        exporter = BibteXExporter()
        output = exporter.bibobject_list_to_text(citations)
        with open("src/tests/bibtex_example.bib", encoding="utf-8") as f:
            expected = f.read()
            self.maxDiff = None
            self.assertEqual(expected, output)
