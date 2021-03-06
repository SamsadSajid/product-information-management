# Generated by Django 3.1.1 on 2020-09-03 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200903_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ean',
            field=models.UUIDField(default=uuid.UUID('1b412709-7179-4bd8-87bb-01e9c577c2b7'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('aca4d236-fbf1-4edd-9b78-532e84584c22'), editable=False),
        ),
    ]
