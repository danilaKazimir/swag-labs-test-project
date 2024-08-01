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
