from . import formats

def collect_data(product_div):
    data_pool = formats.get_data_pool_format()

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
            tracking_url = element.get("href")
            if tracking_url:
                data_pool["tracking_url"] = tracking_url

    return data_pool