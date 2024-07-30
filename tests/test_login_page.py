from pages.login_page import LoginPage


def test_buy_product(set_up):
    driver = set_up

    lp = LoginPage(driver, LoginPage.URL)
    lp.open_login_page()
