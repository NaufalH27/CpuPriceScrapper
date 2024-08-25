import re
from .helper import url_helper
from .helper import data_cleaning
from .helper import product_location

def check_ad(product, data):
    product["is_ad"] = data == "Ad"


def extract_badge(product, data):
    if data.startswith("https://images.tokopedia.net/img/") and "cache/200-square" not in data:
        # filename = data.split('/')[-1]
        # badge_name = filename.rsplit('.', 1)[0]
        product["badge"] = data


def extract_discount(product, data):
    match = re.search(r'^\d+%$', data)
    if match:
        product["discount"] = match.group()
        product["discount_float"] = data_cleaning.percentage_to_float(match.group())


def extract_image(product, data):
    if data.startswith('https://images.tokopedia.net/img/cache/200-square'):
        product["image"] = data


def extract_link(product, obfuscated_url):
    pattern = r'www\.tokopedia\.com(.*)'
    match = re.search(pattern, obfuscated_url)
    if match:
        product["product_link"] = url_helper.decode_url(match.group())


def extract_rating(product, data):
    match = re.search(r'^\d\.\d$', data)
    if match:
        rating_float = float(match.group().strip())
        product["rating"] = rating_float


def extract_sold_items(product, data):
    match = re.search(r'^\d+\+?.*terjual$', data)
    if match:
        product["sold_items"] = match.group().replace("terjual", "").strip()
            

def extract_price(product, data):
    match = re.search(r'^Rp[\d.,]+', data)
    price = {}

    if match:
        new_price = match.group()
        price[new_price] = int(new_price.replace("Rp", "").replace(".", "").strip())

        if product["price"] == None:
            product["price"] = new_price
            product["price_int"] = price[new_price]

        else:
            old_price = product["price"]
            price[old_price] = int(old_price.replace("Rp", "").replace(".", "").strip())
            min_price = min(price, key=price.get)
            product["price"] = min_price
            product["price_int"] = price[min_price]


def extract_location(product,data_list):
    city_map_by_letter = product_location.get_city_map_by_letter()
    best_match = ""
    highest_score = 0
    for data in data_list:
        remove_kab = re.compile("Kab.", re.IGNORECASE)
        city_first_letter = remove_kab.sub("", data).strip()[0].capitalize()
        try:
            city_list = city_map_by_letter[city_first_letter]
            _, curr_data_score = data_cleaning.get_best_match(data, city_list)
            
            if curr_data_score > highest_score:
                highest_score = curr_data_score
                best_match = data

        except KeyError:
            continue

    product["location"] = best_match
    
    


def extract_name(product, data_list):
    pattern = re.compile(r'https://www\.tokopedia\.com/([^/]+)/([^?]+)')
    match = pattern.search(product["product_link"])

    if match:
        product_name = match.group(2)
        best_match, _ = data_cleaning.get_best_match(product_name, data_list)
        product["name"] = best_match


def extract_seller(product, data_list):
    pattern = re.compile(r'https://www\.tokopedia\.com/([^/]+)/([^?]+)')
    match = pattern.search(product["product_link"])

    if match:
        seller_name = match.group(1)
        best_match, _ = data_cleaning.get_best_match(seller_name, data_list)
        product["seller"] = best_match
        product["seller_link"] = f"https://www.tokopedia.com/{seller_name}"
