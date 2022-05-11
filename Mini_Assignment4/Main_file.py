from time import sleep
from selenium import webdriver
from Current_temp import Current_temp
from Summer import click_buy_sunscreens_button, add_spf50, add_spf30
from Winter import click_buy_moisturizers_button, add_aloe, add_almond
from Payment import goto_cart, click_pay_with_card, fill_cart, pay


def summer_shopping():
    # This function takes browser reference as an Argument and adds cheapest priced SPF-50 and SPF-30 products to cart.

    click_buy_sunscreens_button(browser)
    print("Successfully moved to the sunscreen page")
    add_spf50(browser)
    print("Least Priced SPF-50 product added to the cart..")
    add_spf30(browser)
    print("Least Priced SPF-30 product added to the cart..")


def winter_shopping():
    # This function takes browser reference as an Argument and adds the cheapest priced Aloe and Almond products to cart.

    click_buy_moisturizers_button(browser)
    print("successfully moved to Moisturizers page")
    add_aloe(browser)
    print("Least priced ALOE product added to the cart..")
    add_almond(browser)
    print("Least Priced ALMOND product is added to the cart..")


def checkout():
    # This function takes browser reference as an Argument and performs all the operations of payment with dummy account
    # details and shows a successful message when payment is done.

    goto_cart(browser)
    print("Successfully Moved to the cart")
    sleep(3)
    click_pay_with_card(browser)
    print("Pay with card clicked")
    fill_cart(browser)
    print("Payment details filled...")
    sleep(2)
    message = pay(browser)
    print("payment", message)


# Driver code
if __name__ == "__main__":
    browser = webdriver.Chrome('/Users/vidmisra/Downloads/chromedriver')
    browser.get("https://weathershopper.pythonanywhere.com/")
    if browser.title == "Current Temperature":
        print("Landed over to the right page")
    else:
        print("Error: Landed over wrong page")
    temperature = Current_temp(browser)
    print("Temperature found: ", temperature)
    if temperature > 34:
        summer_shopping()
        checkout()
    elif temperature < 19:
        winter_shopping()
        checkout()
    else:
        print("It's All Good, No need for shopping")
    sleep(10)
    browser.close()
