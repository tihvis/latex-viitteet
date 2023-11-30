from entities.citation import BookCitation, ArticleCitation


class BibteXExporter:
    def __init__(self) -> None:
        self._br_open = "{"
        self._br_close = "}"
        self._type_prefix_symbol = "@"
        self._variable_separator = ","
        self._variable_equal_symbol = "="
        self._string_quote_character = '"'
        self._tab_whitespace = "    "

    def _dict_to_bib(
        self,
        citation_type: str,
        citation_key: str,
        entries: dict,
        pretty_print: bool = True,
    ) -> str:
        output = ""

        output += f"{self._type_prefix_symbol}{citation_type}"
        output += f"{self._br_open} {citation_key}{self._variable_separator}"
        i = 0
        for entry_key in entries:
            if pretty_print:
                output += "\n"
                output += self._tab_whitespace
            else:
                output += " "
            output += f"{entry_key} {self._variable_equal_symbol} {self._br_open}{entries[entry_key]}{self._br_close}"

            if i == len(entries.keys()) - 1:
                continue
            output += f"{self._variable_separator}"
            i += 1
        if pretty_print:
            output += "\n"
        output += f"{self._br_close}"

        return output

    def _bibtexbook_to_bib(self, bibtex_book: BookCitation):
        fields = {
            "author": " and ".join(bibtex_book.author),
            "title": bibtex_book.title,
            "publisher": bibtex_book.publisher,
            "year": bibtex_book.year,
        }
        return self._dict_to_bib("book", bibtex_book.citation_key, fields, True)

    def _bibtexarticle_to_bib(self, bibtex_article: ArticleCitation):
        fields = {
            "author": " and ".join(bibtex_article.author),
            "title": bibtex_article.title,
            "journal": bibtex_article.journal,
            "year": bibtex_article.year,
            "volume": bibtex_article.volume,
            "pages": bibtex_article.pages.replace("-", "--"),
        }
        return self._dict_to_bib("article", bibtex_article.citation_key, fields, True)

    def bibobject_list_to_text(self, elements: list):
        output = ""

        for element in elements:
            element_string = ""
            if isinstance(element, BookCitation):
                element_string = self._bibtexbook_to_bib(element)

            if isinstance(element, ArticleCitation):
                element_string = self._bibtexarticle_to_bib(element)

            output += element_string + "\n"

        return output
