# Generated by Django 3.1.1 on 2020-09-03 20:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0008_delete_article'),
        ('article', '0011_auto_20200903_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(null=True, to='pim.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ean',
            field=models.UUIDField(default=uuid.UUID('96b20846-6b7e-4759-8aa4-5afb9ba03860'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('e4bac3a0-25f1-4042-8b16-767afcad1925'), editable=False),
        ),
    ]
