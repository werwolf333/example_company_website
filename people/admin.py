from django.contrib import admin
from .models import People


class PeopleAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'patronymic', 'position', 'boss', 'image']


admin.site.register(People, PeopleAdmin)
