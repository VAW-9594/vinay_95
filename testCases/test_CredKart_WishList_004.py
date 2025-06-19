import sys
import os
import time

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.wishlist_Page import Wishlist_Page_Class

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from faker import Faker
from pageObjects.Registration_Page import Registration_Page_Class
from pageObjects.Login_Page import Login_Page_Class
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()
    wishlist_url = ReadConfigClass.get_data_for_wishlist_url()
    log = log_generator_class.loggen_method()




    def test_CredKart_Login_For_WhishList004(self):
        self.log.info("Testcase test_CredKart_wishlist_004 is started")
        self.log.info(f"Opening browser and landing on login page--{self.wishlist_url}")
        self.driver.get(self.wishlist_url)
        self.wl = Wishlist_Page_Class (self.driver)  # Object Creation

        self.wl.continue_button ()
        time.sleep(2)
        self.wl.playstation_button()
        time.sleep(2)
        self.wl.add_tolist_playstaion()
        time.sleep(2)
        self.wl.xbox_button()
        self.wl.add_tolist_xbox()
        time.sleep(2)
        self.wl.macbook()
        self.wl.add_tolist_macbook()
        time.sleep(2)
        self.wl.speakers_button()
        self.wl.add_tolist_speaker()
        time.sleep(2)
        self.wl.wishlist_button()

        self.log.info("Wish List verifying")
        if self.wl.verify_text() == "Pass":
            self.log.info("Wish List Created Successfully")
            assert True
        else:
            self.log.info("Wish List Creation  Failed")
            assert False

