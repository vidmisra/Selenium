from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

print(driver.title)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[29]/a").click()

print("JavaScript Alerts")

time.sleep(5)

el = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[3]/button")
driver.execute_script("arguments[0].click();", el)

print("Click for JS Prompt")

# Switch the control to the Alert window
obj = driver.switch_to.alert

time.sleep(2)

# Enter text into the Alert using send_keys()
obj.send_keys('Vidushi')

time.sleep(2)

# use the accept() method to accept the alert
obj.accept()

time.sleep(5)

driver.quit()
