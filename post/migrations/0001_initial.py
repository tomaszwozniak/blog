# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=64)),
                ('value', models.TextField(help_text='Please be nice')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(null=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tags', models.CharField(max_length=200, null=True, verbose_name='Related tags', blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='post.Post'),
        ),
    ]
