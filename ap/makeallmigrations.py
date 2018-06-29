from django.conf import settings
import os

if __name__ == '__main__':
  ##################### Loading in env from apenv if file exists ##################
  if 'APENV' in os.environ:
    from aputils import dotenv
    env_f = os.environ['APENV']
    assert os.path.isfile(env_f), 'APENV path not set in env!'
    print('loading env file (overrides default)')
    dotenv.read_dotenv(env_f)
  else:
    print('!!! WARNING !!! No apenv file found, using bash-supplied env (default)')

  ##################### default makeallmigrations.py code below #################
  apps = ' '.join([ app for app in settings.INSTALLED_APPS if not 'django' in app and not '.' in app ])
  print('Running make migrations on: ', apps)
  print('--------------------')

  os.system(os.path.join(settings.SITE_ROOT, 'manage.py') + ' makemigrations ' + apps)
