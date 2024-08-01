# import json
#
#
# # Функция для загрузки данных из файла JSON
# def load_json_file(file_path):
#     """Загружает JSON-данные из указанного файла и возвращает их как словарь Python."""
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data
#
#
# file_path = 'data/swag_labs_products.json'
#
# products = load_json_file(file_path)
#

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductValues(BasePage):
    def get_product_info(self, product_name):
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

        item_name = self.wait_for_element_is_visible(item_name_xpath).text
        item_desc = self.wait_for_element_is_visible(item_desc_xpath).text
        item_price = self.wait_for_element_is_visible(item_price_xpath).text
        item_img_url = self.wait_for_element_is_visible(item_img_url_xpath).get_attribute("src")
        item_button_element = self.wait_for_element_is_clickable(item_button_xpath)

        product_info = {
            "name": item_name,
            "description": item_desc,
            "price": item_price,
            "image": item_img_url,
            "button": item_button_element
        }

        return product_info
