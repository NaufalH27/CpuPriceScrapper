from . import fetch_html

def search_product(product_param, pages = 1):
    pages_string = f"?page={pages}"
    return fetch_html.get_html("https://tokopedia.com/find/" + product_param + pages_string)
