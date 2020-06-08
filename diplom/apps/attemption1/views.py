from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Company


def index(request):
    companies_list = Company.objects.order_by('-id')[:10]
    return render(request, 'attemption1/list.html', {'companies_list': companies_list})


def detail(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except:
        raise Http404('Компания не найдена')

    # activities = c.activity_set.order_by('okved2')

    return render(request, 'attemption1/detail.html', {'company': c}) # 'activities':activities})


def add_activity(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except:
        raise Http404('Компания не найдена')

    # c.activity_set.create(mname=request.POST['name'], okved2=request.POST['okved2'])


    return HttpResponseRedirect(reverse('attemption1:detail', args=(c.id)))
