import time
from random import randrange
import pytest
from pages.auth_page import AuthPage
from pages.mail_ru_auth_page import AuthMailPage


def test_agree(web_browser):
    """ Проверка ссылки на пользовательское соглашение """
    page_rt = AuthPage(web_browser)
    time.sleep(0.5)
    page_rt.wait_page_loaded()  # Ждем загрузки
    wh_rt = web_browser.current_window_handle

    page_rt.agree_link.click()

    for wh in web_browser.window_handles:
        if wh != wh_rt:
            web_browser.switch_to.window(wh)
            break

    assert page_rt.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

    time.sleep(1)


def test_social(web_browser):
    """ Наличие ссылок на соцсети """
    page_rt = AuthPage(web_browser)
    time.sleep(0.5)
    page_rt.wait_page_loaded()  # Ждем загрузки

    time.sleep(2)

    assert page_rt.social_vk.is_visible()
    assert page_rt.social_ya.is_visible()
    assert page_rt.social_ok.is_visible()
    assert page_rt.social_mail.is_visible()

    link = 'https://id.vk.com/'
    page_rt.social_vk.click()
    page_rt.wait_page_loaded()
    assert link == page_rt.get_current_url()[0:len(link)]
    web_browser.back()
    page_rt.wait_page_loaded()

    link = 'https://connect.ok.ru/'
    page_rt.social_ok.click()
    page_rt.wait_page_loaded()
    assert link == page_rt.get_current_url()[0:len(link)]
    web_browser.back()
    page_rt.wait_page_loaded()

    link = 'https://connect.mail.ru/'
    page_rt.social_mail.click()
    page_rt.wait_page_loaded()
    assert link == page_rt.get_current_url()[0:len(link)]
    web_browser.back()
    page_rt.wait_page_loaded()

    # Яша не любит Селениума
    # link = 'https://passport.yandex.ru/'
    # page_rt.social_ya.click()
    # page_rt.wait_page_loaded()
    # assert link == page_rt.get_current_url()[0:len(link)]

    time.sleep(1)


def test_reg_link(web_browser):
    """ Наличие ссылки на регистрацию и её работа """
    reg_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'

    page_rt = AuthPage(web_browser)
    time.sleep(0.5)
    page_rt.wait_page_loaded()  # Ждем загрузки

    assert page_rt.register_lnk.is_presented()

    page_rt.register_lnk.click()
    cur_url = page_rt.get_current_url()
    cur_url = cur_url[0:len(reg_url)]

    assert cur_url == reg_url

    time.sleep(0.2)


def test_all_tabs(web_browser):
    """ Присутствуют все табы для переключения """
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    assert page.tab_phone.is_presented()  # Таб выбора аутентификации по номеру
    assert page.tab_mail.is_presented()  # Таб выбора аутентификации по почте
    assert page.tab_id.is_presented()  # Таб выбора аутентификации по логину
    assert page.tab_ls.is_presented()  # Таб выбора аутентификации по лицевому счету (ЛС)

    time.sleep(0.2)


def test_default_tab(web_browser):
    """ По умолчанию выбрана форма авторизации по телефону """
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    """ По умолчанию выбрана форма авторизации по телефону """
    assert page.input_tt.get_attribute("value") == page._input_tt_values['phone']  # id скрытого поля
    assert page.login_txt.get_text() == page._placeholders['phone']  # замещающий текст поля ввода логина
    assert page.tab_phone.get_attribute("class") == page._tab_active  # активный таб - телефон
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны

    """ Наличие поля ввода пароля"""
    assert page.pass_input.is_visible()   # наличие поля ввода пароля
    assert page.pass_text.get_text() == page._placeholders['pass']  # замещающий текст поля ввода пароля

    time.sleep(0.2)


def test_tab_change(web_browser):
    """ Смена таба по клику """
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    page.tab_ls.click()
    time.sleep(0.2)
    assert page.input_tt.get_attribute("value") == page._input_tt_values['ls']  # id скрытого поля
    assert page.login_txt.get_text() == page._placeholders['ls']  # замещающий текст поля ввода логина
    assert page.tab_ls.get_attribute("class") == page._tab_active  # активный таб - ЛС
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны
    assert page.pass_input.is_visible()  # наличие поля ввода пароля
    assert page.pass_text.get_text() == page._placeholders['pass']  # замещающий текст поля ввода пароля

    page.tab_id.click()
    time.sleep(0.2)
    assert page.input_tt.get_attribute("value") == page._input_tt_values['id']  # id скрытого поля
    assert page.login_txt.get_text() == page._placeholders['id']  # замещающий текст поля ввода логина
    assert page.tab_id.get_attribute("class") == page._tab_active  # активный таб - логин
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны
    assert page.pass_input.is_visible()  # наличие поля ввода пароля
    assert page.pass_text.get_text() == page._placeholders['pass']  # замещающий текст поля ввода пароля

    page.tab_mail.click()
    time.sleep(0.2)
    assert page.input_tt.get_attribute("value") == page._input_tt_values['mail']  # id скрытого поля
    assert page.login_txt.get_text() == page._placeholders['mail']  # замещающий текст поля ввода логина
    assert page.tab_mail.get_attribute("class") == page._tab_active  # активный таб - почта
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны
    assert page.pass_input.is_visible()  # наличие поля ввода пароля
    assert page.pass_text.get_text() == page._placeholders['pass']  # замещающий текст поля ввода пароля

    page.tab_phone.click()
    time.sleep(0.2)
    assert page.input_tt.get_attribute("value") == page._input_tt_values['phone']  # id скрытого поля
    assert page.login_txt.get_text() == page._placeholders['phone']  # замещающий текст поля ввода логина
    assert page.tab_phone.get_attribute("class") == page._tab_active  # активный таб - телефон
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны
    assert page.pass_input.is_visible()  # наличие поля ввода пароля
    assert page.pass_text.get_text() == page._placeholders['pass']  # замещающий текст поля ввода пароля


def test_tab_change_auto(web_browser):
    """ Смена таба по вводимым данным

    Примечание:
    1. Механизм автоперехода с номера телефона на ЛС не работает, не реализован или непонятно на что ориентируется.
        В поле телефона невозможно ввести двенадцатизначный ЛС
    2. Механизм автоперехода с ЛС/почты/логина на телефон не работает, не реализован или непонятно на что ориентируется.
    """
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    page.login_input.send_keys("do@di.halt")
    page.pass_input.click()
    time.sleep(0.2)
    assert page.input_tt.get_attribute("value") == page._input_tt_values['mail']  # id скрытого поля
    assert page.tab_mail.get_attribute("class") == page._tab_active  # активный таб - почта
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны

    page.tab_phone.click()
    time.sleep(0.2)
    page.login_input.send_keys("Attikus")
    page.pass_input.click()
    assert page.input_tt.get_attribute("value") == page._input_tt_values['id']  # id скрытого поля
    assert page.tab_id.get_attribute("class") == page._tab_active  # активный таб - логин
    assert page.tabs_inactive.count() == 3  # остальные табы неактивны

    time.sleep(0.2)


def test_box_remember(web_browser):
    """Тест чекбокса запомнить меня"""
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    box_prev_state = page.div_remember.get_attribute("class")  # сохраняем состояние чекбокса
    page.box_remember.click()  # жмем чекбокс

    # состояние изменилось
    if box_prev_state == page._box_remember_on:
        assert page.div_remember.get_attribute("class") == page._box_remember_off
    else:
        assert page.div_remember.get_attribute("class") == page._box_remember_on

    # чекбокс вернулся к первоначальному состоянию
    page.box_remember.click()
    assert page.div_remember.get_attribute("class") == box_prev_state


@pytest.mark.parametrize("login_type, login, pwd, name, positive",
                         [('phone', '89648011096', 'AAa123454321', 'Несобакин Тим', True),
                          ('mail', 'skiltest.test@mail.ru', 'Qwerty9099', 'Собакин Тим', True),
                          ('phone', '89648011096', '789456123', 'Несобакин Тим', False)],
                         ids=['phone OK & pass OK',
                              'mail OK & pass OK',
                              'phone OK & pass FAIL',
                              ])
def test_login_scenario(web_browser, login_type, login, pwd, name, positive):
    """ Сценарий авторизации различными способами

    Примечание: Если вдруг на сайте включается капча, то пользователю необходимо ввести её вручную. """
    page = AuthPage(web_browser)
    time.sleep(0.5)
    page.wait_page_loaded()  # Ждем загрузки

    if page.div_remember.get_attribute("class") == page._box_remember_on:  # Скидываем чекбокс "запомнить"
        page.box_remember.click()

    if login_type == 'phone':
        page.tab_phone.click()  # Переходим на таб телефон
    elif login_type == 'mail':
        page.tab_mail.click()  # Переходим на таб mail
    elif login_type == 'id':
        page.tab_id.click()  # Переходим на таб логин
    elif login_type == 'ls':
        page.tab_ls.click()  # Переходим на таб ЛС

    page.login_input.send_keys(login)  # Вводим логин
    page.pass_input.send_keys(pwd)  # Вводим пароль

    # Если появилась капча, ждем пока её введут
    if page.captcha_img.is_presented():
        i = 10

        captcha = page.captcha_data.get_attribute('innerHTML')
        while i:
            time.sleep(10)
            if captcha == page.captcha_data.get_attribute('innerHTML'):
                break
            captcha = page.captcha_data.get_attribute('innerHTML')
            i -= 1

    page.btn_enter.click()  # Жмем "войти"
    page.wait_page_loaded()  # Ждем загрузки

    time.sleep(1)

    if positive:  # Позитивные тесты
        assert page.username_container.get_attribute("title") == name  # Проверяем имя

        if login_type == 'phone':
            phone = page.usr_contact_phone.get_attribute('title')

            phone = phone.replace('+7', '')
            phone = phone.replace('-', '')
            phone = phone.replace(' ', '')

            assert phone == login[(len(login) - 10):len(login)]

        elif login_type == 'mail':
            mail = page.usr_contact_mail.get_attribute('title')

            assert mail == login
        elif login_type == 'id':
            """ TODO не на чем проверить - не реализовано """
        elif login_type == 'ls':
            """ TODO не на чем проверить - не реализовано """

        page.btn_logout.click()  # Выходим
        page.wait_page_loaded()  # Ждем загрузки

        assert page.btn_enter.is_visible()  # Проверяем возврат на авторизацию
    else:  # Негативные тесты
        assert page.error_login_msg.is_presented()  # Появилось сообщение об ошибке

    time.sleep(0.2)


@pytest.mark.parametrize("correct_code",
                         [True, False],
                         ids=['code correct',
                              'code incorrect'
                              ])
def test_auth_code(web_browser, correct_code, mail="skiltest.test@mail.ru", mail_pwd="Skilfactory"):
    """ Тест входа по временному коду

    Примечание: Если вдруг на сайте включается капча, то пользователю необходимо ввести её вручную. """
    page_rt = AuthPage(web_browser, url='https://lk.rt.ru')
    time.sleep(0.5)
    page_rt.wait_page_loaded()  # Ждем загрузки
    wh_rt = web_browser.current_window_handle

    # Открываем mail.ru в новой вкладке
    web_browser.switch_to.new_window('tab')
    page_mail = AuthMailPage(web_browser)
    time.sleep(0.5)
    wh_mail = web_browser.current_window_handle
    page_mail.wait_page_loaded()

    # Скидываем чекбокс запомнить
    if page_mail.box_remember.get_attribute("data-checked") == 'true':
        page_mail.box_remember.click()

    # Вводим логин\пароль, заходим
    page_mail.login_input.send_keys(mail)
    page_mail.btn_next.click()
    page_mail.wait_page_loaded()

    page_mail.pass_input.send_keys(mail_pwd)
    page_mail.btn_enter.click()
    page_mail.wait_page_loaded()

    # Очищаем ящик, если в нем есть письма
    if page_mail.btn_inbox.get_attribute("title") != "Входящие, нет писем":
        page_mail.btn_inbox.right_mouse_click()
        page_mail.menu_clear_all.click()
        page_mail.btn_confirm_clear.click()

    time.sleep(0.3)

    # Возвращаемся на страницу авторизации
    web_browser.switch_to.window(wh_rt)

    time.sleep(0.5)

    # Вводим почту
    page_rt.login_code_input.send_keys(mail)

    # Если появилась капча, ждем пока её введут
    if page_rt.captcha_img.is_presented():
        i = 10

        captcha = page_rt.captcha_data.get_attribute('innerHTML')
        while i:
            time.sleep(10)
            if captcha == page_rt.captcha_data.get_attribute('innerHTML'):
                break
            captcha = page_rt.captcha_data.get_attribute('innerHTML')
            i -= 1

    # Если появился таймер запрета повторной отправки кода
    i = 120
    while i and not page_rt.input_ot_code.is_presented():
        page_rt.btn_get_code.click()
        time.sleep(1)
        i -= 1

    # Возвращаемся на страницу почты
    web_browser.switch_to.window(wh_mail)

    # Ждем письма с кодом
    i = 120
    while i and not (page_mail.first_mail_content.is_presented()):
        time.sleep(1)
        i -= 1

    # Копируем код
    code = page_mail.first_mail_content.get_text()
    code = code[9:15]

    # Возвращаемся на страницу авторизации
    web_browser.switch_to.window(wh_rt)

    # Водим код
    if correct_code:  # Тест корректного кода
        page_rt.input_ot_code.send_keys(code)
        page_rt.wait_page_loaded()

        # При первом входе по коду может быть нужно подтверждение
        if page_rt.btn_enter_ot.is_presented():
            page_rt.btn_enter_ot.click()
            page_rt.wait_page_loaded()

        # Проверяем, что зашли
        assert page_rt.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:  # Тест некорректного кода
        wrong_code = code

        while wrong_code == code:  # Портим код
            digit = randrange(10)
            wrong_code = str(digit) + code[1:len(code)]

        page_rt.input_ot_code.send_keys(wrong_code)
        assert page_rt.span_wrong_code.is_presented()

    time.sleep(0.3)
