from service.extract import tokopedia_crawler
from service.transform import parse
import json

html = tokopedia_crawler.tokopedia_search("ryzen 5 7500f", pages=1)

product_list = parse.transform_html(html)
pretty_json = json.dumps(product_list, indent=4)
print(pretty_json)





