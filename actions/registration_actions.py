from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registarion_form_locators import RegistrationForm
import logging
import random
import string

LOGGER = logging.getLogger(__name__)


class RegistrationActions:

    def __init__(self, app):
        self.app = app

    def fill_name_field(self, name=None):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        name_field = self.app.driver.find_element("xpath", RegistrationForm.name_field)

        # Если параметр "name" не передан - создаем рандомное имя юзера
        if name is None:
            LOGGER.info('Параметр "name" не передан, создаем рандомное имя')
            # Создаем случайное имя для поля "Имя"
            test_name = "User_" + random_string
            name_field.clear()
            LOGGER.info(f'Заполняем поле "Имя" используя сгенерированное значение: {test_name}')
            # Заполняем поле "Имя"
            name_field.send_keys(test_name)
        # Если параметр "name" передан
        elif name:
            # В поле "Имя" вводим значение параметра "name"
            name_field.clear()
            LOGGER.info(f'Параметр "name" передан, вводим значение параметра в поле "Имя": {name}')
            name_field.send_keys(name)

    def fill_email_field(self, email=None):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        email_field = self.app.driver.find_element("xpath", RegistrationForm.email_field)

        # Если параметр "email" не передан - создаем рандомный email
        if email is None:
            LOGGER.info('Параметр "email" не передан, создаем рандомный email')
            # Создаем случайный email для поля "Email"
            test_email = "user_" + random_string + "@" + random_string + ".com"
            email_field.clear()
            LOGGER.info(f'Заполняем поле "Email" используя сгенерированное значение: {test_email}')
            # Заполняем поле "Email"
            email_field.send_keys(test_email)
        # Если параметр "email" передан
        elif email:
            # В поле "Email" вводим значение параметра "email"
            email_field.clear()
            LOGGER.info(f'Параметр "email" передан, вводим значение параметра в поле "Email": {email}')
            email_field.send_keys(email)

    def fill_password_field(self, password=None):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
        password_field = self.app.driver.find_element("xpath", RegistrationForm.password_field)

        # Если параметр "password" не передан - создаем рандомный пароль
        if password is None:
            LOGGER.info('Параметр "password" не передан, создаем рандомный пароль')
            # Создаем случайный пароль для поля "Пароль"
            test_password = random_string
            password_field.clear()
            LOGGER.info(f'Заполняем поле "Пароль" используя сгенерированное значение: {test_password}')
            # Заполняем поле "Пароль"
            password_field.send_keys(test_password)
        # Если параметр "password" передан и его значение меньше 6 символов, проверяем что поле не проходит валидацию
        elif password and len(password) < 6:
            LOGGER.info('Параметр "password" передан и его значение меньше 6 символов')
            password_field.clear()
            LOGGER.info(f'Заполняем поле "Пароль" значением параметра "password": {password}')
            # Заполняем поле "Пароль"
            password_field.send_keys(password)
            LOGGER.info('Проверяем валидацию поля "Пароль"')
            # Проверяем валидацию поля "Пароль"
            self.app.driver.find_element("xpath", RegistrationForm.email_field).click()
            wait = WebDriverWait(self.app.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, RegistrationForm.password_validation_error)))
            raise Exception("Пароль не должен быть меньше 6 символов!")

        # Если параметр "password" передан и его значение больше 6 символов, проверяем что поле проходит валидацию
        elif password and len(password) > 6:
            LOGGER.info('Параметр "password" передан и его значение больше 6 символов')
            password_field.clear()
            LOGGER.info(f'Заполняем поле "Пароль" значением параметра "password": {password}')
            # Заполняем поле "Пароль"
            password_field.send_keys(password)

    # Нажать кнопку "Зарегистрироваться" и проверить, что юзер перешел на экран "Вход"
    def tap_registration_button_and_check_register_successfully(self):
        LOGGER.info('Нажать кнопку "Зарегистрироваться" и проверить, что юзер перешел на экран "Вход"')
        LOGGER.info('Нажать кнопку "Зарегистрироваться"')
        self.app.driver.find_element("xpath", RegistrationForm.registration_button).click()

        wait = WebDriverWait(self.app.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, RegistrationForm.enter_button)))
            LOGGER.info('Юзер перешел на экран "Вход"')
        except ValueError:
            wrong_input_error = wait.until(EC.visibility_of_element_located((By.XPATH, RegistrationForm.registration_failed_error)))
            if wrong_input_error:
                raise Exception("Неправильное имя пользователя или пароль!")
            else:
                raise Exception("Новый пользователь не создан!")
