# Generated by Django 5.0.1 on 2024-01-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=99.99),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(default=1),
        ),
    ]