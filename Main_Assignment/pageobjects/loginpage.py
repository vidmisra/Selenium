from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login:
    def __init__(self, driver):
        self.driver = driver
    closing_popup = (By.XPATH, "//button[text()='✕']")
    login_button = (By.XPATH, "//a[text()='Login']")
    phone_number = (By.XPATH, "//span[contains(text(),'Forgot?')]/../../../div/input[@type='text']")
    password = (By.XPATH, "//span[contains(text(),'Forgot?')]/../../input[@type='password']")
    login_button = (By.XPATH, "//span[contains(text(),'Forgot?')]/../../../div/button[@type='submit']")
    welcome_text = (By.XPATH, "//div[contains(text(),'Vidushi')]")

    def closing_the_popup(self):
        element_cut = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.closing_popup))
        return element_cut

    def click_login_homepage(self):
        return self.driver.find_element(*Login.login_button)

    def enter_phone(self):
        return self.driver.find_element(*Login.phone_number)

    def enter_password(self):
        return self.driver.find_element(*Login.password)

    def click_login_alert(self):
        return self.driver.find_element(*Login.login_button)

    def homepage_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.welcome_text))
        return element.text




