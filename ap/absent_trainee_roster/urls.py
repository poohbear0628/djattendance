from django.conf.urls import url
from absent_trainee_roster import views

app_name = 'absent_trainee_roster'

urlpatterns = [
  url(r'^absent_trainee_form/$', views.absent_trainee_form, name='absent_trainee_form'),
  url(r'^(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)/pdf_report$', views.pdf_report, name='pdf'),
  url(r'^email$', views.email, name='email'),
]
