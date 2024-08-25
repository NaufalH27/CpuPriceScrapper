from bs4 import BeautifulSoup
from .import generate_product
from . import data_collector


def parse_html(html):
    product_list = []
    soup = BeautifulSoup(html, features="html.parser")
    parent_div = soup.find('div', {'data-testid': 'cntrFindProductsResult'})
    all_product_div = parent_div.find_all('div', {'data-ssr':"findProductSSR"})
    for product_div in all_product_div:
        product_data_pool = data_collector.collect_product_data(product_div)
        product = generate_product.generate_formatted_product(product_data_pool)
        product_list.append(product)
    return product_list
