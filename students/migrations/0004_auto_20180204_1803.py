# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Назва', max_length=256)),
                ('date', models.DateTimeField(verbose_name='Час проведення')),
                ('professor', models.CharField(verbose_name='Викладач', max_length=256)),
            ],
            options={
                'verbose_name': 'Екзамен',
                'verbose_name_plural': 'Екзамени',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='group_exam',
            field=models.ManyToManyField(to='students.Exam', verbose_name='Екзамен'),
        ),
    ]
