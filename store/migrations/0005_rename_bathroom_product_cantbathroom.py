# Generated by Django 5.0.1 on 2024-01-31 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_bathroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='bathroom',
            new_name='cantBathroom',
        ),
    ]
