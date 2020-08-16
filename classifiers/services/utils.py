import csv

def dict_replace_names(dictionary: dict, old_new_names: dict) -> dict:
    return {new_name: dictionary[old_name] for old_name, new_name in old_new_names.items()}

def dict_delete_empty(dictionary: dict) -> dict:
    return {key: value for key, value in dictionary.items() if not (value is None or value == '')}
    
def import_data_from_csv(model_class: type, csv_file_path: str, csv_model_names_matching: dict):
    with open(csv_file_path, encoding='utf-8', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        next(csv_reader)
        model_objects = [model_class(**dict_delete_empty(dict_replace_names(row, csv_model_names_matching))) for row in csv_reader]
        return model_objects