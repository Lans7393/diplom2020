import re

def replace_multiple(string: str, olds: list, new: str) -> str:
    for old in olds:
        string = string.replace(old, new)
    return  string


def del_redundant_spases(string: str) -> str:
    return re.sub(r'\s+', ' ', string)
