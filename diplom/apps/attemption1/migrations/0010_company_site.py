# Generated by Django 3.0.7 on 2020-06-08 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attemption1', '0009_auto_20200609_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Сайт компании'),
        ),
    ]