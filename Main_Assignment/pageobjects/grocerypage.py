from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Grocery:
    def __init__(self, driver):
        self.driver = driver
    grocery_button = (By.XPATH, "//div[contains(text(),'Grocery')]")
    enter_pin = (By.XPATH, "//input[@placeholder='Enter pincode']")
    search_bar = (By.XPATH, "//input[@placeholder='Search grocery products']")
    selecting_checkbox = (By.XPATH, "//div[text()='24 mantra ORGANIC']/../div[1]")
    select_product = (By.XPATH, "//span[text()='Add Item']/../../../../div/div[2]/div[2]/a/div/div[1]")
    go_to_homepage = (By.XPATH, "//img[@src='//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/fk_goto_home_logo_small_5b9cdd.svg']")

    def click_grocery(self):
        click_grocery = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.grocery_button))
        return click_grocery

    def enter_pin_code(self):
        enter_pin_code = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.enter_pin))
        return enter_pin_code

    def enter_text_search(self):
        seacrh_bar_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_bar))
        return seacrh_bar_input

    def select_checkbox_in_grocery(self):
        selecting_any_checkbox = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.selecting_checkbox))
        return selecting_any_checkbox

    def select_besan_product(self):
        selecting_besan = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.select_product))
        return selecting_besan

    def goto_home(self):
        homepage = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.go_to_homepage))
        return homepage