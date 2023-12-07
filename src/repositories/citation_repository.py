'''Viitteiden tallennuksesta huolehtiva moduli'''
import json
from sqlalchemy.sql import text
from entities.citation import Citation

class CitationRepository:
    """Luokka viitteiden talletusta varten"""

    def __init__(self, db) -> None:
        self._db = db

    def add_citation(self, uuid: str, citation: Citation):
        try:
            sql = text("SELECT id FROM users where uuid=:uuid")
            user_id = self._db.session.execute(sql, {"uuid":uuid}).fetchone()[0]
            data = json.dumps(citation.fields)
            sql = text("INSERT INTO citations (user_id, bibtex) VALUES (:user_id, :data)")
            self._db.session.execute(sql, {"user_id":user_id, "data": data})
            self._db.session.commit()
        except:
            return False
        return True

    def get_all_citations(self, uuid: str):
        sql = text("SELECT id FROM users where uuid=:uuid")
        user_id = self._db.session.execute(sql, {"uuid":uuid}).fetchone()[0]
        sql = text("SELECT bibtex FROM citations WHERE user_id=:user_id")
        result = self._db.session.execute(sql, {"user_id":user_id}).fetchall()
        result = [r[0] for r in result]
        return result
