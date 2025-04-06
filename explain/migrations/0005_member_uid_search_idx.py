# Generated by Django 5.1.7 on 2025-04-04 21:01

import django.contrib.postgres.indexes
import django.db.models.functions.comparison
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explain', '0004_member_name_gin_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='member',
            index=django.contrib.postgres.indexes.GinIndex(django.contrib.postgres.indexes.OpClass(django.db.models.functions.text.Upper(django.db.models.functions.comparison.Cast('uid', output_field=models.TextField())), name='gin_trgm_ops'), name='uid_search_idx'),
        ),
    ]
