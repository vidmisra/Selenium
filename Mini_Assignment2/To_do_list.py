from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from Dropdown_Checkbox_Radio import option

driver = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')

driver.get("http://webdriveruniversity.com/")

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/a/div/div[1]").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(10)

select_element = driver.find_element(By.ID,'selectElementID')
select_object = Select(select_element)

<select>
 <option value=value1>Bread</option>
 <option value=value2 selected>Milk</option>
 <option value=value3>Cheese</option>
</select>

select_object.select_by_index(1)

first_selected_option = select_object.first_selected_option


driver.quit()