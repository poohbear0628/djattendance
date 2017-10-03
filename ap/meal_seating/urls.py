from django.conf.urls import url

from meal_seating import views

app_name = 'meal_seating'

urlpatterns = [
  url(r'^$',
    views.newseats, name='new-seats'),
  url(r'viewlist/',
    views.seattables),
  url(r'mealsignin/',
    views.signin),
  url(r'editinfo/',
    views.editinfo),
  url(r'tables/',
    views.TableListView.as_view(), name='table_edit'),
]
