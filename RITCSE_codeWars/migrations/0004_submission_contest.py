# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RITCSE_codeWars', '0003_auto_20160809_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='contest',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='RITCSE_codeWars.Contest'),
            preserve_default=False,
        ),
    ]
