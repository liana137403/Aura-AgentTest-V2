from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.load()
    login.input_username("tomsmith")
    login.input_password("SuperSecretPassword!")
    login.submit()
    assert "You logged into a secure area" in login.get_flash()