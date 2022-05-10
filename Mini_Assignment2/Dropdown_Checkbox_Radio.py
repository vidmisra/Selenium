from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')

driver.get("http://webdriveruniversity.com/")

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[7]/a/div/div[1]").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

time.sleep(10)

element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/select[1]")
drp = Select(element)

drp.select_by_visible_text("Python")

print(len(drp.options))

all_options = drp.options

for option in all_options:
    print(option.text)

time.sleep(10)

element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/select[2]")
drp = Select(element)

drp.select_by_visible_text("Maven")

print(len(drp.options))

all_options = drp.options

for option in all_options:
    print(option.text)

time.sleep(10)

##### Radio button
status = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/form").is_selected()
print(status)

##### Checkbox
driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/form").click()