#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
  ##################### Loading in env from apenv if file exists ##################
  if 'APENV' in os.environ:
    from aputils import dotenv
    env_f = os.environ['APENV']
    assert os.path.isfile(env_f), 'APENV path not set in env!'
    print('loading env file (overrides default)')
    dotenv.read_dotenv(env_f)
  else:
    print('!!! WARNING !!! No apenv file found, using bash-supplied env (default)')

  ##################### default manage.py code below #################

  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ap.settings.base")

  from django.core.management import execute_from_command_line

  execute_from_command_line(sys.argv)
