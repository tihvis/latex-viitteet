poetry run python3 start-pg.sh &
poetry run python3 src/flask/ &

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001/ping)" != "200" ]];
  do sleep 1;
done

poetry run robot src/tests
status=$?
kill $(lsof -t -i:5001)
exit $status
