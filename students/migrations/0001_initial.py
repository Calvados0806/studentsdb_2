# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(verbose_name="Ім'я", max_length=256)),
                ('last_name', models.CharField(verbose_name='Прізвище', max_length=256)),
                ('middle_name', models.CharField(default='', blank=True, verbose_name='По-батькові', max_length=256)),
                ('birthday', models.DateField(null=True, verbose_name='Дата народження')),
                ('photo', models.ImageField(null=True, verbose_name='Фото', blank=True, upload_to='')),
                ('ticket', models.CharField(verbose_name='Білет', max_length=256)),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
        ),
    ]
