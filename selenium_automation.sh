#!/usr/bin/env bash

# use the prod settings
cd ap
python makeallmigrations.py --settings=ap.settings.prod
python manage.py migrate --settings=ap.settings.prod

# create a super user
echo "super user creation(selenium)"
echo "from accounts.models import User; User.objects.filter(email='ap_test@gmail.com').delete(); User.objects.create_superuser('ap_test@gmail.com', 'ap')" | python manage.py shell

# populate initial data
python manage.py populate_testers --settings=ap.settings.prod
python manage.py populate_events --settings=ap.settings.prod
python manage.py populate_terms --settings=ap.settings.prod

# run the server
echo "run the server(selenium)"
python manage.py runserver --settings=ap.settings.prod &
echo "loading..."
sleep 30

# run the regression
###  MAKE SURE THAT YOU HAVE ADDED ENV VARIABLES FOR SAUCELAB IN TRAVIS SETTINGS! ###
echo "run the selenium via saucelab"
cd ../../; ls .; mkdir saucelab; cd saucelab
git clone -b automation https://github.com/attendanceproject/djattendance.git
cd djattendance/selenium/automation
python run_regression.py

