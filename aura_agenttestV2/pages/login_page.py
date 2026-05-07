from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    USER_INPUT = "#username"
    PWD_INPUT = "#password"
    SUBMIT_BTN = 'button[type="submit"]'
    FLASH_MSG = "#flash"

    def load(self):
        self.open(self.URL)

    def input_username(self, username):
        self.fill(self.USER_INPUT, username)

    def input_password(self, pwd):
        self.fill(self.PWD_INPUT, pwd)

    def submit(self):
        self.click(self.SUBMIT_BTN)

    def get_flash(self):
        return self.get_text(self.FLASH_MSG)