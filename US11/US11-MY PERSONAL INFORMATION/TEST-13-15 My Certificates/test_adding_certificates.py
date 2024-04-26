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
import os
import sys

#Sertifikalarım TC 13-15
class Test_adding_certificates:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def save_buttons(self):
        certificates_save_button = self.waitForElementVisible((By.XPATH,SAVEBUTTON_XPATH))
        certificates_save_button.click()

    def uploadPath(self):
        upload=self.driver.find_element(By.XPATH,UPLOAD_XPATH)
        sleep(2)
        dataPath = certificates_data_path 
        sleep(2)
        upload.send_keys(dataPath)
        sleep(2)
    def uploadPathTxt(self):
        upload=self.driver.find_element(By.XPATH,UPLOAD_XPATH)
        sleep(2)
        dataPath = txt_data_path 
        sleep(2)
        upload.send_keys(dataPath)
        sleep(2)
    
    def UploadPathPng(self):
        upload=self.driver.find_element(By.XPATH,UPLOAD_XPATH)
        photoPath = tobeto_png_path
        upload.send_keys(photoPath)
        sleep(3)
    def UploadPathPng2(self): #//*[@id="__next"]/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]
        upload=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]")
        photoPath = tobeto_png2_path
        upload.send_keys(photoPath)
        sleep(3)

    def upload_area(self):
        uploadFileButton=self.waitForElementVisible((By.XPATH,UPLOAD_AREA_XPATH))
        uploadFileButton.click()
        sleep(2)
    
    def uploadFileButton(self):
        uploadFileButton=self.waitForElementVisible((By.XPATH,UPLOAD_FILE_BUTTON_XPATH))
        uploadFileButton.click()
        sleep(2)

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
        #Profilimi oluştur
        #profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        #assert profileTitleText.text != "Profilini oluştur"
        self.driver.execute_script("window.scrollBy(0, 500);")
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton = self.waitForElementVisible((By.XPATH, PROFILEBUTTON_XPATH))
        #Aşağı scroll
        self.scroll()
        profileButton.click()
        #Eğitimlerim bölümü
        #Yukarı scroll
        self.driver.execute_script("window.scrollTo(0, 0);")
        certificates= self.waitForElementVisible((By.XPATH,CERTIFICATESNAME_XPATH))
        certificates.click()

    
    #TC 13
    def test_adding_certificates (self):
        self.precondition()
        #Dosya yükleme alanına tıklanır
        self.upload_area()
        sleep(2)
        #Dosya sürükleme kodu ve seçme kodu
        self.uploadPath()
        sleep(2)
        #Çarpı butonuna tıklanır
        click_x_button = self.waitForElementVisible((By.XPATH,CLICKXBUTTON_XPATH))
        click_x_button.click()
        #Dosya sürükleme kodu ve seçme kodu
        self.uploadPath()
        sleep(3)
        #Dosya yükleme

        self.uploadFileButton()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)


    #TC 14
    def test_certificate_download_and_deletion(self):
        self.precondition()
        #Dosya yükleme alanına tıklanır
        self.upload_area()
       
        sleep(2)
        #Dosya sürükleme kodu ve seçme kodu
        self.uploadPath()
        sleep(2)

        self.uploadFileButton()


        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)

        #Dosya indirme kodu
        download_file_button = self.waitForElementVisible((By.XPATH,DOWNLOADFILEBUTTON))
        download_file_button.click()

        #Dosya silme kodu
        delete_file_button = self.waitForElementVisible((By.XPATH,DELETEFILEBUTTON))
        delete_file_button.click()
        #Dosya silme evet butonuna bas
        delete_file_yes_button = self.waitForElementVisible((By.XPATH,DELETEFILEYESBUTTON))
        delete_file_yes_button.click()
        
        delete_button_click_text=self.waitForElementVisible((By.XPATH,DELETEBUTTONCLICKTEXT_XPATH))
        assert delete_button_click_text.text == DELETEBUTTONCLICK_TEXT

    #TC 15
    def test_certificates_warning_messages(self):
        self.precondition()

        #Dosya yükleme alanına tıklanır
        self.upload_area()

        #Tobeto.txt dosyası alana sürüklenir.
        self.uploadPathTxt()        
    
        #Sadece image/jpeg, image/png, application/pdf yükleyebilirsiniz uyarı mesajı ekranda görüntülenmelidir."
        txt_file_upload_alert=self.waitForElementVisible((By.XPATH,TXTFILEUPLOADALERT_XPATH))
        assert txt_file_upload_alert.text == TXTFILEUPLOADALERT_TEXT
        sleep(3)
            
        #Tobeto.png ve Tobeto2.png dosyaları alana sürüklenir.
        self.UploadPathPng()

        # self.UploadPathPng2() 

        sleep(3) #Manuel olarak 2.dosya sürüklenmek zorunda
        
        #burda ilk mnce yüklediği dosyayı onaylaması lazım ?
        #Sadece 1 dosya yükleyebilirsiniz"" uyarı mesajı ekranda görüntülenmelidir.
        two_file_upload_alert=self.waitForElementVisible((By.XPATH,TWOFILEUPLOADALERT_XPATH))
        assert two_file_upload_alert.text == TWOFILEUPLOADALERT_TEXT
            

        


        




        


        