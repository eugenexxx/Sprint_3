from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constructor_locators import Constructor
import logging

LOGGER = logging.getLogger(__name__)


class ConstructorActions:

    def __init__(self, app):
        self.app = app

    def click_bun_button(self):
        # Кликаем в "Конструктор" по вкладке "Булки"
        LOGGER.info('Кликаем в "Конструктор" по вкладке "Булки"')
        self.app.driver.find_element("xpath", Constructor.bun_tab_button).click()

    def click_sauce_button(self):
        # Кликаем в "Конструктор" по вкладке "Соусы"
        LOGGER.info('Кликаем в "Конструктор" по вкладке "Соусы"')
        self.app.driver.find_element("xpath", Constructor.sauce_tab_button).click()

    def click_stuffing_button(self):
        # Кликаем в "Конструктор" по вкладке "Начинки"
        LOGGER.info('Кликаем в "Конструктор" по вкладке "Начинки"')
        self.app.driver.find_element("xpath", Constructor.stuffing_tab_button).click()

    def check_bun_tab_is_active(self):
        # Проверяем, что активна вкладка "Булки"
        LOGGER.info('Проверяем, что активна вкладка "Булки"')
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, Constructor.bun_tab_active)))
        except AssertionError:
            LOGGER.info('Вкладка "Булки" не активна!')

    def check_sauce_tab_is_active(self):
        # Проверяем, что активна вкладка "Соусы"
        LOGGER.info('Проверяем, что активна вкладка "Соусы"')
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, Constructor.sauce_tab_active)))
        except AssertionError:
            LOGGER.info('Вкладка "Соусы" не активна!')

    def check_stuffing_tab_is_active(self):
        # Проверяем, что активна вкладка "Начинки"
        LOGGER.info('Проверяем, что активна вкладка "Начинки"')
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, Constructor.stuffing_tab_active)))
        except AssertionError:
            LOGGER.info('Вкладка "Начинки" не активна!')
