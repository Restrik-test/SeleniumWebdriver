from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self) -> str:
        raise NotImplementedError

    def open(self):
        self.driver.get(self.get_url())
