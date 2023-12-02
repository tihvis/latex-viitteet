export DATABASE_URL=postgresql:///$USER
export SECRET_KEY=eb2d0dfe57915dd533d1021c6dab357a


poetry run flask --app src/flaskapp/app.py run