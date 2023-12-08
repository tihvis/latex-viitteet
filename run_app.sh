export $(xargs < .env)
poetry run flask --app src/flaskapp/app.py run --debug