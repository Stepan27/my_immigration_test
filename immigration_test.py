import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/stepan/PycharmProjects/HRM100Full/browser_drivers/chromedriver.exe')
        self.driver.get('http://hrm-online.portnov.com')

    def tearDown(self) -> None:
        self.driver.quit()


    def test_01_MyInfo_01(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()
        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()
        driver.find_element_by_id('immigration_type_flag_1').click()
        driver.find_element_by_id('immigration_number').send_keys('123456789')
        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys('04-09-2020')
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys('04-09-2022')
        driver.find_element_by_id('immigration_i9_status').send_keys('YES')
        Select(driver.find_element_by_id('immigration_country')).select_by_visible_text("Japan")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys('05-09-2020')
        sleep(1)
        driver.find_element_by_id('btnSave').click()

        ##self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          ##'Successfully Saved'))

        sleep(4)

        spam_message = driver.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', spam_message)


    def test_01_MyInfo_02(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()
        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()
        driver.find_element_by_id('immigration_type_flag_2').click()
        driver.find_element_by_id('immigration_number').send_keys('123456789')
        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys('04-09-2020')
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys('04-09-2022')
        driver.find_element_by_id('immigration_i9_status').send_keys('YES')
        Select(driver.find_element_by_id('immigration_country')).select_by_visible_text("Japan")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys('05-09-2020')
        sleep(1)
        driver.find_element_by_id('btnSave').click()

        ##self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          ##'Successfully Saved'))

        sleep(4)

        spam_message = driver.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', spam_message)

    def test_01_MyInfo_03(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()
        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()
        driver.find_element_by_id('immigration_type_flag_2').click()
        driver.find_element_by_id('immigration_number').send_keys('123456789')
        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys('04-09-2020')
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys('04-09-2022')
        driver.find_element_by_id('immigration_i9_status').send_keys('YES')
        Select(driver.find_element_by_id('immigration_country')).select_by_visible_text("Japan")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys('05-09-2020')
        sleep(1)
        driver.find_element_by_id('btnSave').click()
        driver.find_element_by_xpath("(//input[@name='chkImmigration[]'])[1]").click()
        driver.find_element_by_id('btnDelete').click()
        ##self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          ##'Successfully Saved'))
        try:
            driver.find_element_by_xpath("(//input[@name='chkImmigration[]'])[1]").click()
        # вказуєм конкретну Exceptions яка може виникнути і що робити тоді
        except driver.NoSuchElementException:
            return True
        return False
        sleep(4)

        spam_message = driver.find_element_by_id('welcome').text

        self.assertEqual('Welcome Admin', spam_message)




if __name__ == '__main__':
    unittest.main()