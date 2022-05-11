from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')
browser.maximize_window()

browser.get("https://weathershopper.pythonanywhere.com/")
time.sleep(4)

print(browser.title)


def Current_temp(browser):
    # This function finds the temperature by scraping the page

    temperature = browser.find_element_by_id("temperature")
    return int(temperature.text[:-2])


browser.quit()
