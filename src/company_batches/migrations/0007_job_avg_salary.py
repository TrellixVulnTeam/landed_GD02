# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_batches', '0006_auto_20170220_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='avg_salary',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
