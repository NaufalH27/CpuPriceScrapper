from collections import deque
from . import data_identifier
from . import formats
from .helper import list_helper
from .helper import url_helper
from .helper import string_helper

def generate_formatted_product(data_pool):
    product_data_dump = formats.get_raw_data_dump_format()
    populate_product_url_destination(product_data_dump, data_pool["tracking_url"])
    populate_product_text(product_data_dump, data_pool["text"])
    populate_product_img(product_data_dump, data_pool["img"])
    transformed_product = formats.transform_to_final_format(product_data_dump)
    return transformed_product


        
def populate_product_url_destination(product, tracking_url):
    regex = r'www\.tokopedia\.com(.*)'
    match = string_helper.search_regex(tracking_url, regex)
    if match:
        encoded_url_destination = match.group()
        decoded_url_destination = url_helper.decode_url(encoded_url_destination)
        product["product_url"] = decoded_url_destination



def populate_product_img(product, image_list):
    for image_url in image_list:
        if data_identifier.is_seller_badge_url(image_url):
           product["seller_badge_url"] = image_url

        if data_identifier.is_product_image_url(image_url):
            product["image_url"] = image_url



def populate_product_text(product, raw_text_entries):
    raw_text_entries = list_helper.remove_anomalies(raw_text_entries)
    leftover_text = []
   
    text_queue = deque(raw_text_entries)
    while(text_queue):
        text = text_queue.popleft()
        if data_identifier.is_ad(text):
            product["is_ad"] = True 
            continue

        if data_identifier.is_product_price(text):
            current_price = string_helper.rupiah_price_tag_to_int(text)
            if product["price"] is None:
                product["price"] = text
                product["price_int"] = current_price

            elif current_price <  product["price_int"]:
                product["price"] = text
                product["price_int"] = current_price
                
            continue

        if data_identifier.is_product_discount(text):
            product["discount"] = text
            product["discount_float"] = string_helper.percentage_to_float(text)
            continue

        if data_identifier.is_product_sold_item_status(text):
            product["sold_items"] = string_helper.remove_substring(text, "terjual").strip()
            continue

        if data_identifier.is_product_rating(text):
            product["rating"] = string_helper.rating_to_float(text)
            continue

        if data_identifier.is_location(text):
            product["location"] = text
            continue

        leftover_text.append(text)

    
    if product["product_url"] is not None:
        regex = r'https://www\.tokopedia\.com/([^/]+)/([^?]+)'
        match = string_helper.search_regex(product["product_url"], regex)
        if match:
            seller_slug = match.group(1)
            product_name_slug = match.group(2)

        product["product_name"] = string_helper.get_best_match_from_list(product_name_slug, leftover_text)
        product["seller_name"] = string_helper.get_best_match_from_list(seller_slug, leftover_text)
        product["seller_url"] =  f"https://www.tokopedia.com/{seller_slug}"


