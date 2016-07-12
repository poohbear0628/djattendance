#!/bin/bash 

set -e

MIGRATIONBASE=/home/ftta-ap/migrations
VENVDIR=/home/ftta-ap/.virtualenvs/backup
DATABACK=/home/ftta-ap/db_backup
SCRIPTBACK=/home/ftta-ap/script_backup

source $VENVDIR/bin/activate

#Backup Database
cd $DATABACK
pg_dump -U postgres -a -T django_migrations djattendance > ap_data.sql
pg_dump -U postgres djattendance > ap_full.sql
pg_dump -U postgres -s djattendance > ap_schema.sql
git add -A
now=$(date +"%m_%d_%Y_%H%M%S")
git commit -am "Backup Database. Date: $now"
git push dropbox database

#Backup Scipts
cd $SCRIPTBACK
git add -A
now=$(date +"%m_%d_%Y_%H%M%S")
git commit -am "Backup scripts. Date: $now"
git push dropbox scripts
