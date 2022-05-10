from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')

driver.get("http://webdriveruniversity.com/")

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/a/div/div[1]").click()
print(driver.current_window_handle)     #FFF18449A4CC9E3B60AF1E08E2916B28 - parent window

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

###### WebElement Click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div/div[2]/span").click()
print("WebElement Click!")

time.sleep(10)

driver.find_element(By.XPATH, "//button[text() = 'Close']").click()

###### Javascript Click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/div[2]/span").click()
print("Javascript Click!")

driver.find_element(By.XPATH, "//button[text() = 'Close']").click()

###### Action Move & click
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[3]/div/div[2]/span").click()
print("Action move & click!")

driver.find_element(By.XPATH, "//button[text() = 'Close']").click()

driver.quit()