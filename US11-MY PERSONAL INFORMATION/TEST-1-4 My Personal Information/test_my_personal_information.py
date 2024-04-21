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
from selenium.webdriver.common.action_chains import ActionChains


class Test_my_personal_information:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    def test_precondition(self):
        login_email = self.waitForElementVisible((By.XPATH,LOGIN_MAIL_XPATH))
        login_email.send_keys(input_personal_mail)
        login_password = self.waitForElementVisible((By.XPATH,LOGIN_PASSWORD_XPATH))
        login_password.send_keys(input_personal_password)
        login_button = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        login_button.click()
        popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        assert popupMessage.text == POPUP_MESSAGE_TEXT

        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == "Profilini oluştur"
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton.click()
        
    def test_updating_personal_information(self): 
        #Login call testi çağrılır
        self.test_precondition()
        #Profil bilgilerinin dolu olarak geldiğini kontrol eder
        nameTextBox=self.waitForElementVisible((By.XPATH,NAMETEXTBOX_XPATH))
        surnameTextBox=self.waitForElementVisible((By.XPATH,SURNAMETEXTBOX_XPATH))
        phoneTextBox=self.waitForElementVisible((By.ID,PHONETEXTBOX_ID))
        emailTextBox=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/input"))

        # TextBox'ların içerisinin dolu olma durumunu assert ile kontrol etme
        assert {
        nameTextBox.get_attribute("value") and surnameTextBox.get_attribute("value") and phoneTextBox.get_attribute("value") and emailTextBox.get_attribute("value")
        }

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
        dropdown_element_city = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWN_XPATH))
        )
        dropdown = Select(dropdown_element_city)
        # indekse göre seçim yapın
        dropdown.select_by_index(40)

        #İlçe seçilir
        dropdown_element_town = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, TOWNBOX_XPATH))
        )
        dropdown = Select(dropdown_element_town)
        #indekse göre seçim 
        sleep(2)
        dropdown.select_by_index(10)

        saveButton = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        saveButton.click()
        sleep(2)

    def test_empty_incorrect_data_entry(self):
        self.test_precondition()
        

        #TC No girişi yapılır
        tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        tcNo.click()
        tcNo.send_keys(input_incorrect_tcno)

        #Mahalle sokak girişi 
        streetBox= self.waitForElementVisible((By.XPATH,STREET_XPATH))
        streetBox.click()
        streetBox.send_keys(input_street)

        aboutmeBox= self.waitForElementVisible((By.XPATH,ABOUTME_XPATH))
        aboutmeBox.click()
        aboutmeBox.send_keys(input_aboutme)


        saveButton = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        saveButton.click()
        sleep(2)

        
        tcNo.clear()
        

        tcNo_alert=self.waitForElementVisible((By.XPATH,TCNOALERT_XPATH))
        Dateofbirth_alert= self.waitForElementVisible((By.XPATH,DATEOFBIRTHALERT_XPATH))
        countryBox_alert = self.waitForElementVisible((By.XPATH,COUNTRYBOXALERT_XPATH))
        dropdown_element_city_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTCITYALERT_XPATH))
        dropdown_element_town_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTTOWNALERT_XPATH))
        streetBox_alert= self.waitForElementVisible((By.XPATH,STREETBOXALERT_XPATH))
        aboutmeBox_alert= self.waitForElementVisible((By.XPATH,ABOUTMEALERT_XPATH))

        assert {
        tcNo_alert.text== TCNOALERT_TEXT and Dateofbirth_alert.text == "Doldurulması zorunlu alan*" and 
        countryBox_alert.text == "Doldurulması zorunlu alan*" and
        dropdown_element_city_alert.text == "Doldurulması zorunlu alan*" and 
        dropdown_element_town_alert.text ==  "Doldurulması zorunlu alan*" and 
        streetBox_alert.text == "En fazla 200 karakter girebilirsiniz" and
        aboutmeBox_alert.text == "En fazla 300 karakter girebilirsiniz" 
        }

        
        
        #TC No girişi yapılır = "e" --------->BUG

        tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        tcNo.click()
        tcNo.send_keys(input_string_tcno)

    
        
        #Ülke girilme durumu
        countryBox = self.waitForElementVisible((By.XPATH,COUNTRYBOXCLICK_XPATH))
        countryBox.click()
        countryBox.send_keys(input_long_country)


        #Hata mesajlarını kontrol eder
        tcNo_alert = self.waitForElementVisible((By.XPATH, TCNOALERT_XPATH))

        self.driver.save_screenshot("images/registeredNumber.png")
        self.driver.take_and_show_screenshot("images/registeredNumber.png")
        # Beklenen hata mesajını kontrol eder ve hatayı belirtir
        assert False,"HATA"
        
    def test_add_profile_picture(self):
        self.test_precondition()

        avatar_button=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div"))
        avatar_button.click()
        
        # textx = self.waitForElementVisible((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[1]/div/div[2]/div/h3"))
        # assert textx.text == "TOBETO'ya hoş geldin"

        # assert textx.text.replace('\n', '') == "TOBETO'ya hoş geldin".replace('\n', '')

        
        avatar_popup_text1=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]"))
        assert avatar_popup_text1.text == "Sürükleyip bırak, yapıştır veya\ngözat"

        #Sürükleyeceğiniz dosyanın yolunu belirtin
        dosya_yolu = ("images/tobeto.png")

        file_input= self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]"))
        file_input.send_keys(dosya_yolu)
        
        # Hedef alana sürükleyip bırakmak için ActionChains kullanın
        

        imageUploadButton = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button"))
        imageUploadButton.click()
        sleep(2)


    def test_leave_fields_empty(self):
        self.test_precondition()

        nameTextBox=self.waitForElementVisible((By.XPATH,NAMETEXTBOX_XPATH))
        surnameTextBox=self.waitForElementVisible((By.XPATH,SURNAMETEXTBOX_XPATH))
        phoneTextBox=self.waitForElementVisible((By.ID,PHONETEXTBOX_ID))
        emailTextBox=self.waitForElementVisible((By.XPATH,EMAILNAMETEXTBOX_XPATH))

        # TextBox'ların içerisinin dolu olma durumunu assert ile kontrol etme
        assert {
        nameTextBox.get_attribute("value") and surnameTextBox.get_attribute("value") and phoneTextBox.get_attribute("value") and emailTextBox.get_attribute("value")
        }
        
        saveButton = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        saveButton.click()

        tcNo_alert=self.waitForElementVisible((By.XPATH,TCNOALERT_XPATH))
        Dateofbirth_alert= self.waitForElementVisible((By.XPATH,DATEOFBIRTHALERT_XPATH))
        countryBox_alert = self.waitForElementVisible((By.XPATH,COUNTRYBOXALERT_XPATH))
        dropdown_element_city_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTCITYALERT_XPATH))
        dropdown_element_town_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTTOWNALERT_XPATH))

        assert {
        tcNo_alert.text== TCNOALERT_TEXT and Dateofbirth_alert.text == EMPTY_ALERT_ALERT and 
        countryBox_alert.text == EMPTY_ALERT_ALERT and dropdown_element_city_alert.text == EMPTY_ALERT_ALERT and 
        dropdown_element_town_alert.text ==  EMPTY_ALERT_ALERT  
        }
        sleep(3)

    

    

    



