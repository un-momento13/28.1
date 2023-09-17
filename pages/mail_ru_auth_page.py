from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements

class AuthMailPage(WebPage):
    """ Страница авторизации на почте """

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://account.mail.ru/login'
        super().__init__(web_driver, url)

    login_input = WebElement(xpath='//input[@name="username"]')
    pass_input = WebElement(xpath='//input[@name="password"]')

    box_remember = WebElement(xpath='//div[@data-checked]')
    btn_next = WebElement(xpath='//button[@data-test-id="next-button"]')
    btn_enter = WebElement(xpath='//button[@data-test-id="submit-button"]')

    btn_inbox = WebElement(xpath='//a[@href="/inbox/?"]')
    menu_clear_all = WebElement(xpath='//div[@data-qa-id="clear"]')
    btn_confirm_clear = WebElement(xpath='//div[@class="layer__submit-button"]')

    first_mail_content = WebElement(xpath='//span[@class="ll-sp__normal"]')
