from fuzzywuzzy import process
import re

def percentage_to_float(percentage_str : str):
    return float(percentage_str.strip('%')) / 100


def rupiah_price_tag_to_int(price_tag :str):
    return int(price_tag.replace("Rp", "").replace(".", "").strip())


def rating_to_float(rating_str):
    return float(rating_str.strip())


def remove_substring(string, substring):
    substring_to_remove = re.compile(substring, re.IGNORECASE)
    return substring_to_remove.sub("", string)

def is_regex_found(text, regex):
    if re.search(regex, text):
        return True
    
def search_regex(text, regex):
    pattern = re.compile(regex)
    match = pattern.search(text)
    if match:
        return match
    
def get_best_match_from_list(text, text_list):
    best_match, _ = process.extractOne(text, text_list)
    return best_match

def is_new_price_lower(new_price, old_price):
    if old_price is None:
        return True
    
    if rupiah_price_tag_to_int(new_price) < rupiah_price_tag_to_int(old_price):
        return True