poetry run invoke run &

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]];
  do sleep 1;
done

poetry run invoke robottest

status=$?

kill $(lsof -t -i:5000)

exit $status
