from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from pageobjects.base_page import BasePage


class ComparisonPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/compare'

    def get_table(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'table')

    def get_rows(self) -> list:
        return self.get_table().find_elements(By.TAG_NAME, 'tr')

    def find_product_names(self, product_names: list) -> list:
        found_products = []

        for row in self.get_rows():
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                if cell.text in product_names:
                    found_products.append(cell.text)
        return found_products

    def remove_all_products(self):
        while True:
            remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn-danger')
            if not remove_buttons:
                break
            remove_buttons[0].click()
        WebDriverWait(self.driver, 10).until_not(visibility_of_element_located((By.CLASS_NAME, 'table')))

    def get_content_text(self) -> str:
        content_text = self.driver.find_element(By.ID, 'content')
        return content_text.text
