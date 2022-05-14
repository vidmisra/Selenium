from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class searchproduct:
    def __init__(self, driver):
        self.driver = driver
    grocery_button = (By.XPATH, "//input[@placeholder='Search for products, brands and more']")
    search_icon = (By.XPATH, "//button[@type='submit']")
    select_oppowatch = (By.XPATH, "//div[contains(text(),'Black Strap, Regular')]/../a[contains(text(),"
                                  "'OPPO Watch 46 mm WiFi Smartwatch')]")
    select_setwetgel = (By.XPATH, "//a[contains(text(),'SET WET Pomade for Slick & Shiny Look With Transparent ...')]")
    oppo_add_to_cart = (By.XPATH, "//span[contains(text(),'OPPO Watch 46 mm WiFi Smartwatch')]"
                                  "/../../../../../../div[1]/div[2]/div/ul/li/button[text()='ADD TO CART']")
    oppo_gotocart = (By.XPATH, "//button[text()='GO TO CART']")

    oppo_amount = (By.XPATH, "//div[contains(text(),'Total Amount')]/../../span")
    setwet_addtocart = (By.XPATH, "//span[contains(text(),'SET WET Pomade for Slick & Shiny Look With Transparent Formula, No Sulphate, No Alcohol, No Paraben Hair Wax')]"
                                  "/../../../../../../div[1]/div[2]/div/ul/li/button[text()='ADD TO CART']")
    setwet_gotocart = (By.XPATH, "//button[text()='GO TO CART']")
                        # "//span[contains(text(),'SET WET Pomade for Slick & Shiny Look With Transparent Formula, No Sulphate, No Alcohol, No Paraben Hair Wax')]"
                        # "/../../../../../../div[1]/div[2]/div/ul/li/button[text()='ADD TO CART']"

    samsung_fridge_select = (By.XPATH, "//div[contains(text(),'SAMSUNG 253 l Frost Free Double Door 2 Star Refrigerator')]")
    samsung_addtocart = (By.XPATH, "//button[text()='BUY NOW']/../../../li[1]")
        # (By.XPATH, "//button[text()='ADD TO CART']")
    samsung_gotocart = (By.XPATH, "//button[text()='GO TO CART']")
    all_items = (By.XPATH, "//div[contains(text(),'My Cart')]/../../../../div[@class='_1AtVbE col-12-12']")

    def search(self):
        return self.driver.find_element(*searchproduct.grocery_button)

    def search_button(self):
        return self.driver.find_element(*searchproduct.search_icon)

    def oppowatch(self):
        oppo_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.select_oppowatch))
        return oppo_element

    def oppo_add(self):
        oppo_element_cart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.oppo_add_to_cart))
        return oppo_element_cart

    def click_gotocart(self):
        gotocart_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.oppo_gotocart))
        return gotocart_element

    def price(self):
        oppo_price_INR = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.oppo_amount))
        return oppo_price_INR

    def setwet_gel(self):
        select_setwet = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.select_setwetgel))
        return select_setwet

    def setwet_gel_add(self):
        select_setwet_add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.setwet_addtocart))
        return select_setwet_add

    def setwet_gel_goto(self):
        select_setwet_goto = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.setwet_gotocart))
        return select_setwet_goto

    def samsung_fridge(self):
        select_samsung_fridge = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.samsung_fridge_select))
        return select_samsung_fridge

    def samsung_add_to_cart(self):
        samsung_fridge_add = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.samsung_addtocart))
        return samsung_fridge_add

    def samsung_go_to_cart(self):
        samsung_fridge_goto = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.samsung_gotocart))
        return samsung_fridge_goto








