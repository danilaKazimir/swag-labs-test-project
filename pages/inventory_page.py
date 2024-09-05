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

    def check_product_add_to_card_or_remove_button_text(self, product_name: str, expected_text: str):
        button_element = self.product_values.get_product_elements_from_page(product_name)["button"]
        self.assert_element_text_value(button_element, expected_text)

    def click_on_product_add_to_card_or_remove_button(self, product_name: str):
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
        self.check_product_add_to_card_or_remove_button_text(product_name, "Add to cart")
        self.click_on_product_add_to_card_or_remove_button(product_name)
        self.check_product_add_to_card_or_remove_button_text(product_name, "Remove")
        self.assert_element_text_value(self.get_shopping_cart_badge(), expected_cart_badge_count)

    def add_multiple_products_to_shopping_cart(self, count_of_product_to_add):
        products_names = self.product_values.get_all_products_info_from_json()
        for i in range(0, count_of_product_to_add):
            product_name = tuple(products_names.items())[i][1]["name"]
            self.add_product_to_shopping_cart(product_name, str(i + 1))

    def remove_product_from_shopping_cart(self, product_name: str):
        self.check_product_add_to_card_or_remove_button_text(product_name, "Remove")
        self.click_on_product_add_to_card_or_remove_button(product_name)
        self.check_product_add_to_card_or_remove_button_text(product_name, "Add to cart")
        self.wait_for_element_is_not_visible(self.SHOPPING_CART_BADGE)
