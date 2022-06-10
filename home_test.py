import unittest
from selenium import webdriver


class HomeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://kikfit.pl")

    def testTitle(self):
        if self.driver.title == "LET'S KIK EAT":
            print("PASS")
        else:
            print("FAIL")

    def tearDown(self):
        self.driver.quit()
