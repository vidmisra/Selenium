import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Utilities.baseclass import Baseclass


class fashion(Baseclass):
    def __init__(self, driver):
        self.driver = driver
    fashion = (By.XPATH, "//div[text()='Fashion']")
    fashion2 = (By.LINK_TEXT, "All")
    fashion_item1_wishlist = (By.XPATH, "(//a[@class='IRpwTa']/../../a/div[3]/div)[1]")
    fashion_item2_wishlist = (By.XPATH, "(//a[@class='IRpwTa']/../../a/div[3]/div)[2]")

    def gotofashion(self):
        self.movetoelement(self.fashion)
        # time.sleep(5)

    def select_alll(self):
        all = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.fashion2))
        return all

    def select_item1(self):
        item1 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.fashion_item1_wishlist))
        return item1

    def select_item2(self):
        item2 = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.fashion_item2_wishlist))
        return item2



