#import app
from sqlalchemy.sql import text

class Database():
    def __init__(self, db) -> None:
        self._db = db

    def add_book(self, authors, title, publisher, year):
        try:
            type = "book"
            sql = text("INSERT INTO citations (type, title,publisher,year) \
                 VALUES (:type, :title, :publisher, :year) RETURNING id")
            citation_id = self._db.session.execute(sql, {"type":type, "title":title, "publisher":publisher,\
                 "year":year}).fetchone()[0]
            author_ids = []
            for author in authors.splitlines():
                author_ids.append(self._add_author(author))
            for author_id in author_ids:
                self._add_author_citation(author_id, citation_id)
            self._db.session.commit()
        except: #tää pitäis määritellä, lint: "No exception type(s) specified (bare-except)"
            return False
        return True
    
    def add_article(self, authors, title, journal, year, volume, pages):
        try:
            type = "article"
            sql = text("INSERT INTO citations (type, title, journal, year, volume, pages) \
                 VALUES (:type, :title, :journal, :year, :volume, :pages) RETURNING id")
            citation_id = self._db.session.execute(sql, {"type":type, "title":title, "journal":journal,\
                 "year":year, "volume":volume, "pages":pages}).fetchone()[0]
            author_ids = []
            for author in authors.splitlines():
                author_ids.append(self._add_author(author))
            for author_id in author_ids:
                self._add_author_citation(author_id, citation_id)
            self._db.session.commit()
        except: #tää pitäis määritellä, lint: "No exception type(s) specified (bare-except)"
            return False
        return True

    def _add_author(self, name):
        sql = text("INSERT INTO authors (name) VALUES (:name) ON CONFLICT DO NOTHING")
        self._db.session.execute(sql, {"name": name})
        self._db.session.commit()
        sql = text("SELECT id FROM authors WHERE name = :name")
        result = self._db.session.execute(sql, {"name":name}).fetchone()[0]
        return result

    def _add_author_citation(self, author_id,citation_id):
        sql = text("INSERT INTO authors_citations (author_id, citation_id) \
            VALUES (:author_id, :citation_id)")
        self._db.session.execute(sql, {"author_id":author_id, "citation_id":citation_id})
        #app.db.session.commit()


    def get_all_citations(self):
        sql = text("SELECT C.id, C.type, C.title, C. journal, C.year, C.publisher, "
               "C.volume, C.pages, A.name as author_name FROM citations C "
               "LEFT JOIN authors_citations AC ON C.id = AC.citation_id "
               "LEFT JOIN authors A ON AC.author_id = A.id")

        result = self._db.session.execute(sql).fetchall()

        citations = {}
        for row in result:
            citation_id = row[0]
            if citation_id not in citations:
                citations[citation_id] = {
                "id": citation_id,
                "type": row[1],
                "title": row[2],
                "journal":row[3],
                "year": row[4],
                "publisher": row[5],
                "volume": row[6],
                "pages": row[7],
                "authors": [],
                }
            if row[8]:
                citations[citation_id]['authors'].append(row[8])
        return list(citations.values())

