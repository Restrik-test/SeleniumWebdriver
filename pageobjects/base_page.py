from decimal import Decimal
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver


def extract_decimal_price(text: str) -> Decimal:
    split_by_lines: List[str] = text.split('\n')
    first_price_lines = split_by_lines[0].split(' ')
    first_price = first_price_lines[0][1:]
    first_price_without_punctuation = first_price.replace(',', '')
    return Decimal(first_price_without_punctuation)


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self) -> str:
        raise NotImplementedError

    def open(self):
        self.driver.get(self.get_url())

    def extract_decimal_price(self, text: str) -> Decimal:
        split_by_lines: List[str] = text.split('\n')
        first_price_lines = split_by_lines[0].split(' ')
        first_price = first_price_lines[0][1:]
        first_price_without_punctuation = first_price.replace(',', '')
        return Decimal(first_price_without_punctuation)


