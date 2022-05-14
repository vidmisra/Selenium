import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Main_Assignment.pageobjects.address import Address
from Main_Assignment.pageobjects.cartpage import cart
from Main_Assignment.pageobjects.fashion import fashion
from Main_Assignment.pageobjects.grocerypage import Grocery
from Main_Assignment.pageobjects.loginpage import Login
from Main_Assignment.pageobjects.searchproduct import searchproduct
from Main_Assignment.Utilities.baseclass import Baseclass
#import allure


class Test_Login(Baseclass):
    def test_loginpage(self, allure=None):
            exp_msg_alert_msg = "Get access to your Orders, Wishlist and Recommendations"
            act_msg_alert_msg = self.driver.find_element(By.XPATH, "//span[contains(text(),'Get access to your Orders')]").text
            print(act_msg_alert_msg)
            log = self.getlooger()
            lg = Login(self.driver)
            if act_msg_alert_msg in exp_msg_alert_msg:
                lg.enter_phone().send_keys("1234567890")
                lg.enter_password().send_keys("@Vidushi")
                lg.click_login_alert().click()

            else:
                lg.click_login_homepage().click()
                lg.enter_phone().send_keys("1234567890")
                lg.enter_password().send_keys("@Vidushi")
                lg.click_login_alert().click()
            expected_title ="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
            page_title = self.driver.title
            # print(page_title)
            welcome_text = lg.homepage_text()
            expected_text = 'Vidushi'
            try:
                assert expected_text in welcome_text
                print(f"Name is present:-{welcome_text}")
            except Exception as e:
                print('Assertion failed', format(e))
            try:
                assert page_title in expected_title
                allure.attach()
                print('Assertion pass')
            except Exception as e:
                print('Assertion failed', format(e))

            #taking screenshot
            self.driver.get_screenshot_as_file("screen.png")
            log.info("Test-1 welcome to flipkart")

    def test_productsearch(self):
            product_list =[]
            log = self.getlooger()
            search = searchproduct(self.driver)
            c = cart(self.driver)
            search.search().send_keys("oppo watch")
            search.search_button().click()
            search.oppowatch().click()
            #switching to child window
            child_window = self.driver.window_handles[1]
            self.driver.switch_to.window(child_window)
            samsung_add_button = search.samsung_add_to_cart().text
            if samsung_add_button == "ADD TO CART":
                search.oppo_add().click()
                price_IN_INR = search.price().text
                print(price_IN_INR)
                product_list.append(price_IN_INR)
                print(product_list)
                expected_oppo_msg = "OPPO Watch 46 mm WiFi Smartwatch"
                oppo_text = c.oppo_validation().text
                try:
                    assert expected_oppo_msg in oppo_text
                    print(f"oppo watch is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            elif samsung_add_button == "GO TO CART":
                search.click_gotocart().click()
                price_IN_INR = search.price().text
                print(price_IN_INR)
                product_list.append(price_IN_INR)
                print(product_list)
                expected_oppo_msg = "OPPO Watch 46 mm WiFi Smartwatch"
                oppo_text = c.oppo_validation().text
                try:
                    assert expected_oppo_msg in oppo_text
                    print(f"oppo watch is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            #adding second item into cart

            search.search().clear()
            search.search().send_keys("set wet wax")
            search.search_button().click()
            search.setwet_gel().click()
            child_window = self.driver.window_handles[1]
            self.driver.switch_to.window(child_window)
            samsung_add_button = search.samsung_add_to_cart().text
            if samsung_add_button == "ADD TO CART":
                search.setwet_gel_add().click()
                price_IN_INR = search.price().text
                print(price_IN_INR)
                product_list.append(price_IN_INR)
                print(product_list)
                expected_wax_msg = "SET WET Pomade for Slick & Shiny Look With Transparent Formula, No Sulphate, No Alcohol, No Paraben Hair Wax"
                wax_text = c.wax_validation().text
                try:
                    assert expected_wax_msg in wax_text
                    print(f"wax is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            elif samsung_add_button == "GO TO CART":
                search.setwet_gotocart().click()
                price_IN_INR = search.price().text
                product_list.append(price_IN_INR)
                print(product_list)
                expected_wax_msg = "SET WET Pomade for Slick & Shiny Look With Transparent Formula, No Sulphate, No Alcohol, No Paraben Hair Wax"
                wax_text = c.wax_validation().text
                try:
                    assert expected_wax_msg in wax_text
                    print(f"wax is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            #adding 3rd product

            search.search().clear()
            search.search().send_keys("samsung double door fridge")
            search.search_button().click()
            search.samsung_fridge().click()
            child_window = self.driver.window_handles[1]
            self.driver.switch_to.window(child_window)
            samsung_add_button = search.samsung_add_to_cart().text
            # samsung_goto_button = search.samsung_go_to_cart().text
            if samsung_add_button == "ADD TO CART":
                search.samsung_add_to_cart().click()
                price_IN_INR = search.price().text
                product_list.append(price_IN_INR)
                print(product_list)
                expected_fridge_msg = "SAMSUNG 253 l Frost Free Double Door 2 Star Refrigerator"
                fridge_text = c.fridge_validation().text
                try:
                    assert expected_fridge_msg in fridge_text
                    print(f"fridge is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            elif samsung_add_button == "GO TO CART":
                search.samsung_go_to_cart().click()
                price_IN_INR = search.price().text
                print(price_IN_INR)
                product_list.append(price_IN_INR)
                print(product_list)
                expected_fridge_msg = "SAMSUNG 253 l Frost Free Double Door 2 Star Refrigerator"
                fridge_text = c.fridge_validation().text
                try:
                    assert expected_fridge_msg in fridge_text
                    print(f"fridge is present in cart:")
                except Exception as e:
                    print('Assertion failed', format(e))
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            c.navigating_home_from_cart().click()
            # taking screenshot
            self.driver.get_screenshot_as_file("screen.png")
            log.info("Test-2 products added to cart successfully")

    def test_filter(self):
        g = Grocery(self.driver)
        log = self.getlooger()
        search = searchproduct(self.driver)
        g.click_grocery().click()
        g.enter_pin_code().send_keys("560037")
        g.enter_pin_code().send_keys(Keys.ENTER)
        g.enter_text_search().send_keys("besan")
        search.search_button().click()
        g.select_checkbox_in_grocery().click()
        actual_besan_item = g.select_besan_product().text
        expected_besan_name = "24 mantra ORGANIC Besan"
        try:
            assert expected_besan_name in actual_besan_item
            print(f"Besan is coming and name is:-{actual_besan_item}")
        except Exception as e:
            print('Assertion failed', format(e))
        g.goto_home().click()
        log.info("Test-3 Besan test is working fine")

    def test_wishlist(self):
            f = fashion(self.driver)
            c = cart(self.driver)
            f.gotofashion()
            log = self.getlooger()
            f.select_alll().click()
            f.select_item1().click()
            f.select_item2().click()
            home_element = self.driver.find_element(By.XPATH, "//div[text()='Vidushi ']")
            action = ActionChains(self.driver)
            action.move_to_element(home_element).perform()
            time.sleep(5)
            myprofile_wishlist = self.driver.find_element(By.XPATH, "//div[contains(text(),'Wishlist')]")
            action.move_to_element(myprofile_wishlist).click().perform()
            c.navigating_home_from_cart().click()
            log.info("Test-4 wishlist test is working fine")


    def test_address(self):
        time.sleep(5)
        edit_address = Address(self.driver)
        log = self.getlooger()
        home_element = self.driver.find_element(By.XPATH, "//div[text()='Vidushi ']")
        action = ActionChains(self.driver)
        action.move_to_element(home_element).perform()

        myprofile_element2 = self.driver.find_element(By.XPATH, "//div[contains(text(),'My Profile')]")
        action.move_to_element(myprofile_element2).click().perform()
        edit_address.manageaddress().click()
        edit_address.addaddress().click()

        #adding address
        edit_address.addname().send_keys("Vidushi")
        edit_address.addnumber().send_keys("1234567890")
        edit_address.addpincode().send_keys("760004")
        edit_address.addplocality().send_keys("Jaipur")
        edit_address.addarea().send_keys("co-operative colony")
        sel = Select(self.driver.find_element(By.XPATH, "//select[@name='state']"))
        sel.select_by_value("Rajasthan")
        edit_address.addlandmark().send_keys("Abc hospital")
        edit_address.addradio().click()
        edit_address.save_address().click()
        # taking screenshot
        self.driver.get_screenshot_as_file("screen.png")
        log.info("Test-5 Address added successfully")

    def test_logout(self):
        l = Login(self.driver)
        home_element = self.driver.find_element(By.XPATH, "//div[text()='Vidushi ']")
        action = ActionChains(self.driver)
        action.move_to_element(home_element).perform()
        myprofile_logout = self.driver.find_element(By.XPATH, "//div[contains(text(),'Logout')]")
        action.move_to_element(myprofile_logout).click().perform()
        time.sleep(3)
        l.closing_the_popup().click()
        log = self.getlooger()
        log.info("Test-6 logging out successfully")

























