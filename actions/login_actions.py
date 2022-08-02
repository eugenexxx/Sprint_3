from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_locators import Login
import logging

LOGGER = logging.getLogger(__name__)


class LoginOptionsActions:

    def __init__(self, app):
        self.app = app

    def click_login_button(self):
        # Кликаем по кнопке "Войти в аккаунт" на главной странице сайта
        LOGGER.info('Кликаем по кнопке "Войти в аккаунт" на главной странице сайта')
        self.app.driver.find_element("xpath", Login.login_button).click()

    def click_user_profile_button(self):
        # Кликаем по кнопке "Личный кабинет" на главной странице сайта
        LOGGER.info('Кликаем по кнопке "Личный кабинет" на главной странице сайта')
        self.app.driver.find_element("xpath", Login.user_profile_button).click()

    def click_login_button_on_registration_form(self):
        # Кликаем по кнопке "Войти" на странице регистрации
        LOGGER.info('Кликаем по кнопке "Войти" на странице регистрации')
        self.app.driver.find_element("xpath", Login.registration_form_login_button).click()

    def click_login_button_on_forgot_password_form(self):
        # Кликаем по кнопке "Войти" на странице "Восстановить пароль"
        LOGGER.info('Кликаем по кнопке "Войти" на странице "Восстановить пароль"')
        self.app.driver.find_element("xpath", Login.registration_form_login_button).click()

    def check_user_is_redirected_to_the_login_screen(self):
        # Проверяем, что юзер перешел на страницу авторизации ("Вход")
        LOGGER.info('Проверяем, что юзер перешел на страницу авторизации.')
        login_url = "https://stellarburgers.nomoreparties.site/login"
        wait = WebDriverWait(self.app.driver, 60)
        try:
            wait.until(EC.url_to_be(login_url))
            LOGGER.info("Страница авторизации загрузилась!")
        except AssertionError:
            LOGGER.info("Страница авторизации не отображена!")

    def login_in_system(self, email, password):
        # Заполняем форму авторизации
        LOGGER.info(f'Вводим email в поле "Email": {email}')
        self.app.driver.find_element("xpath", Login.email_field).send_keys(email)
        LOGGER.info(f'Вводим пароль в поле "Password": {password}')
        self.app.driver.find_element("xpath", Login.password_field).send_keys(password)
        # Нажимаем кнопку "Войти"
        LOGGER.info('Нажимаем кнопку "Войти"')
        self.app.driver.find_element("xpath", Login.login_form_button).click()
        wait = WebDriverWait(self.app.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, Login.homepage_title)))

    def open_user_profile_on_homepage(self):
        homepage_url = "https://stellarburgers.nomoreparties.site/"
        user_profile_page_url = "https://stellarburgers.nomoreparties.site/account/profile"
        if self.app.driver.current_url == homepage_url:
            LOGGER.info('Нажимаем на кнопку "Личный кабинет" и проверяем, что страница "Личный кабинет" отобразилась.')
            self.app.driver.find_element("xpath", Login.user_profile_button).click()
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, Login.profile_tab_title)))
            assert self.app.driver.current_url == user_profile_page_url, "Личный кабинет не отобразился!"
        else:
            raise Exception("Пользователь находится не на главной странице")

    def check_correct_user_is_authorized_in_system(self, email):
        # Проверяем email авторизованного юзера в личном кабинете
        LOGGER.info('Проверяем email авторизованного юзера в личном кабинете')
        email_xpath = f"//input[@value='{email}']"
        self.app.driver.find_element("xpath", email_xpath)
        LOGGER.info("Пользователь авторизован верно!")
