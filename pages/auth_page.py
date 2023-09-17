from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):
    """ Страница авторизации """

    """Значения value input_tab_type при соответствующем выбраннном табе"""
    _input_tt_values = {'phone': "PHONE", 'mail': "EMAIL", 'id': "LOGIN", 'ls': "LS"}
    """ Замещающий текст полей ввода """
    _placeholders = {'phone': "Мобильный телефон", 'mail': "Электронная почта", 'id': "Логин", 'ls': "Лицевой счёт",
                     'pass': 'Пароль'}
    """ Класс активного таба """
    _tab_active = "rt-tab rt-tab--small rt-tab--active"

    """ Замомнить меня вкл"""
    _box_remember_on = "rt-checkbox rt-checkbox--checked"
    """ Замомнить меня выкл"""
    _box_remember_off = "rt-checkbox"

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    """ Поле ввода для авторизации по коду """
    login_code_input = WebElement(xpath='//input[@id="address"]')
    """ Кнопка "Получить код" """
    btn_get_code = WebElement(xpath='//button[@id="otp_get_code"]')
    """ Кнопка "Войти с паролем" """
    btn_st_auth = WebElement(xpath='//button[@id="standard_auth_btn"]')
    """ Поле ввода одноразового пароля """
    input_ot_code = WebElement(id='rt-code-0')
    """ Кнопка Войти при входе по одноразовому паролю  """
    btn_enter_ot = WebElement(xpath='//div[@class="btn-container"]')
    """ Изображение капчи  """
    captcha_img = WebElement(xpath='//img[@class="rt-captcha__image"]')
    """ Данные капчи введенные пользователем """
    captcha_data = WebElement(
        xpath='//div[@class="rt-input-container rt-captcha__input"]//span[@class="rt-input__mask-start"]')
    """ Сообщение о некоректно введенном одноразовом коде """
    span_wrong_code = WebElement(xpath='//span[@id="form-error-message"]')

    """ Поле ввода логина """
    login_input = WebElement(xpath='//input[@id="username"]')
    """ Поле ввода логина, замещающий текст """
    login_txt = WebElement(
        xpath='//div[@class="rt-input-container tabs-input-container__login"]//span[@class="rt-input__placeholder"]')

    """ Поле ввода пароля"""
    pass_input = WebElement(xpath='//input[@id="password"]')
    """ Поле ввода пароля, замещающий текст """
    pass_text = WebElement(
        xpath='//div[@class="rt-input-container"]//span[@class="rt-input__placeholder"]')

    """Таб выбора аутентификации по номеру"""
    tab_phone = WebElement(xpath='//div[@id="t-btn-tab-phone"]')
    """Таб выбора аутентификации по почте"""
    tab_mail = WebElement(xpath='//div[@id="t-btn-tab-mail"]')
    """Таб выбора аутентификации по логину"""
    tab_id = WebElement(xpath='//div[@id="t-btn-tab-login"]')
    """Таб выбора аутентификации по лицевому счету (ЛС)"""
    tab_ls = WebElement(xpath='//div[@id="t-btn-tab-ls"]')
    """Инпут, указывающий на выбранный тип таба"""
    input_tt = WebElement(xpath='//input[@name="tab_type"]')

    """ Чекбокс Запомнить меня """
    div_remember = WebElement(xpath='//div[@class="login-form__remember-forgot-con"]/div')  # div-контейнер
    box_remember = WebElement(xpath='//div[@class="login-form__remember-forgot-con"]/div/span[1]')  # box

    """ Кнопка Войти"""
    btn_enter = WebElement(id='kc-login')

    """ Все неактивные табы """
    tabs_inactive = ManyWebElements(xpath='//*[@class="rt-tab rt-tab--small"]')

    """Поле юзернейма после успешной авторизации"""
    username_container = WebElement(xpath='//h2[@class="user-name user-info__name"]')

    """ Кнопка Выйти"""
    btn_logout = WebElement(id='logout-btn')

    """ Сообщение об ошибке """
    error_login_msg = WebElement(id='form-error-message')

    """ Контакты авторизованного пользователя """
    usr_contact_phone = WebElement(
        xpath='//div[@class="user-contacts home__user-contacts"]/div[1]//span[@class="user-contacts-item__value text-ellipsis"]')
    usr_contact_mail = WebElement(
        xpath='//div[@class="user-contacts home__user-contacts"]/div[2]//span[@class="user-contacts-item__value text-ellipsis"]')

    """ Соглашение  """
    agree_link = WebElement(id='rt-footer-agreement-link')

    """ Вход через соцсети """
    social_vk = WebElement(id='oidc_vk')
    social_ok = WebElement(id='oidc_ok')
    social_mail = WebElement(id='oidc_mail')
    social_ya = WebElement(id='oidc_ya')
    ya_link = WebElement(xpath='//a[@href="https://ya.ru"]')

    """ Ссылка на регистрацию  """
    register_lnk = WebElement(id='kc-register')
