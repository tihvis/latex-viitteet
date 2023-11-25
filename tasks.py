from os import getenv
from invoke.tasks import task
from sqlalchemy import create_engine, text

@task
def init_db(ctx):
    engine = create_engine("postgresql://postgres:postgres@localhost:5432")
    with engine.begin() as cursor:
        cursor.execute(text(open("schema.sql", "r").read()))

#@task
#def run(ctx):
#    ctx.run("python src/flaskapp/app.py")

#@task
#def robot_test(ctx):
#    ctx.run("robot ./src/tests")

