import logging

from bulk_sync import bulk_sync

from list_org_parser.services.list_org_parser import ListOrgParser
from list_org_parser.models import OrganizationUrl, Organization
from list_org_parser.models import Address, Phone, Fax, Email, Site

logger = logging.getLogger(__name__)

def save_urls(start_page_path: str, start_page_num: int = 1, start_org_num: int = 1, end_page_num: int = None, end_org_num=None):
    parser = ListOrgParser()
    try:
        orgs_urls = parser.parse_orgs_list_pages(
            orgs_list_page_path=start_page_path,
            start_page_num=start_page_num,
            start_org_num=start_org_num,
            end_page_num=end_page_num,
            end_org_num=end_org_num
        )
        orgs_urls = [OrganizationUrl(**org_url) for org_url in orgs_urls]
        ret = bulk_sync(new_models=orgs_urls, filters=[], key_fields=('url',), skip_deletes=True)
    except Exception as e:
        logger.exception(str(e))
    else:
        logger.info("Results of bulk_sync: {created} created, {updated} updated, {deleted} deleted.".format(**ret['stats']))


def save_orgs():
    parser = ListOrgParser()
    loaded_ids = Organization.objects.values_list('list_org_link', flat=True)
    urls = OrganizationUrl.objects.filter(is_active=True).exclude(id__in=loaded_ids)
    try:
        orgs = parser.parse_orgs_pages(urls)
        for org in orgs:
            save(org)
    except Exception as e:
        logger.exception(str(e))
    else:
        return len(orgs)


def save(org: dict):
    address = org.pop('address')
    gps_coordinates = org.pop('gps_coordinates')
    ur_address = org.pop('ur_address')

    phones = org.pop('phones')
    faxes = org.pop('faxes')
    emails = org.pop('emails')
    sites = org.pop('sites')

    main_okved2007 = org.pop('main_okved2007')
    sup_okved2007 = org.pop('sup_okved2007')

    main_okved2 = org.pop('main_okved2')
    sup_okved2007 = org.pop('sup_okved2')

    org = Organization(**org).save()

    # Сохраняем адресс и юридический адресс с gps координатами (если заданы) 
    longitude = gps_coordinates['longitude'] if gps_coordinates['longitude'] else None
    latitude = gps_coordinates['longitude'] if gps_coordinates['longitude'] else None
    if address:
        address = Address(organization=org, address=address, gps_longitude=longitude, gps_latitude=latitude)
        address.save()
        if ur_address:
            ur_address = Address(organization=org, address=ur_address, is_legal=True)
            ur_address.save()
    elif(ur_address):
        ur_address = Address(organization=org, address=ur_address, is_legal=True, gps_longitude=longitude, gps_latitude=latitude)
        ur_address.save()

    # Сохраняем телефонные номера
    phones = [Phone(organization=org, phone=phone) for phone in phones]
    for phone in phones:
        phone.save()

    # Сохраняем факсы
    faxes = [Fax(organization=org, fax=fax) for fax in faxes]
    for fax in faxes:
        fax.save()

    # Сохраняем email'ы
    emails = [Email(organization=org, email=email) for email in emails]
    for email in emails:
        email.save()

    # Сохраняем сыллки на сайты организации
    sites = [Site(organization=org, site=site) for site in sites]

    return org   
