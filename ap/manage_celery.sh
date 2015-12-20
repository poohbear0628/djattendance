#this script needs to be run with sudo
rabbitmq-server -detached
python ap/manage.py celeryd --verbosity=2 --loglevel=DEBUG --settings=ap.settings.dev &

python ap/manage.py celerybeat --verbosity=2 --loglevel=DEBUG --settings=ap.settings.dev &