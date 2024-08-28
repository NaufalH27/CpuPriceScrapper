from bs4 import BeautifulSoup
from .import process_raw_data
from . import raw_data_pool


def tokopedia_product_search(search_html):
    data_bucket_list = []
    soup = BeautifulSoup(search_html, features="html.parser")
    product_container = soup.find('div', {'data-testid': 'cntrFindProductsResult'})

    if product_container:
        all_product_div = product_container.find_all('div', {'data-ssr':"findProductSSR"})

        for product_div in all_product_div:
            product_raw_data_pool = raw_data_pool.collect_data(product_div)
            processed_data_bucket = process_raw_data.get_processed_data(product_raw_data_pool)
            data_bucket_list.append(processed_data_bucket)

        return data_bucket_list
    
    else:
        return []