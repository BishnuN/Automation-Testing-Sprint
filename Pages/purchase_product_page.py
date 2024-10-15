import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Locators.Purchase_product_Locator import Purchaselocate
from Unit_testing.User_login_testing import UserLoginTest
from Pages.AddToCartPage import AddToCartPage

class PurchasePage:
    def __init__(self, driver):
        self.random = None
        self.driver = driver
        self.location = Purchaselocate
        self.cart = AddToCartPage(self.driver)
# Product adding function need to call here

    def navCart(self):
        navC = self.driver.find_element(By.XPATH, self.location.navCart)
        return navC

    def cart_Click(self):
        self.navCart().click()

    def checkbtn1(self):
        checkout_locator = self.driver.find_element(By.XPATH, self.location.checkoutButton1)
        return checkout_locator

    def checkbtn1_click(self):
        self.checkbtn1().click()

    def checkbtn2(self):
        checkout2_locator = self.driver.find_element(By.XPATH, self.location.checkoutButton2)
        return checkout2_locator

    def checkbtn2click(self):
        self.checkbtn2().click()

    def checkbox_nav(self):
        check_box = self.driver.find_element(By.ID, self.location.checkBox_id)
        return check_box

    def checkbox_click(self):
        self.checkbox_nav().click()

    def checkbtn3(self):
        checkout3_locator = self.driver.find_element(By.XPATH, self.location.checkoutButton3)
        return checkout3_locator

    def checkbtn3click(self):
        self.checkbtn3().click()

    def paymentMethod(self):
        payment1 = self.driver.find_element(By.XPATH, self.location.paymentOption1)
        payment2 = self.driver.find_element(By.XPATH, self.location.paymentOption2)
        return payment1, payment2

    def paymentClick(self):
        payment1, payment2 = self.paymentMethod()
        random_element = self.random.choice(payment1, payment2)
        random_element.click()

    def ConfirmOrderr(self):
        confirm_order = self.driver.find_element(By.XPATH, self.location.confirmOrder)
        return confirm_order

    def ConfirmClick(self):
        self.ConfirmOrderr().click()

    def check_and_click_insertData(self, email, password):
        signin = self.driver.find_element(By.ID, 'email')
        signin.click()
        if signin:
           UserLoginTest.login(self, email, password)

    def check_for_empty_cart(self):
        empty = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[5]')
        if empty:
            time.sleep(1)
            self.cart.add_first_item_to_cart()
    def purchasefirst(self):
        print("Checking for empty cart...")
        self.check_for_empty_cart()
        print("Navigating to cart...")
        self.cart_Click()
        print("Clicked on the cart.")
        self.checkbtn1_click()

    def purchasesecond(self):
        self.checkbtn2click()
        self.checkbox_click()
        self.checkbtn3click()
        self.paymentClick()
        self.ConfirmClick()








