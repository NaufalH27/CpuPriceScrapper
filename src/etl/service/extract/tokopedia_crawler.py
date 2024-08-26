from . import fetch_html

def tokopedia_search(search_items, pages = 1):
    pages_string = f"?page={pages}"
    return fetch_html.get_html("https://tokopedia.com/find/" + search_items + pages_string)
