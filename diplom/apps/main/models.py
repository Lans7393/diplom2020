from django.db import models
from phone_field import PhoneField


class Okved(models.Model):
    okved = models.CharField('ОКВЭД', max_length=12, blank=True, null=True)
    okved2 = models.CharField('ОКВЭД2', max_length=12, blank=True, null=True, unique=True)
    name = models.CharField('Наименование', max_length=512)

    def __str__(self):
        return self.okved2 + ' ' + self.name

    class Meta:
        managed = True
        db_table = 'okved'
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'


class Okpd(models.Model):
    okpd2 = models.CharField('ОКПД2', unique=True, max_length=12, blank=True, null=True)
    name = models.CharField('Наименование', max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'okpd'


class Company(models.Model):
    name = models.CharField('Название', max_length=256, blank=True, null=True)
    short_name = models.CharField('Короткое название', max_length=64, blank=True, null=True)

    inn = models.CharField('ИНН', max_length=12, blank=True, null=True)
    kpp = models.CharField('КПП', max_length=32, blank=True, null=True)
    okpo = models.CharField('ОКПО', max_length=32, blank=True, null=True)
    ogrn = models.CharField('ОГРН', max_length=32, blank=True, null=True)
    okfs = models.CharField('ОКФС', max_length=32, blank=True, null=True)
    okopf = models.CharField('ОКОПФ', max_length=32, blank=True, null=True)
    oktmo = models.CharField('ОКТМО', max_length=32, blank=True, null=True)
    okato = models.CharField('ОКАТО', max_length=32, blank=True, null=True)
    okogu = models.CharField('ОКОГУ', max_length=32, blank=True, null=True)

    main_okved = models.ForeignKey(Okved, on_delete=models.DO_NOTHING, null=True, blank=True)
    sup_okveds = models.ManyToManyField(Okved, related_name='companies', blank=True)

    list_org_link = models.URLField('Ссылка на list-org.com', null=True, blank=True)

    def __str__(self):
        return self.short_name if self.short_name else self.name

    class Meta:
        managed = True
        db_table = 'company'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Address(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)

    postal_code = models.CharField('Почтовый индех', max_length=64, blank=True, null=True)
    federal_subject = models.CharField('Субъект федерации', max_length=128, blank=True, null=True)
    locality = models.CharField('Населенный пункт', max_length=128, blank=True, null=True)
    street = models.CharField('Улица', max_length=256, blank=True, null=True)
    remain = models.CharField('Номер дома, квартиры, строения и т.п.', max_length=256, blank=True, null=True)
    gps_coordinates = models.CharField('GPS координаты', max_length=32, blank=True, null=True)
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)
    is_legal = models.BooleanField('Юридический адрес', default=False)

    class Meta:
        managed = True
        db_table = 'address'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Phone(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    phone = PhoneField('Телефон', blank=True, null=False, help_text='Номер телефона')
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'phone'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Fax(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    fax = PhoneField('Факс', blank=True, null=False, help_text='Номер факса')
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fax'
        verbose_name = 'Факс'
        verbose_name_plural = 'Факсы'


class Email(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    email = models.EmailField('E-mail', blank=True, null=False, help_text='E-mail')
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'email'
        verbose_name = 'E-mail'


class Site(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    site = models.URLField('Сайт', null=False, blank=True, help_text='Сайт')
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'site'
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'