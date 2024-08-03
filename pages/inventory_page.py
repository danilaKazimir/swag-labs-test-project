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
    SHOPPING_CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge']")

    # Getters
    def get_swag_labs_logo(self):
        return self.wait_for_element_is_visible(self.SWAG_LABS_LOGO)

    def get_shopping_cart_icon(self):
        return self.wait_for_element_is_clickable(self.SHOPPING_CART_ICON)

    def get_shopping_cart_badge(self):
        return self.wait_for_element_is_visible(self.SHOPPING_CART_BADGE)

    # Actions
    def click_on_shopping_cart_icon(self):
        self.get_shopping_cart_icon().click()

    def click_on_product_add_to_card_button(self, product_name: str):
        button_element = self.product_values.get_product_elements_from_page(product_name)["button"]
        button_element.click()

    def click_on_product_item_name_link(self, product_name: str):
        item_name_link = self.product_values.get_product_elements_from_page(product_name)["name"]
        item_name_link.click()

    # Methods
    def open_shopping_cart(self):
        self.click_on_shopping_cart_icon()

    def check_product_value(self, product_name: str):
        actual_product_value = self.product_values.get_product_elements_from_page(product_name)
        expected_product_value = self.product_values.get_product_info_from_json(product_name)

        self.assert_element_text_value(actual_product_value["name"], expected_product_value["name"])
        self.assert_element_text_value(actual_product_value["description"], expected_product_value["description"])
        self.assert_element_text_value(actual_product_value["price"], expected_product_value["price"])
        self.assert_element_attribute_value("src", actual_product_value["image"], expected_product_value["image"])

    def open_product_page(self, product_name: str):
        product_id = self.product_values.get_product_info_from_json(product_name)["id"]

        self.click_on_product_item_name_link(product_name)
        # TO DO: Make URL as constant for inventory item page
        self.assert_url(f"https://www.saucedemo.com/inventory-item.html?id={product_id}")

    def add_product_to_shopping_cart(self, product_name: str, expected_cart_badge_count: str):
        self.click_on_product_add_to_card_button(product_name)
        self.assert_element_text_value(self.get_shopping_cart_badge(), expected_cart_badge_count)
