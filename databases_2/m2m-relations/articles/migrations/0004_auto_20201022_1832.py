# Generated by Django 3.1.2 on 2020-10-22 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20201022_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
