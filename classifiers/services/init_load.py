import os

from classifiers.models import Okpd2, Okved2, Okved2007
from classifiers.services.utils import import_data_from_csv

from django.conf import settings

from bulk_sync import bulk_sync

data_dir_path = os.path.join(settings.BASE_DIR, 'classifiers', 'data')

def load_okved2():
    csv_model_names_matching = {
        'Name': 'name',
        'global_id': 'global_id',
        'Razdel': 'section',
        'Kod':  'code',
        'Nomdescr': 'description'
    }

    file_path = os.path.join(data_dir_path, "okved2.csv")
    models = import_data_from_csv(Okved2, file_path, csv_model_names_matching)

    result = bulk_sync(new_models=models, filters=[], key_fields=['code', 'name', 'global_id'])
    print("Results of Okved2 bulk_sync: "
        "{created} created, {updated} updated, {deleted} deleted."
                .format(**result['stats']))


def load_okved2007():
    csv_model_names_matching = {
        'Name': 'name',
        'global_id': 'global_id',
        'Razdel': 'section',
        'Prazdel': 'subsection',
        'Idx': 'index',
        'Kod': 'code',
        'Nomdescr': 'description'
    }

    file_path = os.path.join(data_dir_path, "okved2007.csv")
    models = import_data_from_csv(Okved2007, file_path, csv_model_names_matching)

    result = bulk_sync(new_models=models, filters=[], key_fields=['code', 'name', 'index', 'global_id'])
    print("Results of Okved2007 bulk_sync: "
        "{created} created, {updated} updated, {deleted} deleted."
                .format(**result['stats']))


def load_okpd2():
    csv_model_names_matching = {
        'Name': 'name',
        'global_id': 'global_id',
        'Razdel': 'section',
        'Kod':  'code',
        'Nomdescr': 'description'
    }

    file_path = os.path.join(data_dir_path, "okpd2.csv")
    models = import_data_from_csv(Okpd2, file_path, csv_model_names_matching)

    result = bulk_sync(new_models=models, filters=[], key_fields=['code', 'name', 'global_id'])
    print("Results of Okpd2 bulk_sync: "
        "{created} created, {updated} updated, {deleted} deleted."
                .format(**result['stats']))