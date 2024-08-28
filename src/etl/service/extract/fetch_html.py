import time
from selenium import webdriver



def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    scroll_position = 0
    scroll_increment = 250 

    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        scroll_position += scroll_increment
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(0.3)
        if scroll_position >= new_height:
            break
    return driver.page_source
    