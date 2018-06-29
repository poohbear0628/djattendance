from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .groups import add_group_permissions

class AputilsConfig(AppConfig):
  name = 'aputils'
  verbose_name = 'aputils'

  def ready(self):
    post_migrate.connect(add_group_permissions, sender=self)
