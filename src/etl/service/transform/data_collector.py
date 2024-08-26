
def collect_product_data(product_div):
    data_pool = {
        "product_link": None,
        "text": [], 
        "img" :[]
    }

    for element in product_div.descendants:
        if isinstance(element, str):
            text = element.strip()
            if text:
                data_pool["text"].append(text)
        
        elif element.name == 'img':
            img_src = element.get('src')
            if img_src:
                data_pool["img"].append(img_src)

        elif element.name == 'a':
            product_link = element.get("href")
            if product_link:
                data_pool["product_link"] = product_link

    return data_pool