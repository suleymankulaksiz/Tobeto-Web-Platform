import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *

class Test_Register:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(REGISTER_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

   

    def test_register(self):
        emailrandom = generate_random_email()
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))

        firstname.send_keys(input_firstname)
        lastname.send_keys(input_lastname)
        email.send_keys(emailrandom)
        password.send_keys(input_password)
        password_again.send_keys(input_passwordagain)

        
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        sign_up_button.click()
        


        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK))
        input_phone_box.send_keys(input_phone)
        
        
    
       
        sleep(15)          #bu şimdilik robot doğrulama geçmek için manuel yapıyorum.


        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        

       

        sleep(2)
        alertMessage = self.waitForElementVisible((By.XPATH, REGISTERTEXT_XPATH))
        assert alertMessage.text == TRUEREGISTER_TEXT
