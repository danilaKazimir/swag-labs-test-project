import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestBurgerMenu:
    def test_successful_logout(self, set_up):
        # TO DO: make fixture to login into swag labs app
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.logout_from_swag_labs()

    def test_about_link(self, set_up):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.go_to_sauce_labs_site()


class TestFooterLinks:
    def test_x_footer_link(self, set_up):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.go_to_sauce_labs_x_social_media()

    def test_facebook_footer_link(self, set_up):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.go_to_sauce_labs_facebook_social_media()

    def test_linkedin_footer_link(self, set_up):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.go_to_sauce_labs_linkedin_social_media()


@pytest.mark.parametrize("product", ("Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                                     "Sauce Labs Fleece Jacket", "Sauce Labs Onesie",
                                     "Test.allTheThings() T-Shirt (Red)"))
class TestSingleProduct:
    def test_check_product_values(self, set_up, product):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.check_product_value(product)

    def test_open_product_page(self, set_up, product):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.open_product_page(product)

    def test_add_single_product_to_cart(self, set_up, product):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.add_product_to_shopping_cart(product, "1")

    def test_remove_single_product_from_cart(self, set_up, product):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.add_product_to_shopping_cart(product, "1")
        ip.remove_product_from_shopping_cart(product)


@pytest.mark.parametrize("count", (2, 3, 4, 5, 6))
class TestMultipleProducts:
    def test_add_multiple_product_to_cart(self, set_up, count):
        driver = set_up

        lp = LoginPage(driver)
        lp.open_login_page()
        lp.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        lp.assert_url(InventoryPage.URL)

        ip = InventoryPage(driver)
        ip.add_multiple_products_to_shopping_cart(count)
