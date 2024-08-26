def get_initial_product_format():
    return {
            "name": None,
            "seller" : None,
            "is_ad": False,
            "price": None,
            "price_int": None,
            "discount": None,
            "discount_float" : None,
            "badge": None,
            "sold_items": None,
            "rating": None,
            "location": None,
            "product_link" : None,
            "seller_link": None,
            "image" : None
    }

def transform_to_final_format(processed_product):
 return {
    "product": {
        "name": processed_product["name"],
        "is_ad": processed_product["is_ad"],
        "sold_items": processed_product["sold_items"],
        "rating": processed_product["rating"],
        "price":{
           "string" : processed_product["price"],
           "integer" : processed_product["price_int"],
        }, 
        "discount":{ 
           "string" : processed_product["discount"],
           "float" : processed_product["discount_float"]
                    },
        "image": processed_product["image"],
        "link": processed_product["product_link"], 
    },
    "seller": {
        "name": processed_product["seller"],  
        "location": processed_product["location"],
        "badge": processed_product["badge"],
        "link" : processed_product["seller_link"]
    }
}
