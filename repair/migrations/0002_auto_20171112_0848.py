# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='id',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='receiptID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
