from .helper import string_helper


def get_data_pool_format():
    return {
        "tracking_url": None,
        "text": [], 
        "img" :[]
    }


def get_raw_data_dump_format():
    return {
       "product_url" : None,
        "product_name": None,
        "seller_name" : None,
        "is_ad": False,
        "price": None,
        "price_int" : None,
        "discount": None,
        "discount_float" : None,
        "seller_badge_url": None,
        "sold_items": None,
        "rating": None,
        "location": None,
        "seller_url": None,
        "image_url" : None
    }

def transform_to_final_format(product_data_dump):
 return {
    "product_info": {
        "name": product_data_dump["product_name"],
        "is_ad": product_data_dump["is_ad"],
        "sold_items": product_data_dump["sold_items"],
        "rating": product_data_dump["rating"],
        "price":{
           "string" : product_data_dump["price"],
           "integer" : product_data_dump["price_int"],
        }, 
        "discount":{ 
           "string" : product_data_dump["discount"],
           "float" :  product_data_dump["discount_float"],
                    },
        "image": product_data_dump["image_url"],
        "url": product_data_dump["product_url"], 
    },
    "seller": {
        "name": product_data_dump["seller_name"],  
        "location": product_data_dump["location"],
        "badge": product_data_dump["seller_badge_url"],
        "url" : product_data_dump["seller_url"]
    }
}


