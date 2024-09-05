import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestSuccessfulLogin:
    def test_successful_login_into_swag_labs(self, set_up):
        browser = LoginPage(set_up)
        browser.open_login_page()
        browser.fill_fields_and_click_on_login_button("standard_user", "secret_sauce")
        browser.assert_url(InventoryPage.URL)


class TestsUnsuccessfulLogin:
    INVALID_LOGIN_DATA = (
        ("", ""),
        ("", "secret_sauce"),
        ("standard_user", ""),
        ("invalid_login", "secret_sauce"),
        ("standard_user", "invalid_password"),
        ("invalid_login", "invalid_password)"),
        ("locked_out_user", "secret_sauce")
    )
    ERROR_MESSAGES = {
        "Username isn't filled": "Epic sadface: Username is required",
        "Password isn't filled": "Epic sadface: Password is required",
        "Incorrect login values": "Epic sadface: Username and password do not match any user in this service",
        "Locked user": "Epic sadface: Sorry, this user has been locked out."
    }

    @pytest.mark.parametrize('username, password', INVALID_LOGIN_DATA)
    def test_error_message_during_login(self, set_up, username, password):
        browser = LoginPage(set_up)
        browser.open_login_page()
        browser.fill_fields_and_click_on_login_button(username, password)
        if username == "":
            expected_error = TestsUnsuccessfulLogin.ERROR_MESSAGES["Username isn't filled"]
        elif password == "" and username != "":
            expected_error = TestsUnsuccessfulLogin.ERROR_MESSAGES["Password isn't filled"]
        elif username == "locked_out_user" and password == "secret_sauce":
            expected_error = TestsUnsuccessfulLogin.ERROR_MESSAGES["Locked user"]
        else:
            expected_error = TestsUnsuccessfulLogin.ERROR_MESSAGES["Incorrect login values"]
        browser.check_error_message_is_correct(expected_error)
