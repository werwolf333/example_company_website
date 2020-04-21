from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('add/', views.HolidayAdd.as_view(), name='HolidayAdd'),
    path('edit/<int:id>', views.HolidayEdit.as_view(), name='HolidayEdit'),
    path('delete/<int:id>', views.HolidayDelete.as_view(), name='HolidayDelete'),
]
