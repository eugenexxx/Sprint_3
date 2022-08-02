class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self, link):
        driver = self.app.driver
        driver.maximize_window()
        driver.get("https://stellarburgers.nomoreparties.site" + link)
        driver.implicitly_wait(60)
