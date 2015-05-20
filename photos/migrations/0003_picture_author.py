# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_picture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='author',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
