import os
import requests
from django.conf import settings

from django.test import TestCase
from bs4 import BeautifulSoup
from list_org_parser.services.list_org_parser import ListOrgParser
from list_org_parser.services.save_orgs_command import save
from list_org_parser.models import Organization
from list_org_parser.models import Address, Phone, Fax, Email, Site
from classifiers.services.init_load import load_okved2, load_okved2007


class ListOrgParserTestCase(TestCase):
    DATA_DIR_PATH = os.path.join(settings.BASE_DIR, 'list_org_parser', 'data')
    
    ORGS_LIST_PAGE_URL = 'https://www.list-org.com/list?okato=73'
    ORGS_LIST_PAGE_PATH = os.path.join(DATA_DIR_PATH, 'test_organizations_list_page.html')
    ORGS_LIST_URLS = [
        'https://www.list-org.com//company/10608715', # 1
        'https://www.list-org.com//company/10588576', # 2
        'https://www.list-org.com//company/12131152', # 3
        'https://www.list-org.com//company/12133320', # 4
        'https://www.list-org.com//company/10662109', # 5
        'https://www.list-org.com//company/10305733', # 6
        'https://www.list-org.com//company/12131434', # 7
        'https://www.list-org.com//company/10550991', # 8
        'https://www.list-org.com//company/12153692', # 9
        'https://www.list-org.com//company/12133336', # 10
        'https://www.list-org.com//company/12132793', # 11
        'https://www.list-org.com//company/10779233', # 12
        'https://www.list-org.com//company/10431945', # 13
        'https://www.list-org.com//company/10431948', # 14
        'https://www.list-org.com//company/12130737', # 15
        'https://www.list-org.com//company/10557430', # 16
        'https://www.list-org.com//company/11507495', # 17
        'https://www.list-org.com//company/10319862', # 18
        'https://www.list-org.com//company/10080857', # 19
        'https://www.list-org.com//company/11236461', # 20
        'https://www.list-org.com//company/10817611', # 21
        'https://www.list-org.com//company/10678840', # 22
        'https://www.list-org.com//company/12135553', # 23
        'https://www.list-org.com//company/10203581', # 24
        'https://www.list-org.com//company/12137123', # 25
        'https://www.list-org.com//company/12137133', # 26
        'https://www.list-org.com//company/12132985', # 27
        'https://www.list-org.com//company/12131427', # 28
        'https://www.list-org.com//company/11077103', # 29
        'https://www.list-org.com//company/12149729'] # 30

    ORG_DICT = {
        'name': 'Общество с ограниченной ответственностью "Ульяновскхлебпром"',
        'postal_code': '432063',
        'address': 'Г УЛЬЯНОВСК,УЛ ХЛЕБОЗАВОДСКАЯ, Д 3',
        'gps_coordinates': {'longitude':'54.304437', 'latitude':'48.37073'},
        'ur_address': '432017, УЛЬЯНОВСКАЯ ОБЛАСТЬ, ГОРОД УЛЬЯНОВСК, УЛИЦА ХЛЕБОЗАВОДСКАЯ, 3',
        'phones': ['8 (8422) 32-60-54', '8 (8422) 32-25-84'],
        'faxes': ['32-25-84'],
        'emails': ['info@up.ulhp.ru'],
        'sites': ['www.hlebprom.mv.ru'],
        'inn': '7326038108',
        'kpp': '732601001',
        'okpo': '00371334',
        'ogrn': '1117326000010',
        'okfs': '16',
        'okogu': '4210008',
        'okopf': '12300',
        'oktmo': '73701000001',
        'okato': '73401365',
        'main_okved2007': None,
        'main_okved2': '10.71',
        'sup_okveds2': [],
        'sup_okveds2007': [
            '10.13.1', '10.13.2',
            '10.13.3', '10.13.4',
            '10.13.5', '10.13.6',
            '10.13.7', '41.20',
            '47.11', '47.11.1',
            '47.25', '47.9',
            '49.4', '49.41.1',
            '52.29', '56.10',
            '56.10.1', '56.10.3',
            '56.29', '68.10',
            '68.20.1', '68.20.2'
        ]
    }

    ORG_PAGE_URL = 'https://www.list-org.com/company/7121'
    ORG_PAGE_PATH = os.path.join(DATA_DIR_PATH, 'test_organization_page.html')


    def _delete_dinamic_content(self, page):
        soup = BeautifulSoup(page, 'html.parser')

        for adv in soup.find_all('ins', class_='adsbygoogle'):
            adv.decompose()
        
        for script in soup.find_all('script'):
            script.decompose()

        return str(soup)


    def _save_to_file(self, file_name: str, content: str):
        file = open(os.path.join(self.DATA_DIR_PATH, file_name), encoding='utf-8', mode='w')
        file.write(content)
        file.close()


    def _get_page(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/83.0.4103.61 Safari/537.36',
            'accept': '*/*'
        }
        response = requests.get(url=url, headers=headers)
        self.assertEqual(response.status_code, 200)
        return response.text


    def _update_test_files(self):
        self._save_to_file(self.ORG_PAGE_PATH, self._get_page(self.ORG_PAGE_URL))
        self._save_to_file(self.ORGS_LIST_PAGE_PATH, self._get_page(self.ORGS_LIST_PAGE_URL))


    def _init_pages(self):
        self.org_page = open(self.ORG_PAGE_PATH, encoding='utf-8', mode='r').read()
        self.orgs_list_page = open(self.ORGS_LIST_PAGE_PATH, encoding='utf-8', mode='r').read()

    def _init_classifiers(self):
        load_okved2()
        load_okved2007()

    def setUp(self):
        try:
            self._init_pages()
        except FileNotFoundError:
            self._update_test_files()
            self._init_pages()
        self._init_classifiers()


    def test_total_orgs_count_parser(self):
        parser = ListOrgParser()
        self.assertEqual(10228, parser._parse_total_orgs_count(self.orgs_list_page))


    def test_orgs_list_page_parser(self):
        parser = ListOrgParser()
        urls = [org_url['url'] for org_url in parser.parse_orgs_list_page(self.orgs_list_page)]
        self.assertEqual(self.ORGS_LIST_URLS, urls)


    def test_org_page_parser(self):
        parser = ListOrgParser()
        org_dict = parser.parse_org_page(self.org_page)
        self.assertEqual(self.ORG_DICT, org_dict)


    def test_save(self):
        org = save(self.ORG_DICT)
        org_from_db = Organization.objects.get(name=self.ORG_DICT['name'])
        self.assertEqual(org, org_from_db)
        self.assertEqual(self.ORG_DICT['name'], org.name)
        self.assertEqual(self.ORG_DICT['postal_code'], org.postal_code)

        address = Address.objects.get(organization=org, is_legal=False)
        self.assertEqual(self.ORG_DICT['address'], address.address)
        self.assertEqual(self.ORG_DICT['gps_coordinates'], {'longitude': address.gps_longitude, 'latitude': address.gps_latitude})
        self.assertEqual(self.ORG_DICT['ur_address'], Address.objects.get(organization=org, is_legal=True).address)

        self.assertEqual(self.ORG_DICT['phones'], list(Phone.objects.filter(organization=org).values_list('phone', flat=True)))
        self.assertEqual(self.ORG_DICT['faxes'], list(Fax.objects.filter(organization=org).values_list('fax', flat=True)))
        self.assertEqual(self.ORG_DICT['emails'], list(Email.objects.filter(organization=org).values_list('email', flat=True)))
        self.assertEqual(self.ORG_DICT['sites'], list(Site.objects.filter(organization=org).values_list('site', flat=True)))

        self.assertEqual(self.ORG_DICT['inn'], org.inn)
        self.assertEqual(self.ORG_DICT['kpp'], org.kpp)
        self.assertEqual(self.ORG_DICT['okpo'], org.okpo)
        self.assertEqual(self.ORG_DICT['ogrn'], org.ogrn)
        self.assertEqual(self.ORG_DICT['okfs'], org.okfs)
        self.assertEqual(self.ORG_DICT['okogu'], org.okogu)
        self.assertEqual(self.ORG_DICT['oktmo'], org.oktmo)
        self.assertEqual(self.ORG_DICT['okato'], org.okato)

        self.assertEqual(self.ORG_DICT['main_okved2007'], org.main_okved2007.code if org.main_okved2007 else None)
        self.assertEqual(self.ORG_DICT['sup_okveds2'], [okved2007.code for okved2007 in org.sup_okveds2007.all()])

        self.assertEqual(self.ORG_DICT['main_okved2'], org.main_okved2.code if org.main_okved2 else None)
        self.assertEqual(set(self.ORG_DICT['sup_okveds2007']), set([okved2.code for okved2 in org.sup_okveds2.all()]))
        
        
        
