from django.http import HttpResponse
from list_org_parser.services.save_orgs_command import save_orgs, save_urls

def parse_urls(request):
    save_urls(start_page_path='list?okato=73', start_page_num=341, start_org_num=1)
    return HttpResponse('Парсер запущен')

def parse_orgs(request):
    count = save_orgs()
    return HttpResponse(f'Найдено {count} незагруженных организаций.')
