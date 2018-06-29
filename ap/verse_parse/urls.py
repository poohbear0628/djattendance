from django.conf.urls import url
from verse_parse import views

urlpatterns = [
  url(r'^$', views.upload_file, name='verse_parse'),
]
