from selenium.webdriver.common.by import By

from base.base_class import Base


class LoginPage(Base):
    # PAGE URL
    URL = "https://www.saucedemo.com/"

    # Locators

    # Getters

    # Actions

    # Methods
    def open_login_page(self):
        self.driver.get(self.URL)
