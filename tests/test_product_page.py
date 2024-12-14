import unittest

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.product_page import ProductPage


class ProductPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_page = ProductPage(self.driver, '42')
        self.product_page.open()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_product_page(self):
        """Завдання № 1. Тестування сторінки продукту"""

        self.assertEqual(
            'Apple Cinema 30"',
            self.product_page.get_name_product()
        )

        self.assertEqual(
            'Apple',
            self.product_page.get_brand_product()
        )

        self.assertEqual(
            'Product 15',
            self.product_page.get_code_product()
        )

        self.assertEqual(
            110.00,
            self.product_page.get_price_product()
        )

        self.assertTrue(
            'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution' in
            self.product_page.get_description_product()
        )

