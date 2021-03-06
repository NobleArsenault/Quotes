# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('functionalapplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='cite',
            name='favoriter',
        ),
        migrations.AddField(
            model_name='favorites',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_message', to='functionalapplication.cite'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user_who_favorited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_can_favorite', to='login.User'),
        ),
    ]
