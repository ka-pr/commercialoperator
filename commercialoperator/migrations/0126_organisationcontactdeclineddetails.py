# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-07 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        # migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commercialoperator', '0125_auto_20210902_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationContactDeclinedDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commercialoperator.OrganisationContact')),
            ],
        ),
    ]