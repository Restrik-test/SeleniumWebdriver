import unittest

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.cart_page import CartPage
from pageobjects.product_page import ProductPage


class ShoppingCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.hp_product = ProductPage(self.driver, '47')
        self.samsung_product = ProductPage(self.driver, '33')
        self.cart = CartPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_product_page(self):
        """Завдання № 5. Додавання продуктів у кошик"""

        self.samsung_product.open()
        product1 = self.samsung_product.get_name_product()
        self.samsung_product.clear_qty()
        self.samsung_product.input_qty('2')
        self.samsung_product.add_to_cart_click()
        self.assertEqual('Success: You have added Samsung SyncMaster 941BW to your shopping cart!',
                         self.samsung_product.get_alert())

        self.hp_product.open()
        product2 = self.hp_product.get_name_product()
        self.hp_product.add_to_cart_click()
        self.assertEqual('Success: You have added HP LP3065 to your shopping cart!',
                         self.samsung_product.get_alert())

        self.cart.open()

        # Перевіряю чи відповідають назви продуктів у кошику продуктам, які були додані
        products = self.cart.get_products()
        print(products[1].name)
        print(products[0].name)
        for product in self.cart.get_products():
            assert product.name in (product1, product2)


