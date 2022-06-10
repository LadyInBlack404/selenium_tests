# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

# DANE TESTOWE


email = "ddf@fssp.pl"
sex = "male"
lastname = "Nowak"
password = "sdjgfsdfj3"
birthdate = "1986-03-02"
address = "Street 21 New York"
city = "Kozia Wola"
postcode = "23455"
phone = "123123123"
alias = "my alias"


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com")
        self.driver.implicitly_wait(6)

    def testNoNameEntered(self):
        # KROKI
        driver = self.driver
        # 1. Kliknij "Sign in"
        driver.find_element(By.CLASS_NAME, "login").click()
        # 2. Wpisz e-mail
        email_input = driver.find_element(By.ID, 'email_create')
        email_input.send_keys(email)
        # 3. Kliknij przycisk „Create account”
        driver.find_element(By.ID, "SubmitCreate").click()
        # 4. Wybierz płeć
        if sex == "male":
            # Kliknij Mr
            driver.find_element(By.ID, "id_gender1").click()
        else:
            # Kliknij Mrs
            driver.find_element(By.ID, "id_gender2").click()
        # 5. Wpisz nazwisko
        driver.find_element(By.ID, "customer_lastname").send_keys(lastname)
        # 6. Sprawdź poprawność e-maila
        personal_information_email_input = driver.find_element(By.ID, "email")
        email_fact = personal_information_email_input.get_attribute("value")
        self.assertEqual(email, email_fact)
        # 7. Wpisz hasło
        driver.find_element(By.ID, "passwd").send_keys(password)
        # 8. Wybierz datę urodzenia
        birthday = str(int(birthdate.split("-")[2]))
        day = Select(driver.find_element(By.ID, "days"))
        day.select_by_value(birthday)
        month = Select(driver.find_element(By.ID, "months"))
        birthmonth = str(int(birthdate.split("-")[1]))
        month.select_by_value(birthmonth)
        birthyear = birthdate.split("-")[0]
        year = Select(driver.find_element(By.ID, "years"))
        year.select_by_value(birthyear)
        # 9. Sprawdź pole „First name”
        first_name_fact = driver.find_element(By.ID, 'firstname').get_attribute("value")
        self.assertEqual("", first_name_fact)
        # 10. Sprawdź pole „Last name”
        last_name_fact = driver.find_element(By.ID, 'lastname').get_attribute("value")
        self.assertEqual(lastname, last_name_fact)
        # 11. Wpisz adres
        driver.find_element(By.ID, 'address1').send_keys(address)
        # 12. Wpisz miasto
        driver.find_element(By.ID, 'city').send_keys(city)
        # 13. Wpisz kod pocztowy
        driver.find_element(By.ID, 'postcode').send_keys(postcode)
        # 14. Wybierz stan
        state_select = Select(driver.find_element(By.ID, "id_state"))
        state_select.select_by_visible_text("Alabama")
        # 15. Wpisz numer telefonu
        driver.find_element(By.ID, 'phone_mobile').send_keys(phone)
        # 16. Wpisz alias adresu
        al = driver.find_element(By.ID, 'alias')
        al.clear()
        al.send_keys(alias)
        # 17. Kliknij Register
        driver.find_element(By.ID, 'submitAccount').click()

        # UWAGA! TU BĘDZIE SPRAWDZANY OCZEKIWANY REZULTAT #
        error_number_info = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p').text
        print(error_number_info)

        # Poczekaj 3 sekundy, aby zobaczyć co się dzieje
        sleep(3)

    def tearDown(self):
        self.driver.quit()
