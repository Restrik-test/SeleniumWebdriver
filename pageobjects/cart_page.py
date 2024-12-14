from decimal import Decimal
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from pageobjects.base_page import BasePage, extract_decimal_price


@dataclass
class Product:
    name: str
    model: str
    quantity: str
    unit_price: Decimal
    total: Decimal


class CartPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=checkout/cart'

    def get_table(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'table-responsive')

    def get_rows(self) -> list:
        return self.get_table().find_elements(By.TAG_NAME, 'tr')[1:]

    def get_products(self):
        products = []

        for row in self.get_rows():
            cells = row.find_elements(By.TAG_NAME, "td")
            name = cells[1].text.split("\n")[0].strip()
            model = cells[2].text.strip()
            quantity = cells[3].find_element(By.TAG_NAME, "input").get_attribute("value").strip()
            unit_price = cells[4].text.strip()
            total = cells[5].text.strip()

            product = Product(
                name=name,
                model=model,
                quantity=quantity,
                unit_price=Decimal(extract_decimal_price(unit_price)),
                total=Decimal(extract_decimal_price(total))
            )

            # product = Product(name, model, quantity, unit_price, total)
            products.append(product)
        return products

    def remove_all_products(self):
        while True:
            remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn-danger')
            if not remove_buttons:
                break
            remove_buttons[0].click()
        WebDriverWait(self.driver, 10).until_not(visibility_of_element_located((By.CLASS_NAME, 'table')))

    def check_no_products_message(self):
        content = self.driver.find_element(By.ID, 'content')
        assert 'Your shopping cart is empty!' in content.text
