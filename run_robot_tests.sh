
start-pg.sh &
cd src/flaskapp
poetry run flask run &

#while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]];
#  do sleep 1;
#done

poetry run robot src/tests
status=$?
kill $(lsof -t -i:5000)
exit $status
