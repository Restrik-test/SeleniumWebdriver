from _decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element

from pageobjects.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, page_id: str):
        super().__init__(driver)
        self.driver = driver
        self.page_id = page_id

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/product&product_id=' + self.page_id

    def get_list_info(self) -> WebElement:
        info_panel = self.driver.find_element(By.ID, 'content').find_element(By.CLASS_NAME, 'col-sm-4')
        list_info = info_panel.find_elements(By.CLASS_NAME, 'list-unstyled')
        return list_info[0]

    def get_name_product(self) -> str:
        return self.driver.find_element(By.TAG_NAME, 'H1').text

    def get_brand_product(self) -> str:
        elements = self.get_list_info().find_elements(By.TAG_NAME, 'li')
        brand_product_line = elements[0].text
        brand_product = brand_product_line.split(': ')
        return brand_product[1]

    def get_code_product(self) -> str:
        elements = self.get_list_info().find_elements(By.TAG_NAME, 'li')
        code_product_line = elements[1].text
        code_product = code_product_line.split(': ')
        return code_product[1]

    def get_price_product(self) -> Decimal:
        info_panel = self.driver.find_element(By.ID, 'content').find_element(By.CLASS_NAME, 'col-sm-4')
        list_info2 = info_panel.find_elements(By.CLASS_NAME, 'list-unstyled')
        price_line = list_info2[1].find_element(By.TAG_NAME, 'H2')
        price_text = price_line.text[1:]
        price_without_punctuation = price_text.replace(',', '')
        return Decimal(price_without_punctuation)

    def get_qty_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-quantity')

    def get_description_product(self) -> str:
        return self.driver.find_element(By.ID, 'tab-description').text

    def get_your_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-name')

    def get_your_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-review')

    def get_alert(self) -> str:
        element = WebDriverWait(self.driver, 10).until(visibility_of_element_located((
            By.CLASS_NAME, 'alert-dismissible')))
        alert = element.text.split('\n×')
        return alert[0]

    def input_qty(self, number: str):
        self.get_qty_field().send_keys(number)

    def clear_qty(self):
        self.get_qty_field().clear()

    def add_to_cart_click(self):
        self.driver.find_element(By.ID, 'button-cart').click()
        self.driver.find_element(By.ID, 'button-cart').click()
        WebDriverWait(self.driver, 10).until_not(text_to_be_present_in_element((
            By.ID, 'button-cart'), 'Loading...'))

    def reviews_tab_click(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reviews').click()

    def input_your_name(self, name: str):
        self.get_your_name_field().send_keys(name)

    def clear_your_name(self):
        self.get_your_name_field().clear()

    def input_your_review(self, review: str):
        self.get_your_review_field().send_keys(review)

    def clear_your_review(self):
        self.get_your_review_field().clear()

    def select_rating(self, value):
        self.driver.find_element(By.CSS_SELECTOR, f"input[type='radio'][name='rating'][value='{value}']").click()

    def button_continue_click(self):
        self.driver.find_element(By.ID, 'button-review').click()
        WebDriverWait(self.driver, 10).until_not(text_to_be_present_in_element((
            By.ID, 'button-review'), 'Loading...'))

    def button_compare_click(self):
        self.driver.find_element(By.CLASS_NAME, 'fa-exchange').click()

    def link_product_comparison_click(self):
        element = WebDriverWait(self.driver, 10).until(visibility_of_element_located((
            By.LINK_TEXT, 'product comparison')))
        element.click()

