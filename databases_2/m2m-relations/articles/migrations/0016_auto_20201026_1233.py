# Generated by Django 3.1.2 on 2020-10-26 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20201026_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='scope_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scp_name', to='articles.articlescope', verbose_name='Название'),
        ),
    ]
