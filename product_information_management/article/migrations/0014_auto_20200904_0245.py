# Generated by Django 3.1.1 on 2020-09-04 02:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20200903_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ean',
            field=models.UUIDField(default=uuid.UUID('ef6c88a0-c439-4007-b19d-fcdbbe947894'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('c12f7b48-18d2-416c-9b8a-bb3be0544be3'), editable=False),
        ),
    ]
