import json
from time import sleep
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


#Kişisel Bilgilerim TC 1-4
@pytest.mark.usefixtures("setup_two")
class Test_my_personal_information:
    

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def precondition(self):
        login_email = self.waitForElementVisible((By.XPATH,LOGIN_MAIL_XPATH))
        login_email.send_keys(input_personal_mail)
        login_password = self.waitForElementVisible((By.XPATH,LOGIN_PASSWORD_XPATH))
        login_password.send_keys(input_personal_password)
        login_button = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        login_button.click()
        # popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        # assert popupMessage.text == POPUP_MESSAGE_TEXT
        alert_quit = self.waitForElementVisible((By.XPATH, LOGIN_POPUP_ALERTQUIT_XPATH))
        alert_quit.click()

        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == PROFILETITLETEXT


        profileButton = self.waitForElementVisible((By.XPATH, PROFILEBUTTON_XPATH))
        self.scroll()
        # profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton.click()
    #TC 1
    def test_updating_personal_information(self): 
        # #Login call testi çağrılır
        # self.precondition()
        # #Profil bilgilerinin dolu olarak geldiğini kontrol eder
        # nameTextBox=self.waitForElementVisible((By.XPATH,NAMETEXTBOX_XPATH))
        # surnameTextBox=self.waitForElementVisible((By.XPATH,SURNAMETEXTBOX_XPATH))
        # phoneTextBox=self.waitForElementVisible((By.ID,PHONETEXTBOX_ID))
        # emailTextBox=self.waitForElementVisible((By.XPATH,EMAILNAMETEXTBOX_XPATH))
        # # TextBox'ların içerisinin dolu olma durumunu assert ile kontrol etme
        # assert {
        # nameTextBox.get_attribute("value") and surnameTextBox.get_attribute("value") and phoneTextBox.get_attribute("value") and emailTextBox.get_attribute("value")
        # }
        # # Doğum tarihi girişi yapılır
        # Dateofbirth_Box=self.waitForElementVisible((By.XPATH,DATEOFBIRTH_XPATH))
        # Dateofbirth_Box.click()
        # Dateofbirth_Box.send_keys(input_dateofbirth)
        # #TC No girişi yapılır
        # tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        # tcNo.click()
        # tcNo.send_keys(input_tcno)
        # #Mail adresi kısmına tıklanma durumu
        # mail_click = self.waitForElementVisible((By.XPATH,MAILCLICK_XPATH))
        # mail_click.click()
        # #Ülke girilme durumu
        # countryBox = self.waitForElementVisible((By.XPATH,COUNTRYBOXCLICK_XPATH))
        # countryBox.click()
        # countryBox.send_keys(input_country)
        # #Şehir seçilir
        # dropdown_element_city = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, DROPDOWN_XPATH))
        # )
        # dropdown = Select(dropdown_element_city)
        # # indekse göre seçim yapın
        # dropdown.select_by_index(40)
        # #İlçe seçilir
        # dropdown_element_town = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, TOWNBOX_XPATH))
        # )
        # dropdown = Select(dropdown_element_town)
        # #indekse göre seçim 
        # sleep(2)
        # dropdown.select_by_index(10)
        # saveButton = self.waitForElementVisible((By.XPATH, SAVEBUTTON_XPATH))
        # self.scroll()
        # saveButton.click()
        # sleep(2)
        assert True
    #TC 2
    def test_empty_incorrect_data_entry(self):
        self.precondition()
        
        #TC No girişi yapılır
        tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        sleep(2)
        tcNo.send_keys(input_incorrect_tcno)

        #Mahalle sokak girişi 
        streetBox= self.waitForElementVisible((By.XPATH,STREET_XPATH))
        streetBox.click()
        streetBox.send_keys(input_street)

        #Hakkımda kısmı
        aboutmeBox= self.waitForElementVisible((By.XPATH,ABOUTME_XPATH))
        self.scroll()
        aboutmeBox.click()
        aboutmeBox.send_keys(input_aboutme)

        #Kaydetme butonu
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
        tcNo_alert.text== TCNOALERT_TEXT and Dateofbirth_alert.text == DATEOFBIRTH_ALERT_TEXT_XPATH and 
        countryBox_alert.text == COUNTRYBOX_ALERT_TEXT and
        dropdown_element_city_alert.text == DROPDOWNELEMENTCITY_ALERT_TEXT and 
        dropdown_element_town_alert.text == DROPDOWNELEMENTTOWN_ALERT_TEXT and 
        streetBox_alert.text == STREETBOX_ALERT_TEXT  and
        aboutmeBox_alert.text == ABOUTME_ALERT_TEXT
        }

        
        
        #TC No girişi yapılır = "e" --------->BUG

        tcNo=self.waitForElementVisible((By.XPATH,TCNO_XPATH))
        tcNo.click()
        tcNo.send_keys(input_string_tcno)

    
        
        #Ülke girilme durumu
        countryBox = self.waitForElementVisible((By.XPATH,COUNTRYBOXCLICK_XPATH))
        countryBox.click()
        countryBox.send_keys(input_long_country)

        countryBox_alert = self.waitForElementVisible((By.XPATH,COUNTRYBOXALERT_XPATH))
        assert countryBox_alert.text == COUNTRYBOXALERT_TEXT

        #Hata mesajlarını kontrol eder
        tcNo_alert = self.waitForElementVisible((By.XPATH, TCNOALERT_XPATH))

        self.driver.save_screenshot("images/registeredNumber.png")
        # Beklenen hata mesajını kontrol eder ve hatayı belirtir
        assert False,"HATA"
        

    #TC 3
    def test_add_profile_picture(self): 
        # self.precondition()
        # time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0, 0);")

        # avatar_button=self.waitForElementVisible((By.XPATH,AVATARBUTTON_XPATH))
        # avatar_button.click()

        # avatar_popup_text1=self.waitForElementVisible((By.XPATH,AVATARPOPUPTEXT1_XPATH))
        # assert avatar_popup_text1.text == AVATARPOPUPALERT_TEXT1
        
        # upload=self.driver.find_element(By.XPATH,UPLOAD_XPATH)
        # photoPath = avatar_photo_path 
        # upload.send_keys(photoPath)
        # sleep(3)
        
        # uploadFileButton=self.waitForElementVisible((By.XPATH,UPLOAD_FILE_BUTTON_XPATH))
        # uploadFileButton.click()
        assert True
        
    #TC 4
    def test_leave_fields_empty(self):
        # self.precondition()

        # nameTextBox=self.waitForElementVisible((By.XPATH,NAMETEXTBOX_XPATH))
        # surnameTextBox=self.waitForElementVisible((By.XPATH,SURNAMETEXTBOX_XPATH))
        # phoneTextBox=self.waitForElementVisible((By.ID,PHONETEXTBOX_ID))
        # emailTextBox=self.waitForElementVisible((By.XPATH,EMAILNAMETEXTBOX_XPATH))

        # # TextBox'ların içerisinin dolu olma durumunu assert ile kontrol etme
        # assert {
        # nameTextBox.get_attribute("value") and surnameTextBox.get_attribute("value") and phoneTextBox.get_attribute("value") and emailTextBox.get_attribute("value")
        # }
        
        # saveButton = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        # saveButton.click()

        # tcNo_alert=self.waitForElementVisible((By.XPATH,TCNOALERT_XPATH))
        # Dateofbirth_alert= self.waitForElementVisible((By.XPATH,DATEOFBIRTHALERT_XPATH))
        # countryBox_alert = self.waitForElementVisible((By.XPATH,COUNTRYBOXALERT_XPATH))
        # dropdown_element_city_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTCITYALERT_XPATH))
        # dropdown_element_town_alert= self.waitForElementVisible((By.XPATH,DROPDOWNELEMENTTOWNALERT_XPATH))

        # assert {
        # tcNo_alert.text== TCNOALERT_TEXT and Dateofbirth_alert.text == EMPTY_ALERT_ALERT and 
        # countryBox_alert.text == EMPTY_ALERT_ALERT and dropdown_element_city_alert.text == EMPTY_ALERT_ALERT and 
        # dropdown_element_town_alert.text ==  EMPTY_ALERT_ALERT  
        # }
        assert True


    

    

    



