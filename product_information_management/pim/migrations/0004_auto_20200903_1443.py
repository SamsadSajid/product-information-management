# Generated by Django 3.1.1 on 2020-09-03 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0003_category_softdelete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='softDelete',
            new_name='isDeleted',
        ),
    ]