#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
parentdir="$(dirname "$DIR")"

start() {
  echo "#### Starting rabbitmq-server, celeryd, and celerybeat. You can stop with 'stop' or tail logs with 'status'."
  #this script needs to be run with sudo
  sudo rabbitmq-server -detached

  sudo -k

  nohup python $DIR/manage.py celeryd --verbosity=2 --loglevel=DEBUG --settings=ap.settings.dev > $parentdir/celeryd.log &

  nohup python $DIR/manage.py celerybeat --verbosity=2 --loglevel=DEBUG --settings=ap.settings.dev > $parentdir/celerybeat.log &
}

stop() {
  echo "#### Killing all celeryd, celerybeat and rabbitmq-server processes"
  sudo rabbitmqctl stop;

  nohup ps aux | grep celery | awk '{system("sudo kill -9 " $2)}' &

  nohup ps aux | grep rabbit | awk '{system("sudo kill -9 " $2)}' &

  echo "Finished killing all the threads!"

}

status() {
  tail -f $parentdir/nohup.out $parentdir/celery.log $parentdir/celeryd.log $parentdir/celerybeat.log
}

threads() {
  echo "All the threads running:"
  ps aux | grep rabbit;
  ps aux | grep celery;
}

args() {
  printf "%s" options:
  while getopts a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:z: OPTION "$@"; do
    printf " -%s '%s'" $OPTION $OPTARG
  done
  shift $((OPTIND - 1))
  printf "arg: '%s'" "$@"
  echo
}

if [[ $1 =~ ^(start|stop|status|threads|args)$ ]]; then
  "$@"
else
  echo "Invalid subcommand $1" >&2
  echo "Usage:"
  echo "    manage_celery.sh start      Start all processes."
  echo "    manage_celery.sh stop       Kill all processes."
  echo "    manage_celery.sh status     Tails all the log files."
  echo "    manage_celery.sh threads    Lists all the processes running."
  exit 1
fi







