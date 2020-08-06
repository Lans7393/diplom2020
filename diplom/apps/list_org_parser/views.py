from django.conf import settings
from django.http import HttpResponse
from apps.list_org_parser.services import ListOrgParser

def parse_companies_from_list_org(request):
    parser_path = os.path.join(settings.PROJECT_ROOT, 'csv', 'companies.csv')
    parser = ListOrgParser()
    parser.parse(companies_list_page_path='list?okato=73', end_page=10, end_number=30, only_active=False)
    return HttpResponse(html)
