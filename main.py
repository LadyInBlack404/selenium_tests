# Import biblioteki
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# Tworzymy instancje klasy WebDriver
# (w zasadzie to odpowiednia podklase - Chrome, Firefox itd.)
driver = webdriver.Chrome()
driver.get("http://www.wsb.pl")

# firefox = webdriver.Firefox()
# firefox.get("https://www.google.pl")
# print(firefox.page_source)

# Odszukanie elementu "accept cookies" po Xpath'ie
accept_cookies_btn = driver.find_element(By.XPATH, '//button[@class="agree-button eu-cookie-compliance-default-button"]')
accept_cookies_btn.click()

#Odszukanie elementu
kontakt_link = driver.find_element(By.LINK_TEXT, 'Kontakt')
kontakt_link.click()
