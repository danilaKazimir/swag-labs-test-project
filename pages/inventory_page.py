from selenium.webdriver.common.by import By
from base.base_class import Base


class InventoryPage(Base):
    # PAGE URL
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    SWAG_LABS_LOGO = (By.CLASS_NAME, "app_logo")

    # Getters
    def get_swag_labs_logo(self):
        return self.wait_for_element_is_visible(self.SWAG_LABS_LOGO)

    # Actions

    # Methods

