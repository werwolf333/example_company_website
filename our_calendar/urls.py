from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('add/', views.HolidayAdd.as_view(), name='HolidayAdd'),
]
