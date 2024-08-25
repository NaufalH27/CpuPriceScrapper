from . import extract_utils
from . import output_format
from .helper import data_cleaning

def generate_formatted_product(data_pool):
    product = output_format.get_initial_product_format()
    extract_utils.extract_link(product, data_pool["product_link"])
    populize_product_text(product, data_pool["text"])
    populize_product_img(product, data_pool["img"])
    transformed_product = output_format.transform_to_final_format(product)
    return transformed_product

def populize_product_img(product, image_list):
    for image in image_list:
        if product["badge"] == None:
            extract_utils.extract_badge(product, image)

        if product["image"] == None:
            extract_utils.extract_image(product, image)  


def populize_product_text(product, text_list):
    for text in text_list:
        if product["is_ad"] == None or product["is_ad"] == False:
            extract_utils.check_ad(product, text)
        
        extract_utils.extract_price(product, text)

        if product["discount"] == None:
            extract_utils.extract_discount(product, text)

        if product["sold_items"] == None:
            extract_utils.extract_sold_items(product, text)

        if product["rating"] == None:
            extract_utils.extract_rating(product, text)

    texts_to_remove = {text for text in product.values() if text is not None}
    text_list = [text for text in text_list if text not in texts_to_remove]
    text_list = data_cleaning.remove_anomalies(text_list)

    if product["location"] == None:
        extract_utils.extract_location(product, text_list)
        text_list = [text for text in text_list if text != product["location"]]

    if product["name"] == None:
        extract_utils.extract_name(product, text_list)
        text_list = [text for text in text_list if text != product["name"]]

    if product["seller"] == None:
        extract_utils.extract_seller(product, text_list)
        text_list = [text for text in text_list if text != product["seller"]]
