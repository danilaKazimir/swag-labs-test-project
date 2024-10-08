import json

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductValues(BasePage):
    FILE_PATH = "data/swag_labs_products.json"

    def get_all_products_info_from_json(self):
        with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
            products_data = json.load(file)
        return products_data

    def get_product_info_from_json(self, product_name):
        with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
            product_data = json.load(file)[product_name]
        return product_data

    def get_product_elements_from_page(self, product_name):
        item_name_xpath = (By.XPATH, f"//div[text() = '{product_name}']")
        item_desc_xpath = (
            By.XPATH, f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]"
                      "//div[@data-test='inventory-item-desc']")
        item_price_xpath = (By.XPATH,
                            f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]//div[@data-test='inventory-item-price']")
        item_img_url_xpath = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div"
                                        "[contains(@class, 'inventory_item')]//img")
        item_button_xpath = (
            By.XPATH, f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]//button")

        item_name = self.wait_for_element_is_visible(item_name_xpath)
        item_desc = self.wait_for_element_is_visible(item_desc_xpath)
        item_price = self.wait_for_element_is_visible(item_price_xpath)
        item_img_url = self.wait_for_element_is_visible(item_img_url_xpath)
        item_button_element = self.wait_for_element_is_clickable(item_button_xpath)

        product_info = {
            "name": item_name,
            "description": item_desc,
            "price": item_price,
            "image": item_img_url,
            "button": item_button_element
        }

        return product_info
