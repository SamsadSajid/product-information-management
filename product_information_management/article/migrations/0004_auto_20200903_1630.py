# Generated by Django 3.1.1 on 2020-09-03 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200903_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ean',
            field=models.UUIDField(default=uuid.UUID('d4e8e5d1-aad2-4dcf-85b0-8ad25779b921'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('3df4a54b-dbbe-4389-bd0b-e2b16a7b63fd'), editable=False),
        ),
    ]
