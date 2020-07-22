# Generated by Django 3.0.7 on 2020-06-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attemption1', '0012_auto_20200616_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okved', models.CharField(blank=True, max_length=12, null=True, verbose_name='ОКВЭД')),
                ('okved2', models.CharField(blank=True, max_length=12, null=True, verbose_name='ОКВЭД2')),
                ('name', models.CharField(max_length=512, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид деятельности',
                'verbose_name_plural': 'Виды деятельности',
                'db_table': 'okved',
                'managed': True,
            },
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Okpd',
        ),
        migrations.RemoveField(
            model_name='company',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='company',
            name='main_activity',
        ),
        migrations.AddField(
            model_name='address',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Company'),
        ),
        migrations.AddField(
            model_name='address',
            name='is_legal',
            field=models.BooleanField(default=False, verbose_name='Юридический адрес'),
        ),
        migrations.AddField(
            model_name='company',
            name='kpp',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='КПП'),
        ),
        migrations.AddField(
            model_name='company',
            name='ogrn',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОГРН'),
        ),
        migrations.AddField(
            model_name='company',
            name='okato',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AddField(
            model_name='company',
            name='okfs',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКФС'),
        ),
        migrations.AddField(
            model_name='company',
            name='okogu',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКОГУ'),
        ),
        migrations.AddField(
            model_name='company',
            name='okopf',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКОПф'),
        ),
        migrations.AddField(
            model_name='company',
            name='okpo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКПО'),
        ),
        migrations.AddField(
            model_name='company',
            name='oktmo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='email',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Company'),
        ),
        migrations.AlterField(
            model_name='fax',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Company'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Company'),
        ),
        migrations.AlterField(
            model_name='site',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Company'),
        ),
        migrations.AlterModelTable(
            name='okpd',
            table='okpd',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AddField(
            model_name='company',
            name='main_okved',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attemption1.Okved'),
        ),
        migrations.AddField(
            model_name='company',
            name='sup_okveds',
            field=models.ManyToManyField(blank=True, related_name='companies', to='attemption1.Okved'),
        ),
    ]