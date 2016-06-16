# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('can_rock', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'band',
                'verbose_name_plural': 'bands',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name="Member's name", max_length=200)),
                ('instrument', models.CharField(choices=[('g', 'Guitar'), ('b', 'Bass'), ('d', 'Drums'), ('v', 'Vocal'), ('p', 'Piano')], max_length=1)),
                ('band', models.ForeignKey(related_name='band', to='bands.Band')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
    ]
