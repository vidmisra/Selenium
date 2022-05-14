from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Address:
    def __init__(self, driver):
        self.driver = driver

    select_address = (By.XPATH, "//div[text()='Vidushi ']")
    manage_address = (By.XPATH, "//div[contains(text(),'Manage Addresses')]")
    add_address = (By.XPATH, "//div[contains(text(),'ADD A NEW ADDRESS')]")
    address_name = (By.XPATH, "//input[@name='name']")
    address_number = (By.XPATH, "//input[@name='phone']")
    address_pincode = (By.XPATH, "//input[@name='pincode']")
    address_locality = (By.XPATH, "//input[@name='addressLine2']")
    address_area = (By.XPATH, "//textarea[@name='addressLine1']")
    address_city = (By.XPATH, "//input[@name='city']")
    address_state = (By.XPATH, "//select[@name='state']")
    address_landmark = (By.XPATH, "//input[@name='landmark']")
    address_radio_button = (By.XPATH, "//span[text()='Home']/../../div[1]")
    address_save = (By.XPATH, "//button[text()='Save']")


    def manipulating_address(self):
        address_select = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.select_address))
        return address_select

    def manageaddress(self):
        edit_address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.manage_address))
        return edit_address

    def addaddress(self):
        add_address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.add_address))
        return add_address

    def addname(self):
        name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.address_name))
        return name

    def addnumber(self):
        number = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.address_number))
        return number

    def addpincode(self):
        pincode = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_pincode))
        return pincode

    def addplocality(self):
        locality = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_locality))
        return locality

    def addarea(self):
        area = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_area))
        return area

    def addcity(self):
        city = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_city))
        return city

    def addstate(self):
        state = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_state))
        return state

    def addlandmark(self):
        landmark = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_landmark))
        return landmark

    def addradio(self):
        radio = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_radio_button))
        return radio

    def save_address(self):
        save = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.address_save))
        return save

