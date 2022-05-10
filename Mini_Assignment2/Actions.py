from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')

driver.get("http://webdriveruniversity.com/")

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[9]/a/div/div[1]").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(10)

source = driver.find_element(By.LINK_TEXT, "DRAG ME TO MY TARGET!")
target = driver.find_element(By.LINK_TEXT, "Dropped!")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
driver.close()


source= driver.find_element(By.LINK_TEXT, "Double Click Me!");
# action chain object creation
action = ActionChains(driver)
# double click operation and perform
action.double_click(source).perform()

driver.close()
driver.quit()