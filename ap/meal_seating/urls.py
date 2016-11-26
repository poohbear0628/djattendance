from django.conf.urls import patterns, url

from meal_seating import views

urlpatterns = patterns('',
    url(r'newseating/',
        views.newseats),
    url(r'viewlist/',
        views.seattables),
    url(r'mealsignin/',
        views.signin),
    url(r'editinfo/',
        views.editinfo),
    url(r'tables/', 
        views.TableListView.as_view(), name='table_edit'),
    url(r'trainees/', 
        views.TraineeExclusionListView.as_view(), name='trainee_edit'),
)
