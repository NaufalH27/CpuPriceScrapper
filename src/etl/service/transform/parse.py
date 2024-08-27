from bs4 import BeautifulSoup
from .import generate_product
from . import generate_data_pool


def transform_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    product_grid_container = soup.find('div', {'data-testid': 'cntrFindProductsResult'})

    if not product_grid_container:
        return []

    all_product_div = product_grid_container.find_all('div', {'data-ssr':"findProductSSR"})
    
    if not all_product_div:
        return []
    
    product_list = []
    for product_div in all_product_div:
        product_data_pool = generate_data_pool.collect_data(product_div)
        product = generate_product.generate_formatted_product(product_data_pool)
        product_list.append(product)

    return product_list
