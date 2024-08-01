from selenium.common import TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

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

    def assert_url_on_opened_tab(self, expected_url: str):
        """Method to assert URL on new opened windows"""
        new_window = self.driver.window_handles[1]
        try:
            self.driver.switch_to.window(new_window)
        except NoSuchWindowException:
            raise AssertionError("No new windows are open!")
        self.assert_url(expected_url)

    def assert_element_text_value(self, actual_value: WebElement, expected_value: str):
        """Method to assert text value"""
        assert actual_value.text == expected_value, (
            f"Incorrect element text value, expected value - {expected_value}, "
            f"but is - {actual_value.text}")

    # Burger menu locators and methods
    # URL
    SAUCE_LABS_URL = "https://saucelabs.com/"

    # Locators
    BURGER_MENU_ICON = (By.CLASS_NAME, "bm-burger-button")
    LOGOUT_SIDEBAR_LINK = (By.ID, "logout_sidebar_link")
    ABOUT_SIDEBAR_LINK = (By.ID, "about_sidebar_link")

    # Getters
    def get_burger_menu_icon(self):
        return self.wait_for_element_is_clickable(self.BURGER_MENU_ICON)

    def get_logout_sidebar_link(self):
        return self.wait_for_element_is_clickable(self.LOGOUT_SIDEBAR_LINK)

    def get_about_sidebar_link(self):
        return self.wait_for_element_is_clickable(self.ABOUT_SIDEBAR_LINK)

    # Actions
    def click_burger_menu_icon(self):
        self.get_burger_menu_icon().click()

    def click_logout_sidebar_link(self):
        self.get_logout_sidebar_link().click()

    def click_about_sidebar_link(self):
        self.get_about_sidebar_link().click()

    # Methods
    def logout_from_swag_labs(self):
        self.click_burger_menu_icon()
        self.click_logout_sidebar_link()
        self.assert_url("https://www.saucedemo.com/")

    def go_to_sauce_labs_site(self):
        self.click_burger_menu_icon()
        self.click_about_sidebar_link()
        self.assert_url(self.SAUCE_LABS_URL)

    # Footer locators and methods
    # Social URLs
    SAUCE_LABS_X_URL = "https://x.com/saucelabs"
    SAUCE_LABS_FACEBOOK_URL = "https://www.facebook.com/saucelabs"
    SAUCE_LABS_LINKEDIN_URL = "https://www.linkedin.com/company/sauce-labs/"

    # Locators
    FOOTER_SAUCE_LABS_X_ICON = (By.XPATH, "//a[@data-test='social-twitter']")
    FOOTER_SAUCE_LABS_FACEBOOK_ICON = (By.XPATH, "//a[@data-test='social-facebook']")
    FOOTER_SAUCE_LABS_LINKEDIN_ICON = (By.XPATH, "//a[@data-test='social-linkedin']")

    # Getters
    def get_footer_sause_labs_x_icon(self):
        return self.wait_for_element_is_visible(self.FOOTER_SAUCE_LABS_X_ICON)

    def get_footer_sauce_labs_facebook_icon(self):
        return self.wait_for_element_is_visible(self.FOOTER_SAUCE_LABS_FACEBOOK_ICON)

    def get_footer_sauce_labs_linkedin_icon(self):
        return self.wait_for_element_is_visible(self.FOOTER_SAUCE_LABS_LINKEDIN_ICON)

    # Actions
    def click_footer_sauce_labs_x_icon(self):
        self.get_footer_sause_labs_x_icon().click()

    def click_footer_sauce_labs_facebook_icon(self):
        self.get_footer_sauce_labs_facebook_icon().click()

    def click_footer_sauce_labs_linkedin_icon(self):
        self.get_footer_sauce_labs_linkedin_icon().click()

    # Methods
    def go_to_sauce_labs_x_social_media(self):
        self.click_footer_sauce_labs_x_icon()
        self.assert_url_on_opened_tab(self.SAUCE_LABS_X_URL)

    def go_to_sauce_labs_facebook_social_media(self):
        self.click_footer_sauce_labs_facebook_icon()
        self.assert_url_on_opened_tab(self.SAUCE_LABS_FACEBOOK_URL)

    def go_to_sauce_labs_linkedin_social_media(self):
        self.click_footer_sauce_labs_linkedin_icon()
        self.assert_url_on_opened_tab(self.SAUCE_LABS_LINKEDIN_URL)
