class CitationFactory:
    @staticmethod
    def create(data):
        match data["type"]:
            case "book":
                citation = BookCitation(data)
            case "article":
                citation = ArticleCitation(data)
            case "inproceedings":
                citation = InproceedingsCitation(data)
        return citation


class Citation:
    def __init__(self, fields):
        self._author = fields["author"]
        self._title = fields["title"]
        self._year = fields["year"]

    @property
    def fields(self) -> dict:
        pass

    @property
    def citation_key(self):
        return "".join(self.author[0].split(" ")[-1]) + self._year

    @property
    def author(self) -> list:
        """Tekijät listana str muodossa"""
        return self._author.splitlines()

    @property
    def title(self) -> str:
        """Nimi str muodossa"""
        return self._title

    @property
    def year(self) -> int:
        """Julkaisuvuosi int muodossa"""
        return self._year


class BookCitation(Citation):
    """Kirja viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        super().__init__(fields)
        self._publisher = fields["publisher"]

    @property
    def publisher(self) -> str:
        """Kirjan kustantaja str muodossa"""
        return self._publisher

    @property
    def fields(self) -> dict:
        fields = {
            "type": "book",
            "author": self._author,
            "title": self._title,
            "publisher": self._publisher,
            "year": self._year,
        }
        return fields


class ArticleCitation(Citation):
    """Artikkeli viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        super().__init__(fields)
        self._journal = fields["journal"]
        self._volume = fields["volume"]
        self._pages = fields["pages"]

    @property
    def journal(self) -> str:
        """Artikkelin lehti str muodossa"""
        return self._journal

    @property
    def volume(self) -> str:
        """Artikkelin lehden numero str muodossa"""
        return self._volume

    @property
    def pages(self) -> str:
        """Artikkelin sivut str muodossa"""
        return self._pages

    @property
    def fields(self) -> dict:
        fields = {
            "type": "article",
            "author": self._author,
            "title": self._title,
            "journal": self._journal,
            "year": self._year,
            "volume": self._volume,
            "pages": self._pages,
        }
        return fields


class InproceedingsCitation(Citation):

    """Joku konferenssi pöytäkirja emt viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        super().__init__(fields)
        self._booktitle = fields["booktitle"]

    @property
    def booktitle(self) -> str:
        """INPROC julkaisun nimi str muodossa"""
        return self._booktitle

    @property
    def fields(self) -> dict:
        fields = {
            "type": "inproceedings",
            "author": self._author,
            "title": self._title,
            "year": self._year,
            "booktitle": self._booktitle,
        }
        return fields
