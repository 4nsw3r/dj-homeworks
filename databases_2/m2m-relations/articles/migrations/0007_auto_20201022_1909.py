# Generated by Django 3.1.2 on 2020-10-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20201022_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='delete',
        ),
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
