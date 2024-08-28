from .helper import string_helper
from .helper import city_dictionary


#image url based data identifier
def is_seller_badge_url(image_url):
    if image_url.startswith("https://images.tokopedia.net/img/") and "cache/200-square" not in image_url:
        return True

def is_product_image_url(image_url):
    if image_url.startswith('https://images.tokopedia.net/img/cache/200-square'):
        return True


#text based data identifier
def is_ad(text):
    return text == "Ad"

def is_product_discount(text):
    discount_regex = r'^\d+%$'
    return string_helper.is_regex_found(text, discount_regex)

def is_product_rating(text):
    rating_regex = r'^\d\.\d$'
    return string_helper.is_regex_found(text, rating_regex)

def is_product_sold_item_status(text):
    sold_item_regex = r'^\d+\+?.*terjual$'
    return string_helper.is_regex_found(text, sold_item_regex)
    
def is_product_price(text):
    price_regex = r'^Rp[\d.,]+'
    return string_helper.is_regex_found(text, price_regex)
    
def is_location(text):
    city_list = city_dictionary.get_city_list_by_first_letter(text)
    if city_list is not None and text in city_list:
        return True


