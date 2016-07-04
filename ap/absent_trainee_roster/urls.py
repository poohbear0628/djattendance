from django.conf.urls import patterns, url

#from django.contrib.auth.decorators import permission_required
#from absent_trainee_roster.views import absent_trainee_form

from absent_trainee_roster import views
from absent_trainee_roster import test

urlpatterns = patterns('',
	#url(r'^absent_trainee_form/$', permission_required('is_hc')(absent_trainee_form.as_view()), name='absent_trainee_form'),
	url(r'^absent_trainee_form/$', views.absent_trainee_form, name='absent_trainee_form'),
	# url(r'^absent_trainee_form/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d+)/generate/$', views.pdf_report),
	url(r'^(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)/pdf_report$', views.pdf_report, name='pdf'),
	url(r'^email$', views.email, name='email'),
)