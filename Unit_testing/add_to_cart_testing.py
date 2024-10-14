import time
import unittest
from selenium import webdriver

from Pages.AddToCartPage import AddToCartPage


class AddToCartTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qaecoma.bishalkarki.xyz/index.php?id_category=3&controller=category")
        self.add_to_cart = AddToCartPage(self.driver)

    def test_scroll_and_add_first_item_to_cart(self):
        self.add_to_cart.scroll_to_first_item()
        self.add_to_cart.add_first_item_to_cart()

    def test_hover_add_to_cart_icon(self):
        self.add_to_cart.hover_to_cart_icon()
        cart_details = self.add_to_cart.get_cart_details()
        self.assertIn("Cart Details", cart_details)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()