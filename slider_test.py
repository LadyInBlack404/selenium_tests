import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SliderTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://kikfit.pl")
        accept_cookies_btn = self.driver.find_element(By.ID, 'acceptBtn')
        accept_cookies_btn.click()
        sleep(1)

    def testGallery(self):
        self.driver.find_element(By.CLASS_NAME, 'swiper-wrapper').location_once_scrolled_into_view
        sleep(1)
        slide_one = self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[5]/img")
        ActionChains(self.driver).click_and_hold(slide_one).move_by_offset(-580, 0).pause(0.1).release().perform()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[6]/img").is_displayed():
            print("Slide 1 to the left PASS")
        else:
            print("Slide 1 to the left FAIL")
        slide_two = self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[6]/img")
        sleep(1)
        ActionChains(self.driver).click_and_hold(slide_two).move_by_offset(-580, 0).pause(0.1).release().perform()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[7]/img").is_displayed():
            print("Slide 2 to the left PASS")
        else:
            print("Slide 2 to the left FAIL")
        slide_three = self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[7]/img")
        sleep(1)
        ActionChains(self.driver).click_and_hold(slide_three).move_by_offset(-580, 0).pause(0.1).release().perform()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[8]/img").is_displayed():
            print("Slide 3 to the left PASS")
        else:
            print("Slide 3 to the left FAIL")
        slide_four = self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[8]/img")
        sleep(1)
        ActionChains(self.driver).click_and_hold(slide_four).move_by_offset(-580, 0).pause(0.1).release().perform()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[9]/img").is_displayed():
            print("Slide 4 to the left PASS")
        else:
            print("Slide 4 to the left FAIL")
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'swiper-button.-next').click()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[6]/img").is_displayed():
            print("Button 'next' PASS")
        else:
            print("Button 'next' FAIL")
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'swiper-button.-prev').click()
        if self.driver.find_element(By.XPATH, "//*[@id='mealSlider']/div[1]/div[1]/div[5]/img").is_displayed():
            print("Button 'back' PASS")
        else:
            print("Button 'back' FAIL")
        sleep(1)

    def tearDown(self):
        self.driver.quit()
        
