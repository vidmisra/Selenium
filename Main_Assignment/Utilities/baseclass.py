import inspect
import logging
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup_browser")
class Baseclass:
    pass

    def movetoelement(self, by_locator):

        action = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(element).perform()

    def getlooger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        file_handler = logging.FileHandler('/Users/vidmisra/PycharmProjects/Selenium/Main_Assignment/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger