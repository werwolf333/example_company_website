from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleList.as_view(), name='People_list'),
    path('<int:id>/', views.PeopleLink.as_view(), name='People_link'),
    path('delete/<int:id>', views.PeopleDelete.as_view(), name='peopleDelete'),
    path('add', views.PeopleAdd.as_view(), name='peopleAdd'),

]