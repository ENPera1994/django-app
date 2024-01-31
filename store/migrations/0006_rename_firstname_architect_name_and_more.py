# Generated by Django 5.0.1 on 2024-01-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_bathroom_product_cantbathroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architect',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='architect',
            name='country',
        ),
        migrations.RemoveField(
            model_name='architect',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='architect',
            name='province',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='architect',
            name='experience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='architect',
            name='positions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='architect',
            name='qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
