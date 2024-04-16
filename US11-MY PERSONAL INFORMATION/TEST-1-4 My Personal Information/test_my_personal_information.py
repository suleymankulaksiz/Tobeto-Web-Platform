import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
from selenium.webdriver.support.ui import Select


class Test_my_personal_information:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                   
        self.driver.get(LOGIN_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    def test_login(self):
        login_email = self.waitForElementVisible((By.XPATH,LOGIN_MAIL_XPATH))
        login_email.send_keys(input_personal_mail)
        login_password = self.waitForElementVisible((By.XPATH,LOGIN_PASSWORD_XPATH))
        login_password.send_keys(input_personal_password)
        login_button = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        login_button.click()
        popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        assert popupMessage.text == POPUP_MESSAGE_TEXT
        
    def test_updating_personal_information(self): 

        #Login call testi çağrılır
        self.test_login()
        #Profil bilgileri
        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == "Profilini oluştur"
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton.click()
        nameTextBox=self.waitForElementVisible((By.XPATH,NAMETEXTBOX_XPATH))
        surnameTextBox=self.waitForElementVisible((By.XPATH,SURNAMETEXTBOX_XPATH))
        phoneTextBox=self.waitForElementVisible((By.ID,"phoneNumber"))

        sleep(2)
        # TextBox'ların içerisinin dolu olma durumunu assert ile kontrol etme
        assert nameTextBox.get_attribute("value")
        assert surnameTextBox.get_attribute("value")
        assert phoneTextBox.get_attribute("value")

        # Doğum tarihi girişi yapılır
        Dateofbirth_Box=self.waitForElementVisible((By.XPATH,DATEOFBIRTH_XPATH))
        Dateofbirth_Box.click()
        Dateofbirth_Box.send_keys(input_dateofbirth)

        #TC No girişi yapılır
        tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        tcNo.click()
        tcNo.send_keys(input_tcno)

        #Mail adresi kısmına tıklanma durumu
        mail_click = self.waitForElementVisible((By.XPATH,MAILCLICK_XPATH))
        mail_click.click()

        #Ülke girilme durumu
        countryBox = self.waitForElementVisible((By.XPATH,COUNTRYBOXCLICK_XPATH))
        countryBox.click()
        countryBox.send_keys(input_country)

        #Şehir seçilir
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWN_XPATH))
        )
        dropdown = Select(dropdown_element)
        # indekse göre seçim yapın
        dropdown.select_by_index(40)

        #İlçe seçilir
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, TOWNBOX_XPATH))
        )
        dropdown = Select(dropdown_element)
        #indekse göre seçim 
        sleep(2)
        dropdown.select_by_index(10)

        saveButton = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        saveButton.click()
        sleep(2)




    
    
    
    