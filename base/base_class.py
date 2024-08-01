from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def wait_for_element_is_clickable(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """Method to wait until the element becomes clickable"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator}' isn't clickable within {timeout} seconds")

    def wait_for_element_is_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """Method to wait until the element becomes visible"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator '{locator}' isn't visible within {timeout} seconds")

    def assert_url(self, expected_url: str):
        """Method to assert URL"""
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL isn't correct, expected url - {expected_url}, but is - {current_url}"

    def assert_element_text_value(self, actual_value: WebElement, expected_value: str):
        """Method to assert text value"""
        assert actual_value.text == expected_value, (f"Incorrect element text value, expected value - {expected_value}, "
                                                     f"but is - {actual_value.text}")
