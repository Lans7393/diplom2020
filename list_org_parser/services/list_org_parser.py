import logging
import webbrowser
import re
import time
import requests

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class ListOrgParser:
    DOMAIN = 'https://www.list-org.com/'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/83.0.4103.61 Safari/537.36',
        'accept': '*/*'
    }

    def __init__(
            self,
            time_sleep: int = 3,
            orgs_per_page: int = 30,
        ):
        self.orgs_per_page = orgs_per_page
        self.time_sleep = time_sleep
        
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        self.browser = webbrowser.get('chrome')


    def _get_page(self, url: str) -> str:
        '''Скачивает html страницу по заданному url'''
        try:
            while True:
                response = requests.get(url, timeout=15, headers=self.HEADERS)
                response.raise_for_status() 

                # Вернулась не ожидаемая страница а страница с капчей
                if 'Проверка, что Вы не робот' in response.text:
                    logger.warning(f'CAPCHA on url:{url}')

                    self.browser.open_new_tab(url)

                    time.sleep(90) #полторы минуты на заполнение капчи
                    continue
                else:
                    logger.info(f'Get page url:{url} success!')
                    return response.text       

        except requests.RequestException as err:
            logger.error(f'RequestException url:{url} err:{str(err)}')
            return ''
            
            


    def _get_divs_dict_from_org_page(self, org_page: str) -> dict:
        soup = BeautifulSoup(org_page, 'html.parser')

        # Удаляем иконки со страницы
        for icon in soup.find_all('i', class_='fa'):
            icon.decompose()

        divs_dict = {'main': None, 'contacts': None, 'requisites': None, 'activities': None}

        for div in soup.find_all('div', class_='c2m'):
            if div.find('i', string='Полное юридическое наименование:'):
                divs_dict['main'] = div
            elif div.find('i', text=[
                    'Юридический адрес:',
                    'Адрес:',
                    'Телефон:',
                    'E-mail:',
                    'Сайт:']):
                divs_dict['contacts'] = div
            elif div.find('i', string=[
                    'ИНН:',
                    'КПП:',
                    'ОКПО:',
                    'ОГРН:',
                    'ОКТМО:',
                    'ОКФС:',
                    'ОКАТО:',
                    'ОКОПФ:']):
                divs_dict['requisites'] = div
            elif div.find('span', text=re.compile(r'.*ОКВЭД.*')):
                divs_dict['activities'] = div
                break
        return divs_dict


    def _parse_main_div(self, main_div) -> dict:
        link = main_div.find('a', class_='upper')
        return {'name': link.text}


    def _parse_postal_code(self, contacts_div):
        postal_code = contacts_div.find('i', text=re.compile('Индекс:'))
        return re.split(': ', postal_code.parent.text)[1].strip() if postal_code else None


    def _parse_address(self, contacts_div):
        address = contacts_div.find('i', string=re.compile('Адрес:'))
        return address.parent.find('span').text.strip() if address else None


    def _parse_ur_address(self, contacts_div):
        ur_address = contacts_div.find('i', string=re.compile('Юридический адрес:'))
        return ur_address.parent.find('span').text.strip() if ur_address else None


    def _parse_gps_coordinates(self, contacts_div):
        par = contacts_div.find('i', string=re.compile('GPS координаты:'))
        return [link.text.strip() for link in par.parent.find_all('a')] if par else None


    def _parse_phones(self, contacts_div):
        par = contacts_div.find('i', string=re.compile('Телефон:'))
        return [link.text.strip() for link in par.parent.find_all('a')] if par else None


    def _parse_faxes(self, contacts_div):
        par = contacts_div.find('i', string=re.compile('Факс:'))
        return [link.text.strip() for link in par.parent.find_all('a')] if par else None


    def _parse_emails(self, contacts_div):
        par = contacts_div.find('i', string=re.compile('E-mail:'))
        return [link.text.strip() for link in par.parent.find_all('a')] if par else None


    def _parse_sites(self, contacts_div):
        par = contacts_div.find('i', string=re.compile('Сайт:'))
        return [link.text.strip() for link in par.parent.find_all('a')] if par else None


    def _parse_contacts_div(self, div) -> dict:
        gps_coordinates = self._parse_gps_coordinates(div)
        if gps_coordinates:
            assert len(gps_coordinates) == 1
            gps_coordinates = gps_coordinates[0].split(',')
            assert len(gps_coordinates) == 2
            gps_coordinates = {
                'longitude': gps_coordinates[0].strip(),
                'latitude': gps_coordinates[1].strip()
            }
        return {
            'postal_code': self._parse_postal_code(div),
            'ur_address': self._parse_ur_address(div),
            'address': self._parse_address(div),
            'gps_coordinates': gps_coordinates,
            'phones': self._parse_phones(div),
            'faxes': self._parse_faxes(div),
            'emails': self._parse_emails(div),
            'sites': self._parse_sites(div),
        }


    def _parse_inn(self, requisites_div):
        label = requisites_div.find('i', string='ИНН:')
        return re.split(': ', label.parent.text)[1].strip() if label else None


    def _parse_kpp(self, requisites_div):
        label = requisites_div.find('i', string='КПП:')
        return re.split(': ', label.parent.text)[1].strip() if label else None


    def _parse_okpo(self, requisites_div):
        span = requisites_div.find('span', id='okpo')
        return span.text.strip() if span else None


    def _parse_ogrn(self, requisites_div):
        label = requisites_div.find('i', string='ОГРН:')
        return re.split(': ', label.parent.text)[1].strip() if label else None


    def _parse_okfs(self, requisites_div):
        label = requisites_div.find('i', string='ОКФС:')
        return re.findall(r'(\d+)', label.parent.text)[0].strip() if label else None


    def _parse_okogu(self, requisites_div):
        label = requisites_div.find('i', string='ОКОГУ:')
        return re.findall(r'(\d+)', label.parent.text)[0].strip() if label else None


    def _parse_okopf(self, requisites_div):
        label = requisites_div.find('i', string='ОКОПФ:')
        return re.findall(r'(\d+)', label.parent.text)[0].strip() if label else None


    def _parse_oktmo(self, requisites_div):
        label = requisites_div.find('i', string='ОКТМО:')
        return re.findall(r'(\d+)', label.parent.text)[0].strip() if label else None


    def _parse_okato(self, requisites_div):
        label = requisites_div.find('i', string='ОКАТО:')
        return label.parent.find('a').text.strip() if label else None


    def _parse_requisites_div(self, div) -> dict:
        return {
            'inn': self._parse_inn(div),
            'kpp': self._parse_kpp(div),
            'okpo': self._parse_okpo(div),
            'ogrn': self._parse_ogrn(div),
            'okfs': self._parse_okfs(div),
            'okogu': self._parse_okogu(div),
            'okopf': self._parse_okopf(div),
            'oktmo': self._parse_oktmo(div),
            'okato': self._parse_okato(div),
        }

    def _parse_main_activity(self, activities_div) -> dict:
        main_activity = {
            'okved2': None,
            'okved': None
        }

        link = activities_div.find('a', href=re.compile(r'.*/list\?okved2=.*'))
        if link:
            main_activity['okved2'] = link.text.strip()
        else:
            link = activities_div.find('a', href=re.compile(r'.*/list\?okved=.*'))
            if link:
                main_activity['okved'] = link.text.strip()

        return main_activity

    def _parse_sup_activities(self, activities_div) -> dict:
        sup_activities = {
            'okved2': [],
            'okved': []
        }

        activities_table = activities_div.find('table', class_='tt')
        a_name = None
        if activities_table:
            if activities_div.find('i', string='Дополнительные виды деятельности по ОКВЭД 2:'):
                a_name = 'okved2'
            elif activities_div.find('i', string='Дополнительные виды деятельности по ОКВЭД:'):
                a_name = 'okved'
            else:
                raise ValueError('У компании есть дополнительные виды деятельности,\
             но не ОКВЭД2 и не ОКВЭД')

            activities_table = activities_table.find_all('td', string=re.compile(r'[0-9\.]+'))
            sup_activities[a_name] = [activity.text.strip() for activity in activities_table]

        return sup_activities


    def _parse_activities_div(self, div) -> dict:
        main_activity = self._parse_main_activity(div)
        sup_activities = self._parse_sup_activities(div)
        return {
            'main_okved2': main_activity['okved2'],
            'main_okved2007': main_activity['okved'],
            'sup_okveds2': sup_activities['okved2'],
            'sup_okveds2007': sup_activities['okved'],
        }


    def _org_is_active(self, label: str) -> bool:
        return not label.find('span', class_='status_0')


    def _parse_total_orgs_count(self, orgs_list_page: str) -> int:
        '''Находит на странице со списком организаций сколько всего организаций в списке'''
        soup = BeautifulSoup(orgs_list_page, 'html.parser')
        count_string = soup.find(text=re.compile('Всего организаций'))
        return int(re.findall(r'(\d+)', count_string)[0])


    def _calc_last_page_num(self, orgs_count: int) -> int:
        import math
        return math.ceil(orgs_count / self.orgs_per_page)


    def _calc_last_org_num(self, orgs_count: int) -> int:
        return orgs_count % self.orgs_per_page


    def parse_orgs_list_page(self, orgs_list_page: str) -> list:
        '''Находит список url-адресов страниц организаций, со страницы со списком организаций'''
        soup = BeautifulSoup(orgs_list_page, 'html.parser')
        org_list = soup.find('div', class_='org_list')
        assert org_list, "Can't find div with class 'org_list'"

        orgs_labels = org_list.find_all('label')

        orgs_urls = [
            {'url': self.DOMAIN+label.find('a')['href'], 'is_active': self._org_is_active(label)}
            for label in orgs_labels
        ]

        return orgs_urls


    def parse_org_page(self, org_page: str) -> dict:
        divs_dict = self._get_divs_dict_from_org_page(org_page)

        main_div_info = self._parse_main_div(divs_dict['main'])
        contacts_div_info = self._parse_contacts_div(divs_dict['contacts'])
        requisites_div_info = self._parse_requisites_div(divs_dict['requisites'])
        activities_div_info = self._parse_activities_div(divs_dict['activities'])

        return {
            'name': main_div_info['name'],
            # Контакты
            'postal_code': contacts_div_info['postal_code'],
            'address': contacts_div_info['address'],
            'ur_address': contacts_div_info['ur_address'],
            'gps_coordinates': contacts_div_info['gps_coordinates'],
            'phones': contacts_div_info['phones'],
            'faxes': contacts_div_info['faxes'],
            'emails': contacts_div_info['emails'],
            'sites': contacts_div_info['sites'],
            # Реквизиты
            'inn': requisites_div_info['inn'],
            'kpp': requisites_div_info['kpp'],
            'okpo': requisites_div_info['okpo'],
            'ogrn': requisites_div_info['ogrn'],
            'okfs': requisites_div_info['okfs'],
            'okogu': requisites_div_info['okogu'],
            'okopf': requisites_div_info['okopf'],
            'oktmo': requisites_div_info['oktmo'],
            'okato': requisites_div_info['okato'],
            # Виды деятельности
            'main_okved2007': activities_div_info['main_okved2007'],
            'main_okved2': activities_div_info['main_okved2'],
            'sup_okveds2': activities_div_info['sup_okveds2'],
            'sup_okveds2007': activities_div_info['sup_okveds2007'],
        }

    def parse_orgs_pages(self, orgs_urls: list, only_active_orgs=False):
        orgs = []
        for org_url in orgs_urls:
            if only_active_orgs and not org_url['is_active']:
                continue
            else:
                org_page = self._get_page(org_url['url'])
                orgs += self.parse_org_page(org_page)
        return orgs


    def parse_orgs_list_pages(
            self,
            orgs_list_page_path: str,
            start_page_num: int = 1,
            start_org_num: int = 1,
            end_page_num: int = None,
            end_org_num: int = None
        ) -> list:
        orgs_list_page_url = self.DOMAIN+orgs_list_page_path
        orgs_list_page = self._get_page(orgs_list_page_url)

        orgs_count = self._parse_total_orgs_count(orgs_list_page)
        last_page_num = self._calc_last_page_num(orgs_count)
        last_org_num = self._calc_last_org_num(orgs_count)
        if not end_page_num:
            end_page_num = last_page_num
        if not end_org_num:
            end_org_num = last_org_num

        # Валидация лимитрирующих параметров
        if end_page_num > last_page_num:
            raise ValueError(f'Parametr end_page_num should be <= {last_page_num}.')
        elif end_page_num == last_page_num and end_org_num > last_org_num:
            raise ValueError(f'Parametr end_org_num should be <= {last_org_num}.')

        if start_page_num > end_page_num:
            raise ValueError(f'Parametr start_page_num should be <= {end_page_num}.')
        elif start_page_num == end_page_num and start_org_num > end_org_num:
            raise ValueError(f'Parametr start_org_num should be <= {end_org_num}.')

        # Получение списка url-адресов страниц организаций со страниц со списками организаций
        try:
            orgs_urls = []
            for orgs_list_page_num in range(start_page_num, end_page_num+1):
                url = orgs_list_page_url + '&page=' + str(orgs_list_page_num)
                orgs_list_page = self._get_page(url)

                start_org_num = start_org_num if orgs_list_page_num == start_page_num else 1
                end_org_num = end_org_num if orgs_list_page_num == end_page_num else self.orgs_per_page

                orgs_urls += self.parse_orgs_list_page(orgs_list_page)[start_org_num-1:end_org_num]

            return orgs_urls
        except Exception as e:
            logger.exception(str(e))
            return orgs_urls
    
        # frequency = 2500  # Set Frequency To 2500 Hertz
        # duration = 2000  # Set Duration To 1000 ms == 1 second
        # winsound.Beep(frequency, duration)
