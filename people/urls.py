from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleList.as_view(), name='People_list'),
]