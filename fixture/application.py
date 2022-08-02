from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fixture.session import SessionHelper
from actions.registration_actions import RegistrationActions
from actions.login_actions import LoginOptionsActions
from actions.user_profile_actions import UserProfileActions
from actions.constructor_actions import ConstructorActions


class Application:

    def __init__(self):
        path = '/Users/admin/WebDriver/bin/chromedriver'
        s = Service(path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.registration_actions = RegistrationActions(self)
        self.login_actions = LoginOptionsActions(self)
        self.profile_actions = UserProfileActions(self)
        self.constructor_actions = ConstructorActions(self)

    def destroy(self):
        self.driver.quit()
