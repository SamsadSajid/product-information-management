# Generated by Django 3.1.1 on 2020-09-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0005_auto_20200903_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.UUIDField(editable=False)),
                ('ean', models.UUIDField(editable=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('stock_quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]