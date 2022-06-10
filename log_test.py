import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

login = "to.jest.testtt@gmail.com"
password = "wrongPassword"


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://kikfit.pl")
        accept_cookies_btn = self.driver.find_element(By.ID, 'acceptBtn')
        accept_cookies_btn.click()
        sleep(1)

    def testBadPassword(self):
        self.driver.find_element(By.CLASS_NAME, 'c-profile').click()
        login_input = self.driver.find_element(By.NAME, 'username')
        login_input.send_keys(login)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'c-btn.-primary').location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'c-btn.-primary').click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(log_in)).click()
        if self.driver.find_element(By.CLASS_NAME, "-cErrorInfo.-mb10.-tCenter"):
            print("test Wrong Password PASS")
        else:
            print("test Wrong Password FAIL")
        sleep(1)

    def testVisiblePassword(self):
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        eye = self.driver.find_element(By.CLASS_NAME, 'icon-eye')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(eye)).click()
        input_type = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        if WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(input_type)):
            print("test Visible Password PASS")
        else:
            print("test Visible Password FAIL")
        sleep(3)

    def tearDown(self):
        self.driver.quit()
