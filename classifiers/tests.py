from django.test import TestCase

from classifiers.services.utils import *
from classifiers.models import Okved2
from classifiers.models import Okpd2

class DataImportTestCase(TestCase):

    def setUp(self):
        pass

    def test_dict_replace_names(self):
        value_one = 'value_one'
        value_two = 'value_two'

        old_name_one = 'OldNameOne'
        old_name_two = 'OldNameTwo'

        new_name_one = 'new_name_one'
        new_name_two = 'new_name_two'

        old_new_names_dict = {
            old_name_one: new_name_one,
            old_name_two: new_name_two,
        }

        old_dict = {
            old_name_one: value_one,
            old_name_two: value_two,
        }

        expected = {
            new_name_one: value_one,
            new_name_two: value_two,
        }

        self.assertEqual(expected, dict_replace_names(old_dict, old_new_names_dict))

    def test_dict_delete_empty(self):
        not_empty_str_key = 'not_empty_str'
        not_empty_str_value = 'not_empty_value'

        not_empty_int_key = 'not_empty_int'
        not_empty_int_value = 10

        dict_with_empty = {
            not_empty_str_key: not_empty_str_value,
            'empty_str': '',
            not_empty_int_key: not_empty_int_value,
            'empty_int': None
        }

        expected = {
            not_empty_str_key: not_empty_str_value,
            not_empty_int_key: not_empty_int_value,
        }

        self.assertEqual(expected, dict_delete_empty(dict_with_empty))


    # TODO Необходимо создавать файл и заполнять его
    # тестовыми данными, затем проверять корректно ли
    # они считались
    # def test_import_data_from_csv(self):
    #   pass
   
        
