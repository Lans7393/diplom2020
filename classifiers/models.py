from django.db import models

class Okved2(models.Model):
    '''Общероссийский классификатор видов экономической деятельности ОКВЭД 2 (ОК 029-2014 (КДЕС Ред. 2))'''
    name = models.CharField('Наименование', max_length=512, null=False, blank=False)
    section = models.CharField('Раздел', max_length=4, null=False, blank=False)
    code = models.CharField('Код', unique=True, max_length=16, null=True, blank=True, default=None)
    global_id = models.CharField('Global ID', unique=True, max_length=16, null=True, blank=False)
    description = models.TextField('Описание', null=True, blank=True, default='')

    def __str__(self):
        return self.code + ' ' + self.name

    class Meta:
        managed = True
        db_table = 'okved2'
        verbose_name = 'Вид деятельности по ОКВЭД 2'
        verbose_name_plural = 'Виды деятельности по ОКВЭД 2'


class Okved2007(models.Model):
    '''Общероссийский классификатор видов экономической деятельности 2007 (ОКВЭД 2007)'''
    name = models.CharField('Наименование', max_length=512, null=False, blank=False)
    section = models.CharField('Раздел', max_length=4, null=False, blank=False)
    subsection = models.CharField('Подраздел', max_length=4, null=False, blank=False)
    index = models.IntegerField('Индекс', null=False, blank=False)
    code = models.CharField('Код', unique=True, max_length=16, null=True, blank=True, default=None)
    global_id = models.CharField('Global ID', unique=True, max_length=16, null=True, blank=False)
    description = models.TextField('Описание', null=True, blank=True, default='')

    def __str__(self):
        return self.code + ' ' + self.name

    class Meta:
        managed = True
        db_table = 'okved2007'
        verbose_name = 'Вид деятельности по ОКВЭД 2007'
        verbose_name_plural = 'Виды деятельности по ОКВЭД 2007'


class Okpd2(models.Model):
    '''Общероссийский классификатор продукции по видам экономической деятельности ОКПД 2 (ОК 034-2014 (КПЕС 2008))'''
    name = models.CharField('Наименование', max_length=512, null=False, blank=False)
    section = models.CharField('Раздел', max_length=4, null=False, blank=False)
    code = models.CharField('Код', unique=True, max_length=16, null=True, blank=True, default=None)
    global_id = models.CharField('Global ID', unique=True, max_length=16, null=True, blank=False)
    description = models.TextField('Описание', null=True, blank=True, default='')

    class Meta:
        managed = True
        db_table = 'okpd2'
        verbose_name = 'Вид продукции по ОКПД 2'
        verbose_name_plural = 'Виды продукции по ОКПД 2'
        