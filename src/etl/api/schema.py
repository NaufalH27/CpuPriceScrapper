from pydantic import BaseModel, HttpUrl
from typing import Optional



def get_product_output(product_list):
    schema = []
    for product_data_bucket in product_list:
        if ProductData.is_valid(product_data_bucket):
            schema.append(transform_to_final_format(product_data_bucket))
    return schema


def transform_to_final_format(product_data_bucket):
 return {
    "product_info": {
        "name": product_data_bucket["product_name"],
        "is_ad": product_data_bucket["is_ad"],
        "sold_items": product_data_bucket["sold_items"],
        "rating": product_data_bucket["rating"],
         "discount":{ 
           "string" : product_data_bucket["discount"],
           "float" :  product_data_bucket["discount_float"],
        },
        "price":{
           "string" : product_data_bucket["price"],
           "integer" : product_data_bucket["price_int"],
        }, 
       
        "image": product_data_bucket["image_url"],
        "url": product_data_bucket["product_url"], 
    },
    "seller": {
        "name": product_data_bucket["seller_name"],  
        "location": product_data_bucket["location"],
        "badge": product_data_bucket["seller_badge_url"],
        "url" : product_data_bucket["seller_url"]
    }
}



class ProductData(BaseModel):

    #data integration
    product_url : HttpUrl
    product_name : str
    seller_name : str
    is_ad : bool
    price : str
    price_int : int
    discount : Optional[str]
    discount_float : Optional[float]
    seller_badge_url : HttpUrl
    sold_items :  Optional[str]
    rating:  Optional[float]
    location : str
    seller_url : HttpUrl
    image_url : HttpUrl

    @classmethod
    def is_valid(cls, data):
        try:
            product_data = cls(**data)
            return True
        except ValueError:
            return False
        