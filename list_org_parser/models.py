from django.utils.timezone import now
from django.db import models
from phone_field import PhoneField
from classifiers.models import Okved2, Okved2007

class OrganizationUrl(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = True
        db_table = 'organization_url'
        verbose_name = 'URL организации'


class Organization(models.Model):
    name = models.CharField('Название', max_length=256, null=True, blank=True)
    short_name = models.CharField('Короткое название', max_length=64, null=True, blank=True)
    postal_code = models.CharField('Почтовый индекс', max_length=16, null=True, blank=True)

    inn = models.CharField('ИНН', max_length=12, null=True, blank=True)
    kpp = models.CharField('КПП', max_length=32, null=True, blank=True)
    okpo = models.CharField('ОКПО', max_length=32, null=True, blank=True)
    ogrn = models.CharField('ОГРН', max_length=32, null=True, blank=True)
    okfs = models.CharField('ОКФС', max_length=32, null=True, blank=True)
    okopf = models.CharField('ОКОПФ', max_length=32, null=True, blank=True)
    oktmo = models.CharField('ОКТМО', max_length=32, null=True, blank=True)
    okato = models.CharField('ОКАТО', max_length=32, null=True, blank=True)
    okogu = models.CharField('ОКОГУ', max_length=32, null=True, blank=True)

    main_okved2 = models.ForeignKey(Okved2, on_delete=models.DO_NOTHING, null=True, blank=True)
    sup_okveds2 = models.ManyToManyField(Okved2, related_name='organizations', blank=True)
    main_okved2007 = models.ForeignKey(Okved2007, on_delete=models.DO_NOTHING, null=True, blank=True)
    sup_okveds2007 = models.ManyToManyField(Okved2007, related_name='organizations', blank=True)

    list_org_link = models.OneToOneField(OrganizationUrl, on_delete=models.DO_NOTHING, null=True, blank=True)
    create_date = models.DateTimeField(blank=True, default=now)

    def __str__(self):
        return self.short_name if self.short_name else self.name

    class Meta:
        managed = True
        db_table = 'organization'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Address(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.CharField('Адрес', max_length=1024, null=False, blank=False)
    is_legal = models.BooleanField('Юридический', null=False, blank=True, default=False)
    gps_longitude = models.CharField('Долгота', max_length=16, null=True, blank=True, default=None)
    gps_latitude = models.CharField('Широта', max_length=16, null=True, blank=True, default=None)
    comment = models.CharField('Комментарий', max_length=256, null=True, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

class Phone(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True, blank=True)
    phone = PhoneField('Телефон', blank=True, null=False, help_text='Номер телефона')
    comment = models.CharField('Комментарий', max_length=256, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'phone'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Fax(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True, blank=True)
    fax = PhoneField('Факс', blank=True, null=False, help_text='Номер факса')
    comment = models.CharField('Комментарий', max_length=256, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'fax'
        verbose_name = 'Факс'
        verbose_name_plural = 'Факсы'


class Email(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.EmailField('E-mail', blank=True, null=False, help_text='E-mail')
    comment = models.CharField('Комментарий', max_length=256, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'email'
        verbose_name = 'E-mail'


class Site(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True, blank=True)
    site = models.URLField('Сайт', null=False, blank=True, help_text='Сайт')
    comment = models.CharField('Комментарий', max_length=256, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'site'
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'