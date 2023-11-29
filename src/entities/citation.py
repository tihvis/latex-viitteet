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
    def __init__(self) -> None:
        pass

    @property
    def fields(self) -> dict:
        pass


class BookCitation(Citation):
    """Kirja viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        self._author = fields["author"]
        self._title = fields["title"]
        self._publisher = fields["publisher"]
        self._year = fields["year"]
        #self._isbn = fields["isbn"]

    @property
    def author(self) -> list:
        """Kirjan tekijät listana str muodossa"""
        return self._author

    @property
    def title(self) -> str:
        """Kirjan nimi str muodossa"""
        return self._title

    @property
    def publisher(self) -> str:
        """Kirjan kustantaja str muodossa"""
        return self._publisher

    @property
    def year(self) -> int:
        """Kirjan julkaisuvuosi int muodossa"""
        return self._year

    # @property def isbn(self):

    @property
    def fields(self) -> dict:
        fields = {
            "type": "book",
            "author": self.author,
            "title": self.title,
            "publisher": self.publisher,
            "year": self.year,
            "isbn": self.isbn,
        }
        return fields


class ArticleCitation(Citation):
    """Artikkeli viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        self._author = fields["author"]
        self._title = fields["title"]
        self._journal = fields["journal"]
        self._year = fields["year"]
        self._volume = fields["volume"]
        self._pages = fields["pages"]

    @property
    def author(self) -> list:
        """Artikkelin tekijät listana str muodossa"""
        return self._author

    @property
    def title(self) -> str:
        """Artikkelin nimi str muodossa"""
        return self._title

    @property
    def journal(self) -> str:
        """Artikkelin lehti str muodossa"""
        return self._journal

    @property
    def year(self) -> int:
        """Artikkelin julkaisuvuosi int muodossa"""
        return self._year

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
            "author": self.author,
            "title": self.title,
            "journal": self.journal,
            "year": self.year,
            "volume": self.volume,
            "pages": self.pages,
        }
        return fields


class InproceedingsCitation(Citation):

    """Joku konferenssi pöytäkirja emt viite luokka, sisältää read-only tiedot viitteestä"""

    def __init__(self, fields: dict) -> None:
        self._author = fields["author"]
        self._title = fields["title"]
        self._year = fields["year"]
        self._booktitle = fields["booktitle"]

    @property
    def author(self) -> list:
        """INPROC tekijät listana str muodossa"""
        return self._author

    @property
    def title(self) -> str:
        """INPROC nimi str muodossa"""
        return self._title

    @property
    def year(self) -> int:
        """Kirjan julkaisuvuosi int muodossa"""
        return self._year

    @property
    def booktitle(self) -> str:
        """INPROC julkaisun nimi str muodossa"""
        return self._booktitle

    @property
    def fields(self) -> dict:
        fields = {
            "type": "inproceedings",
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "booktitle": self.booktitle,
        }
        return fields
