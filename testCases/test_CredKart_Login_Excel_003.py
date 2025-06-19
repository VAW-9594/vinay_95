import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Excel_Utils import Excel_utils


class Test_CredKart_Login_DDT:
    excel_file_path = r"C:\Users\91959\OneDrive\Desktop\Automation testing\CredKart_Pytest_Framework_02\TestData\File_for_prcatice.xlsx"
    sheet_name = "login_data"
    #excel_file_path = "D:\\Batch Notes\\Automation Testing may 2025\\03. Pytest Framework\\Test_Data\\Bank_App_Test_Data.xlsx"

    #@pytest.mark.flaky(reruns=5, reruns_delay=1)  # to retry the failed testcases
    def test_CredKart_login_DDT_003(self, driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        # time.sleep(2)
        print("Title of the page:", driver.title)
        #########################################################################
        rows = Excel_utils.get_row_count(self.excel_file_path, self.sheet_name)
        print("Total rows are:", rows)
        Result_List = []
        for r in range(2, rows+1):


            driver.get("https://automation.credence.in/login")
            email = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 2)
            password = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 3)
            expected_result = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 4)




            print(f"email is: {email}")
            print(f"Password is: {password}")
            print(f"Expected Result is: {expected_result}")

            # Enter Username
            time.sleep(3)
            username_field = driver.find_element(By.XPATH, "//input[@id='email']")
            username_field.send_keys(email)

            # Enter Password
            password_field = driver.find_element(By.XPATH, "//input[@id='password']")
            password_field.send_keys(password)

            # Click on Create User Button

            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            driver.execute_script("arguments[0].scrollIntoView();", login_button)
            login_button.click()
            # Verify the User login Successfully
            wait = WebDriverWait(driver, 3)

            try:
                wait.until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
                    )
                driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
                print("User login Successfully")
                # driver.save_screenshot("User login Successfully.png")
                actual_result = "Pass"
                Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 5, actual_result)
                time.sleep(3)
                logout_button = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
                driver.execute_script("arguments[0].scrollIntoView();", logout_button)
                logout_button.click()
                time.sleep(5)
                driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
                time.sleep(3)
            except:
                print("User login Failed")
                # driver.save_screenshot("User login Failed.png")
                actual_result = "Fail"
                Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 5, actual_result)

            if actual_result == expected_result:
                test_case_result = "Pass"
                print(f"Test Case Result is: {test_case_result}")
            else:
                test_case_result = "Fail"
                print(f"Test Case Result is: {test_case_result}")

            Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 6, test_case_result)
            Result_List.append(test_case_result)

        print(f"Result List is: {Result_List}")
        assert "Fail" not in Result_List, "Test Case Failed"
        # if "Fail" not in Result_List:
        #     assert True
        # else:
        #     assert False

#
#   credencejune01@credence.in
#  Credence@123