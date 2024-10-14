
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from Locators.AddToCartLocator import AddToCartLocator

class AddToCartPage:
    def __init__(self,driver):
        self.random = None
        self.driver = driver

    def find_cart_icon(self):
        return self.driver.find_element(By.XPATH, AddToCartLocator.cart_icon)
    
    def hover_to_cart_icon(self):
        icon = WebDriverWait(self.driver,10).until (
            EC.visibility_of_element_located(
                (By.XPATH, AddToCartLocator.cart_icon)
            )
        )
        ActionChains(self.driver).move_to_element(icon).perform()

    def get_cart_details(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, AddToCartLocator.cart_detail))
        ).text

    def get_first_item(self):
        return self.driver.find_element (By.XPATH,AddToCartLocator.first_Item_Xpath)

    def get_cart_count(self):
        return self.driver.find_elemt(By.XPATH,AddToCartLocator.cart_count)

    def scroll_to_first_item(self):
        #find first element
        first_item = self.get_first_item()

    def get_add_to_cart_button(self,item):
        return item.find_element(By.XPATH,AddToCartLocator.add_To_Cart_button)
    
    def add_first_item_to_cart(self):
        self.scroll_to_first_item()
        self.driver.implicitly.wait(10)
        first_item= self.get_first_item()
        self.driver.execute_script("executing :",first_item)
        add_to_cart_button = self.get_add_to_cart_button(first_item)
        add_to_cart_button.click()

    
