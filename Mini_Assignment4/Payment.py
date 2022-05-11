from time import sleep


def goto_cart(browser):
    # This function searches the cart in the page and moves the cursor over there to click and move to the cart.

    browser.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()


def click_pay_with_card(browser):
    # This function finds the payment option into the cart and clicks it.

    browser.find_element_by_xpath("//button[@type = 'submit']").click()


def fill_cart(browser):
    # This function fills the card details in the form

    browser.switch_to.frame("stripe_checkout_app")
    browser.find_element_by_xpath("//input[@type = 'email']").send_keys("sample@gmail.com")
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'Card number']") \
        .send_keys('6011 1111 1111 1117')
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder = 'MM / YY']").send_keys('11/24')
    sleep(1)
    browser.find_element_by_xpath("//input[@placeholder = 'CVC']").send_keys('132')
    sleep(1)


def pay(browser):
    #This function clicks "submit" button to pay after filling the form and sends message whether payment is successful or not.

    browser.find_element_by_xpath("//button[@type='submit' and \
        @class='Button-animationWrapper-child--primary Button']").click()
    browser.switch_to_default_content()
    sleep(5)
    return "success" if browser.title == "Confirmation" else "failed"
