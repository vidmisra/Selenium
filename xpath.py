from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="//Users//vidmisra//Downloads//chromedriver")

driver.get("https://www.goibibo.com/")

print(driver.title)

#login/signup
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/div[2]/div/div").click()
driver.find_element(By.XPATH, "//*[@class='login__tab_wrapper']").click()
driver.find_element(By.XPATH, "//*[@id='get_sign_in']").click()
driver.find_element(By.XPATH, "//*[@css_selector= ']")


#logo
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/a/span").click()
driver.find_element(By.XPATH, "//*[@class='header-sprite logo'")

#Hotels, Flights or Cabs
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/header/ul/li[1]/a").click()
driver.find_element(By.XPATH, "//*[@class='nav-link active']")

#Round trip
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/ul/li[2]/span[2]").click()
driver.find_element(By.XPATH, "//*[@class='sc-gsNilK dImRia']")

#From, To
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/p") #From
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/p")  #To

driver.find_element(By.XPATH, "//*[@class='sc-iJKOTD iipKRx fswWidgetPlaceholder']")  #From
driver.find_element(By.XPATH, "//*[@class='sc-iJKOTD iipKRx fswWidgetPlaceholder']")  #To

#Search Flights
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/span")
driver.find_element(By.XPATH, "//*[@class='sc-fHeRUh jHgPBA']")

#Fare Type: Student
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[4]")
driver.find_element(By.XPATH, "//*[@class='sc-gKclnd kDbVbq'")

#View all products
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[7]/div/div[3]/div/div[2]/a")
driver.find_element(By.XPATH, "//*[@class='fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn']")

driver.close()

