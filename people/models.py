from django.db import models


class People(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя")
    surname = models.CharField(max_length=20, verbose_name="фамилия")
    patronymic = models.CharField(max_length=20, verbose_name="Отчество")
    position = models.CharField(max_length=20, verbose_name="Должность")
    boss = models.ForeignKey("self", blank=True, null=True, related_name='workers', on_delete=models.DO_NOTHING)
    image = models.ImageField(blank=True, upload_to='images/people/', help_text='100x100px', verbose_name='ссылка картинки')

    def __str__(self):
        return self.position + ': '+self.surname + ' '+self.name +' '+self.patronymic

    def full_name(self):
        return self.surname + ' '+self.name +' '+self.patronymic