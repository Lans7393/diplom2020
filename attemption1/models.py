from django.db import models


class Activity(models.Model):
    okved2 = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.okved2 + ' ' + self.name


    class Meta:
        managed = True
        db_table = 'activity'
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'


class Product(models.Model):
    okpd2 = models.CharField(unique=True, max_length=12, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product'


class Company(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    post_index = models.CharField(max_length=64, blank=True, null=True)
    activities = models.ManyToManyField(Activity, related_name='companies')

    class Meta:
        managed = True
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
