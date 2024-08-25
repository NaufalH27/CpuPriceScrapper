def is_integrated(product):
    product_name =  product["product"]["name"]
    sold_items = product["product"]["sold_items"]
    rating = product["product"]["rating"]
    price_str = product["product"]["price"]["string"] 
    price_int = product["product"]["price"]["integer"] 
    discount_str = product["product"]["discount"]["string"] 
    discount_float = product["product"]["discount"]["float"] 
    product_img = product["product"]["image"]
    product_link = product["product"]["link"] 
    seller_name =  product["seller"]["name"]
    seller_location = product["seller"]["location"]
    seller_badge = product["seller"]["badge"] 
    seller_link = product["seller"]["link"] 
    

    if product_name == None or not isinstance(product_name, str):
        return False
    if not isinstance(sold_items, str):
        return False
    if rating !=  None and not isinstance(rating, float) or rating > 5.0:
        return False
    if price_str == None or not isinstance(price_str, str):
        return False
    if not isinstance(price_int, int):
        return False
    if rating != None and not isinstance(discount_str, str):
        return False
    if discount_float == None and not isinstance(discount_float, float):
        return False
    if product_img == None:
        return False
    if product_link == None:
        return False
    if seller_name == None:
        return False
    if seller_location == None:
        return False
    if seller_badge == None:
        return False
    if seller_link == None:
        return False
    
     