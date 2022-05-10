from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="//Users//vidmisra//Downloads//chromedriver")

driver.get("https://www.facebook.com/")

print(driver.title)

driver.close()