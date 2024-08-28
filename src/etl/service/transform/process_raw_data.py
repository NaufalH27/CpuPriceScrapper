from collections import deque
from . import data_identifier
from . import formats
from .helper import list_helper
from .helper import url_helper
from .helper import string_helper




def get_processed_data(data_pool):
    data_bucket = formats.get_data_bucket_format()
    dump_url_destination_to_bucket(data_bucket, data_pool["tracking_url"])
    dump_text_data_to_bucket(data_bucket, data_pool["text"])
    dump_image_url_to_bucket(data_bucket, data_pool["img"])
    return data_bucket




#helper function
def dump_url_destination_to_bucket(data_bucket, tracking_url):
    tokopedia_url_destination_regex  = r'www\.tokopedia\.com(.*)'
    match = string_helper.search_regex(tracking_url, tokopedia_url_destination_regex )

    if match:
        encoded_url_destination = match.group()
        decoded_url_destination = url_helper.decode_url(encoded_url_destination)
        data_bucket["product_url"] = decoded_url_destination



def dump_image_url_to_bucket(data_bucket, image_list):
    for image_url in image_list:
        if data_identifier.is_seller_badge_url(image_url):
           data_bucket["seller_badge_url"] = image_url

        if data_identifier.is_product_image_url(image_url):
            data_bucket["image_url"] = image_url




def dump_text_data_to_bucket(data_bucket, text_list):
    text_list = list_helper.remove_anomalies(text_list)
    leftover_text = []
    queue = deque(text_list)

    while(queue):
        current_text = queue.popleft()
        if data_identifier.is_ad(current_text):
            data_bucket["is_ad"] = True 
            continue

        if data_identifier.is_product_price(current_text):
            old_price =  data_bucket["price"]
            new_price = current_text

            if string_helper.is_new_price_lower(new_price, old_price):
                data_bucket["price"] = new_price
                data_bucket["price_int"] = string_helper.rupiah_price_tag_to_int(new_price)

            continue

        if data_identifier.is_product_discount(current_text):
            data_bucket["discount"] = current_text
            data_bucket["discount_float"] = string_helper.percentage_to_float(current_text)
            continue

        if data_identifier.is_product_sold_item_status(current_text):
            data_bucket["sold_items"] = string_helper.remove_substring(current_text, "terjual").strip()
            continue

        if data_identifier.is_product_rating(current_text):
            data_bucket["rating"] = string_helper.rating_to_float(current_text)
            continue

        if data_identifier.is_location(current_text):
            data_bucket["location"] = current_text
            continue
        
        # If the current text does not match any known data identifiers, it is likely part of the product or seller name.
        # This unidentified text is added to the leftover_text list for further processing.
        leftover_text.append(current_text)



    # Process the seller name and product name using the remaining unidentified text.
    # Extract the best matches for both the seller and product names based on the Tokopedia URL slugs.
    # Example Tokopedia URL: "https://www.tokopedia.com/sellerslug/product-name-slug&random%&config"
    # The slug_regex below extracts two groups:
    #   group(1): 'sellerslug' - the seller's URL slug
    #   group(2): 'product-name-slug&random%&config' - the product's URL slug and additional parameters
    if data_bucket["product_url"] is not None and leftover_text is not None:
        slug_regex = r'https://www\.tokopedia\.com/([^/]+)/([^?]+)'
        match = string_helper.search_regex(data_bucket["product_url"], slug_regex)
        
        if match:
            seller_slug = match.group(1)
            product_name_slug = match.group(2)

            data_bucket["product_name"] = string_helper.get_best_match_from_list(product_name_slug, leftover_text)
            data_bucket["seller_name"] = string_helper.get_best_match_from_list(seller_slug, leftover_text)
            
            data_bucket["seller_url"] = f"https://www.tokopedia.com/{seller_slug}"


