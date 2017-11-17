# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entry_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.TextField()),
                ('body', models.TextField()),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'modified',
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
