import requests
import logging
import time
from selenium import webdriver




driver = webdriver.Chrome()


def fetch_url(url):
    try:
        driver.get(url)
        scroll_position = 0
        scroll_increment = 250 

        while True:
            driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
            scroll_position += scroll_increment
            new_height = driver.execute_script("return document.body.scrollHeight")
            if scroll_position >= new_height:
                break
        time.sleep(1)
        return  driver.page_source
    
    except requests.exceptions.Timeout:
        logging.error(e + ", retrying... ")     

    except requests.exceptions.TooManyRedirects:
        logging.error("bad url, try different url")

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    