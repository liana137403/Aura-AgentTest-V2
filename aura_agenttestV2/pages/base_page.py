class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def click(self, selector):
        self.page.locator(selector).click()

    def get_text(self, selector):
        return self.page.locator(selector).text_content().strip()