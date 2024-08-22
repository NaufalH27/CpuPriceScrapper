from .crawler_script import fetch_url

def tokopedia_search(search_items):
    return fetch_url("https://tokopedia.com/find/" + search_items)
