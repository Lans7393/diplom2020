# Generated by Django 3.1 on 2020-08-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Okpd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Наименование')),
                ('section', models.CharField(max_length=4, verbose_name='Раздел')),
                ('code', models.CharField(blank=True, default=None, max_length=16, null=True, unique=True, verbose_name='Код')),
                ('global_id', models.CharField(max_length=16, null=True, unique=True, verbose_name='Global ID')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид продукции по ОКПД 2',
                'verbose_name_plural': 'Виды продукции по ОКПД 2',
                'db_table': 'okpd2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Okved2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Наименование')),
                ('section', models.CharField(max_length=4, verbose_name='Раздел')),
                ('code', models.CharField(blank=True, default=None, max_length=16, null=True, unique=True, verbose_name='Код')),
                ('global_id', models.CharField(max_length=16, null=True, unique=True, verbose_name='Global ID')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид деятельности по ОКВЭД 2',
                'verbose_name_plural': 'Виды деятельности по ОКВЭД 2',
                'db_table': 'okved2',
                'managed': True,
            },
        ),
    ]