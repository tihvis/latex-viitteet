export DATABASE_URL=postgresql://postgres:postgres@localhost:5432
export SECRET_KEY=eb2d0dfe57915dd533d1021c6dab357a

psql < schema.sql

poetry run flask --app src/flaskapp/app.py run &

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000)" != "200" ]];
  do sleep 1;
done

poetry run robot src/tests

status=$?


kill $(lsof -t -i:5000)


exit $status
