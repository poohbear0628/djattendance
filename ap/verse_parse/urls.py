from django.conf.urls import url
from verse_parse import views

app_name = 'verse_parse'

urlpatterns = [
  url(r'^$', views.upload_file, name='verse_parse'),
]
