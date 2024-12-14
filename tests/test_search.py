import unittest
from _decimal import Decimal
from typing import List

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.search_page import SearchPage
from pageobjects.search_page import ProductInfo


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.open()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_product_page(self):
        """Завдання № 2. Тестування пошуку"""

        self.search_page.input_search('apple')
        self.search_page.click_search_button()

        products: List[ProductInfo] = self.search_page.get_search_results()
        names: List[str] = [product.name for product in products]
        prices: List[Decimal] = [product.price for product in products]

        self.assertTrue('Apple Cinema 30"' in names)
        self.assertTrue(110.00 in prices)

        self.search_page.clear_search()

        self.search_page.input_search('sony')
        self.search_page.click_search_button()

        products: List[ProductInfo] = self.search_page.get_search_results()
        names: List[str] = [product.name for product in products]
        prices: List[Decimal] = [product.price for product in products]

        self.assertTrue('Sony VAIO' in names)
        self.assertTrue(1202.00 in prices)

        self.search_page.clear_search()

        self.search_page.input_search('nokia')
        self.search_page.click_search_button()

        self.assertTrue('There is no product that matches the search criteria.' in self.search_page.get_content_text())
