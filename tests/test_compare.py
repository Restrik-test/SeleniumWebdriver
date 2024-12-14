import unittest

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.comparison_page import ComparisonPage
from pageobjects.product_page import ProductPage

product_names = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']


class CompareTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.apple_product = ProductPage(self.driver, '42')
        self.samsung_product = ProductPage(self.driver, '33')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_product_page(self):
        """Завдання № 4. Тестування порівняння продуктів"""

        self.apple_product.open()
        self.apple_product.button_compare_click()

        self.samsung_product.open()
        self.samsung_product.button_compare_click()

        self.samsung_product.link_product_comparison_click()

        # Перебираю всі комірки таблиці (<td>), щоб знайти текст продуктів
        self.product_comparison_page = ComparisonPage(self.driver)
        found_products = self.product_comparison_page.find_product_names(product_names)

        # Перевіряю, чи всі продукти знайдені
        for product in product_names:
            assert product in found_products

        self.product_comparison_page.remove_all_products()
        self.product_comparison_page.check_no_products_message()

