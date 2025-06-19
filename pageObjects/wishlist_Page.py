from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Wishlist_Page_Class :
    click_continue_button_Xpath = "//a[@class='btn btn-primary btn-lg']"
    click_Playstation_button_Xpath = " //h3[normalize-space()='Playstation 4']"
    click_add_tolist_button_Xpath = "//input[@value='Add to Wishlist']"
    click_Xbox_One_button_Xpath = "//h3[normalize-space()='Xbox One']"
    click_add_tolist_Xbox_button_Xpath = "//input[@value='Add to Wishlist']"
    click_Apple_Macbook_Pro_button_Xpath = "//h3[normalize-space()='Apple Macbook Pro']"
    click_add_tolist_Macbook_button_Xpath = "//input[@value='Add to Wishlist']"
    click_Speakers_button_Xpath = "//h3[normalize-space()='Speakers']"
    click_add_tolist_Speaker_button_Xpath = "//input[@value='Add to Wishlist']"
    click_wishlist_button_Xpath="//a[normalize-space()='Wishlist (4)']"
    text_Verify_Xpath = "//h1[normalize-space()='Your Wishlist']"





    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def continue_button(self):
       # self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.click_continue_button_Xpath)))
        self.driver.find_element(By.XPATH,self.click_continue_button_Xpath).click()

    def playstation_button(self):
        self.driver.find_element(By.XPATH,self.click_Playstation_button_Xpath).click()

    def add_tolist_playstaion(self):
        self.driver.find_element(By.XPATH,self.click_add_tolist_button_Xpath).click()

    def xbox_button(self):
        self.driver.find_element(By.XPATH,self.click_Xbox_One_button_Xpath).click()

    def add_tolist_xbox(self):
        self.driver.find_element(By.XPATH,self.click_add_tolist_Xbox_button_Xpath).click()

    def macbook(self):
        self.driver.find_element(By.XPATH,self.click_Apple_Macbook_Pro_button_Xpath).click()

    def add_tolist_macbook(self):
        self.driver.find_element(By.XPATH, self.click_add_tolist_Macbook_button_Xpath).click()

    def speakers_button(self):
        self.driver.find_element(By.XPATH,self.click_Speakers_button_Xpath).click()

    def add_tolist_speaker(self):
        self.driver.find_element(By.XPATH,self.click_add_tolist_Speaker_button_Xpath).click()

    def wishlist_button(self):
        self.driver.find_element(By.XPATH,self.click_wishlist_button_Xpath).click()

    def verify_text(self):
        try:
            self.wait.until(
                expected_conditions.presence_of_element_located((By.XPATH,self.text_Verify_Xpath)))
            return "Pass"
        except:
            return "Fail"

