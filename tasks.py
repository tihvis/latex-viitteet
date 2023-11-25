from invoke.tasks import task
from src.flaskapp.app import db

@task
def init_db(ctx):
    with db.session() as cursor:
        cursor.execute(open("schema.sql", "r").read())