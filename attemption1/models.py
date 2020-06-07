from django.db import models


class Activity(models.Model):
    okved2 = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 'activity'


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
    activities = models.ManyToManyField(Activity)

    class Meta:
        managed = True
        db_table = 'company'
