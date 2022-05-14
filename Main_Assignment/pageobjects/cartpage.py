from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class cart:
    def __init__(self, driver):
        self.driver = driver

    oppo_product = (By.XPATH, "//a[contains(text(),'OPPO Watch 46 mm WiFi Smartwatch')]")
    WAX = (By.XPATH, "//a[contains(text(),'SET WET Pomade for Slick & Shiny Look With Transparent Formula, "
                     "No Sulphate, No Alcohol, No Paraben Hair Wax')]")
    fridge = (By.XPATH,"//a[contains(text(),'SAMSUNG 253 l Frost Free Double Door 2 Star Refrigerator')]")
    navigating_home = (By.XPATH, "//img[@alt='Flipkart']")
    click_on_cart = (By.XPATH, "//span[text()='Cart']")


    def oppo_validation(self):
        return self.driver.find_element(*cart.oppo_product)

    def wax_validation(self):
        return self.driver.find_element(*cart.WAX)

    def fridge_validation(self):
        return self.driver.find_element(*cart.fridge)

    def navigating_home_from_cart(self):
        return self.driver.find_element(*cart.navigating_home)
