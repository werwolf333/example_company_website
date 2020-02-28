from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationFormView.as_view(), name='Registration'),
    path('login/', views.LoginFormView.as_view(), name='Login'),
    path('login/logout/', views.Logout.as_view(), name='Logout'),
]
