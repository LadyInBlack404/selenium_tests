import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select


class LinksTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://kikfit.pl")
        accept_cookies_btn = self.driver.find_element(By.ID, 'acceptBtn')
        accept_cookies_btn.click()
        sleep(1)

    def testPhoneNumber(self):
        self.driver.find_element(By.XPATH, '/html/body/div[3]/header/div/div/div[2]/div[1]/div[1]/a').click()
        print(self.driver.current_window_handle)
        # to fetch the first child window handle
        chwnd = self.driver.window_handles[0]
        # to switch focus the first child window handle
        self.driver.switch_to.window(chwnd)
        print(self.driver.find_element(By.TAG_NAME("h3").text))
        # str mainWindowHandle = self.driver.current_window_handle
        # set str allWindowsHandles = self.driver.window_handles
        # WebDriverWait(self.driver, 40).until(found_window()((By.ID, 'facebook'))).click()
        sleep(3)

    # def testMessage(self):
    #     WebDriverWait(self.driver, 40).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="contact"]/div[1]/a[1]/button'))).click()
    #     sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[1])

    # def testCall(self):
    #     WebDriverWait(self.driver, 40).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="contact"]/div[1]/a[2]/button'))).click()
    #     sleep(1)
    #
    # def testInstagram(self):
    #     WebDriverWait(self.driver, 40).until(
    #         EC.presence_of_element_located((By.ID, 'instagram'))).click()
    #     sleep(3)

        # WebDriverWait(self.driver, timeout=50).until(found_window("new window name"))
    #
    # def testMail(self):
    #     WebDriverWait(self.driver, 40).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'mail'))).click()
    #     sleep(1)
    #
    # def testFacebook(self):
    #     WebDriverWait(self.driver, 40).until(
    #         EC.presence_of_element_located((By.ID, 'facebook'))).click()
    #     sleep(1)

    def tearDown(self):
        self.driver.quit()
