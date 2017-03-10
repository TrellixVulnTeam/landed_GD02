# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_batches', '0005_auto_20170214_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='job',
        ),
        migrations.AddField(
            model_name='companybatch',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company_batches.Job'),
            preserve_default=False,
        ),
    ]
