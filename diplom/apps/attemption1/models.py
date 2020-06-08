from django.db import models


class Activity(models.Model):
    okved2 = models.CharField('ОКВЕД2', max_length=12, blank=True, null=True)
    name = models.CharField('Наименование', max_length=512)

    def __str__(self):
        return self.okved2 + ' ' + self.name


    class Meta:
        managed = True
        db_table = 'activity'
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'


class Product(models.Model):
    okpd2 = models.CharField('ОКПД2', unique=True, max_length=12, blank=True, null=True)
    name = models.CharField('Наименование', max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'product'


class Company(models.Model):
    name = models.CharField('Название', max_length=256, blank=True, null=True)
    short_name = models.CharField('Короткое название', max_length=64, blank=True, null=True)
    address = models.CharField('Адрес', max_length=512, blank=True, null=True)
    postal_code = models.CharField('Почтовый индех', max_length=64, blank=True, null=True)
    activities = models.ManyToManyField(Activity, related_name='companies')

    def __str__(self):
        return self.short_name

    class Meta:
        managed = True
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
