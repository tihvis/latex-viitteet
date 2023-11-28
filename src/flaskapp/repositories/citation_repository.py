from sqlalchemy.sql import text
import json
from entities.citation import Citation


class CitationRepository:
    """Luokka viitteiden talletusta varten"""

    def __init__(self, db) -> None:
        self._db = db

    def add_citation(self, citation: Citation):
        try:
            data = json.dumps(citation.fields)
            sql = text("INSERT INTO citations (bibtex) VALUES (:data)")
            self._db.session.execute(sql, {"data": data})
            self._db.session.commit()
        except:
            return False
        return True

    def get_all_citations(self):
        sql = text("SELECT bibtex FROM citations")
        result = self._db.session.execute(sql).fetchall()
        result = [r[0] for r in result]
        print(result)
        return result
