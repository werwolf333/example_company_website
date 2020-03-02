# Generated by Django 3.0.3 on 2020-03-01 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('surname', models.CharField(max_length=20, verbose_name='фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('position', models.CharField(max_length=20, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, help_text='100x100px', upload_to='images/people/', verbose_name='ссылка картинки')),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workers', to='people.People')),
            ],
        ),
    ]