import unittest
import string
import random

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.product_page import ProductPage


def generate_random_string_with_symbols(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


class AddReviewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_page = ProductPage(self.driver, '42')
        self.product_page.open()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_review(self):
        """Завдання № 3. Тестування додавання відгуку на продукт"""

        self.product_page.reviews_tab_click()
        self.product_page.button_continue_click()
        self.assertEqual('Warning: Please select a review rating!', self.product_page.get_alert())

        self.product_page.select_rating('3')
        self.product_page.input_your_name('John')
        random_text = generate_random_string_with_symbols(24)
        self.product_page.input_your_review(random_text)
        self.product_page.button_continue_click()
        self.assertEqual('Warning: Review Text must be between 25 and 1000 characters!',
                         self.product_page.get_alert())

        random_text = generate_random_string_with_symbols(25)
        self.product_page.clear_your_review()
        self.product_page.input_your_review(random_text)
        self.product_page.button_continue_click()
        self.assertEqual('Thank you for your review. It has been submitted to the webmaster for approval.',
                         self.product_page.get_alert())

        self.product_page.select_rating('5')
        self.product_page.input_your_name('John')
        random_text = generate_random_string_with_symbols(1001)
        self.product_page.input_your_review(random_text)
        self.product_page.button_continue_click()
        self.assertEqual('Warning: Review Text must be between 25 and 1000 characters!',
                         self.product_page.get_alert())
