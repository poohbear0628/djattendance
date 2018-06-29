from django.conf.urls import url
from syllabus.views import CLView, SyllabusDetailView, HomeView, DetailView, TestView, DeleteSyllabusView, AddSyllabusView, AddSessionView, DeleteSessionView
from terms.models import Term

urlpatterns = [

  url(r'^$', HomeView.as_view(model=Term), name='home-view'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/$', CLView.as_view(), name='classlist-view'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/(?P<kode>\D{0,5})/(?P<pk>\d+)$',
    DetailView.as_view(), name='detail-view'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/add_syllabus$',
    AddSyllabusView.as_view(), name='add-syllabus'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/delete/(?P<pk>\d+)$',
    DeleteSyllabusView.as_view(), name='delete-syllabus'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/(?P<kode>\D{0,5})/add_session/(?P<pk>\d+)$',
    AddSessionView.as_view(), name='add-session'),

  url(r'^(?P<term>(Fa|Sp)\d{2})/(?P<kode>\D{0,5})/(?P<syllabus_pk>\d+)/delete_session/(?P<pk>\d+)$',
    DeleteSessionView.as_view(), name='delete-session'),

  # url(r'^Term/(?P<kode>\D+)/$', DetailView.as_view(model=Syllabus), name='detail-view'),

]
