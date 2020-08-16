from django.http import HttpResponse
from classifiers.services.init_load import load_okpd2, load_okved2007, load_okved2

def okpd2(request):
    load_okpd2()
    return HttpResponse('Загрузка справочника ОКПД 2 запущена')


def okved2(request):
    load_okved2()
    return HttpResponse('Загрузка справочника ОКВЭД 2 запущена')


def okved2007(request):
    load_okved2007()
    return HttpResponse('Загрузка справочника ОКВЭД 2007 запущена')
    