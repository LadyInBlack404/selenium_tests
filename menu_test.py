import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://kikfit.pl")
        accept_cookies_btn = self.driver.find_element(By.ID, 'acceptBtn')
        accept_cookies_btn.click()
        sleep(1)

    def testPrograms(self):
        programs = self.driver.find_element(By.LINK_TEXT, 'Programy')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(programs)).click()
        title = self.driver.find_element(By.XPATH, '//*[@id="offer"]/div[2]/div[1]/div/h2')
        if WebDriverWait(self.driver, 20).until(EC.visibility_of(title)):
            print("Programs PASS")
        else:
            print("Programs FAIL")
        sleep(3)

    def testKikBar(self):
        kik_bar = self.driver.find_element(By.LINK_TEXT, 'kikfit bar')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(kik_bar)).click()
        if self.driver.current_url == "https://kikfit.pl/kreator/bar/wybor-dan":
            print("kikfit bar PASS")
        else:
            print("kikfit bar FAIL")
        sleep(3)

    def testIndividualProgram(self):
        individual_program = self.driver.find_element(By.LINK_TEXT, 'Program Indywidualny')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(individual_program)).click()
        title = self.driver.find_element(By.XPATH, '/html/body/div[3]/main/section[1]/div/div/div[2]/h2/p')
        if WebDriverWait(self.driver, 20).until(EC.visibility_of(title)):
            print("Individual Program PASS")
        else:
            print("Individual Program FAIL")
        sleep(3)

    def testAboutUs(self):
        about_us = self.driver.find_element(By.LINK_TEXT, 'O nas')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(about_us)).click()
        if self.driver.current_url == "https://kikfit.pl/o-nas":
            print("About Us PASS")
        else:
            print("About Us FAIL")
        sleep(3)

    def testDelivery(self):
        delivery = self.driver.find_element(By.LINK_TEXT, 'Gdzie dowozimy')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(delivery)).click()
        if self.driver.current_url == "https://kikfit.pl/mapa-dowozu":
            print("Delivery PASS")
        else:
            print("Delivery FAIL")
        sleep(3)

    def testContact(self):
        contact = self.driver.find_element(By.LINK_TEXT, 'Kontakt')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(contact)).click()
        if self.driver.current_url == "https://kikfit.pl/o-nas":
            print("Contact PASS")
        else:
            print("Contact FAIL")
        sleep(3)

    def tearDown(self):
        self.driver.quit()
