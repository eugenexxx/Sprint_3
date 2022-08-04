from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.user_profile_locators import UserProfile
import logging

LOGGER = logging.getLogger(__name__)


class UserProfileActions:

    def __init__(self, app):
        self.app = app

    def click_constructor_button(self):
        # Кликаем по кнопке "Конструктор"
        LOGGER.info('Кликаем по кнопке "Конструктор"')
        self.app.driver.find_element("xpath", UserProfile.constructor_button).click()

    def click_header_logo(self):
        # Кликаем по логотипу в хедере
        LOGGER.info('Кликаем по логотипу в хедере')
        self.app.driver.find_element("xpath", UserProfile.header_logo).click()

    def click_sign_out(self):
        # Нажимаем кнопку "Выход"
        LOGGER.info('Нажимаем кнопку "Выход"')
        self.app.driver.find_element("xpath", UserProfile.sign_out_button).click()

    def check_constructor_is_active(self):
        # Проверяем, что активна вкладка "Конструктор"
        LOGGER.info('Проверяем, что активна вкладка "Конструктор"')
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, UserProfile.constructor_button_active)))
        except AssertionError:
            LOGGER.info('Вкладка "Конструктор" не активна!')
