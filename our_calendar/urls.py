from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('add/', views.HolidayAdd.as_view(), name='HolidayAdd'),
    path('edit/<int:id>', views.HolidayEdit.as_view(), name='HolidayEdit'),
    path('delete/<int:id>', views.HolidayDelete.as_view(), name='HolidayDelete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
