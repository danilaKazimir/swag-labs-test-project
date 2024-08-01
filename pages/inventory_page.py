from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.get_product_values import ProductValues


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_values = ProductValues(driver)

    # PAGE URL
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    SWAG_LABS_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART_ICON = (By.XPATH, "//a[@data-test='shopping-cart-link']")

    # Getters
    def get_swag_labs_logo(self):
        return self.wait_for_element_is_visible(self.SWAG_LABS_LOGO)

    def get_shopping_cart_icon(self):
        return self.wait_for_element_is_clickable(self.SHOPPING_CART_ICON)

        # Actions

    def click_on_shopping_cart_icon(self):
        self.get_shopping_cart_icon().click()

    # Methods
    def open_shopping_cart(self):
        self.click_on_shopping_cart_icon()
