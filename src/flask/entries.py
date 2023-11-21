import app
from sqlalchemy.sql import text

def add_book(authors, title, publisher, year, isbn):
    sql = text("INSERT INTO citations (title,publisher,year,isbn) VALUES (:title, :publisher, :year, :isbn) RETURNING id")
    citation_id = app.db.session.execute(sql, {"title":title, "publisher":publisher, "year":year, "isbn":isbn}).fetchone()[0]
    
    author_ids = []
    for author in authors.splitlines():
        author_ids.append(_add_author(author))
    for author_id in author_ids:
        _add_author_citation(author_id, citation_id)


def _add_author(name):
    sql = text("INSERT INTO authors (name) VALUES (:name) ON CONFLICT DO NOTHING RETURNING ID")
    result = app.db.session.execute(sql, {"name": name}).fetchone()[0]
    return result
    
    
def _add_author_citation(author_id,citation_id):
    sql = text("INSERT INTO authors_citations (author_id, citation_id) VALUES (:author_id, :citation_id)")
    app.db.session.execute(sql, {"author_id":author_id, "citation_id":citation_id})
    app.db.session.commit()