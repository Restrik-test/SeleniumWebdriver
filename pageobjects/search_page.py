from _decimal import Decimal
from dataclasses import dataclass
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobjects.base_page import BasePage
from helper import extract_decimal_price


@dataclass
class ProductInfo:
    name: str
    price: Decimal


class SearchPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def get_search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.ID, 'input-search')
        return search_field

    def get_search_button(self) -> WebElement:
        search_button = self.driver.find_element(By.ID, 'button-search')
        return search_button

    def get_description_search_checkbox(self) -> WebElement:
        description_checkbox = self.driver.find_element(By.ID, 'description')
        return description_checkbox

    def input_search(self, search_text: str):
        self.get_search_field().send_keys(search_text)

    def clear_search(self):
        self.get_search_field().clear()

    def click_search_button(self):
        self.get_search_button().click()

    def click_description_search_checkbox(self):
        self.get_description_search_checkbox().click()

    def get_search_results(self) -> List[ProductInfo]:
        products_tags = self.driver.find_elements(By.CLASS_NAME, 'product-layout')
        products: List[ProductInfo] = []

        for product_div_tag in products_tags:
            name: str = product_div_tag.find_element(By.TAG_NAME, 'H4').text
            price_text: str = product_div_tag.find_element(By.CLASS_NAME, 'price').text
            product = ProductInfo(
                name=name,
                price=Decimal(extract_decimal_price(price_text))
            )
            products.append(product)

        return products

    def get_content_text(self) -> str:
        content_text = self.driver.find_element(By.ID, 'content')
        return content_text.text
