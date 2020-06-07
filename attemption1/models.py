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
    actions = models.ManyToManyField(Activity, through='CompanyActivities')

    class Meta:
        managed = True
        db_table = 'company'


class CompanyActivities(models.Model):
    company = models.ForeignKey('Company', models.DO_NOTHING)
    activity = models.ForeignKey('Activity', models.DO_NOTHING)
    is_main_activity = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'company_activities'
        unique_together = (('company', 'activity'),)
