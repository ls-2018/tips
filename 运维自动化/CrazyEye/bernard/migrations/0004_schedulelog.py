# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-14 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bernard', '0003_auto_20170210_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(0, 'failed'), (1, 'success'), (2, 'error'), (3, 'running')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bernard.Plan')),
            ],
        ),
    ]
