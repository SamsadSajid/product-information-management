# Generated by Django 3.1.1 on 2020-09-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0002_auto_20200903_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='softDelete',
            field=models.IntegerField(default=0),
        ),
    ]