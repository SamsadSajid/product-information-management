# Generated by Django 3.1.1 on 2020-09-03 16:18

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='ean',
            field=models.UUIDField(default=uuid.UUID('50e981f1-d877-41de-ac94-8204dfaec082'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='sku',
            field=models.UUIDField(default=uuid.UUID('819e9d75-dfc5-4c8e-8b02-623a77b6f558'), editable=False),
        ),
    ]
