import os
import pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

        # with open('my_cookies.txt', 'rb') as cookiesfile:
        #    cookies = pickle.load(cookiesfile)
        #    for cookie in cookies:
        #        web_driver.add_cookie(cookie)
        # web_driver.refresh();

    # Main search field
    # search = WebElement(id='search_product')

    # Search button
    # search_run_button = WebElement(xpath='//button[@type="button"]')

    # Titles of the products in search results
    # products_titles = ManyWebElements(xpath="//div[contains(@class, 'productinfo text-center')]")
