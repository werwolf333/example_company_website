from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'people'

urlpatterns = [
    path('', views.PeopleList.as_view(), name='People_list'),
    path('<int:id>/', views.PeopleLink.as_view(), name='People_link'),
    path('delete/<int:id>', views.PeopleDelete.as_view(), name='peopleDelete'),
    path('add', views.PeopleAdd.as_view(), name='peopleAdd'),
    path('edit/<int:id>', views.PeopleEdit.as_view(), name='peopleEdit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
