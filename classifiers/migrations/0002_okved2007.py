# Generated by Django 3.1 on 2020-08-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okved2007',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Наименование')),
                ('section', models.CharField(max_length=4, verbose_name='Раздел')),
                ('subsection', models.CharField(max_length=4, verbose_name='Подраздел')),
                ('index', models.IntegerField(verbose_name='Индекс')),
                ('code', models.CharField(blank=True, default=None, max_length=16, null=True, unique=True, verbose_name='Код')),
                ('global_id', models.CharField(max_length=16, null=True, unique=True, verbose_name='Global ID')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид деятельности по ОКВЭД 2007',
                'verbose_name_plural': 'Виды деятельности по ОКВЭД 2007',
                'db_table': 'okved2007',
                'managed': True,
            },
        ),
    ]
