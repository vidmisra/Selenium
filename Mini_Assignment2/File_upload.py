from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')

driver.get("http://webdriveruniversity.com/")

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[16]/a/div/div[1]").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/form").send_keys("/Users/vidmisra/Downloads")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/input[2]").click()

driver.quit()