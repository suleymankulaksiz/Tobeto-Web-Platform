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

#Sertifikalarım TC 13-15
class Test_adding_certificates:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def save_buttons(self):
        education_save_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        education_save_button.click()

    def precondition(self):
        #Login
        login_email = self.waitForElementVisible((By.XPATH,LOGIN_MAIL_XPATH))
        login_email.send_keys(input_personal_mail)
        login_password = self.waitForElementVisible((By.XPATH,LOGIN_PASSWORD_XPATH))
        login_password.send_keys(input_personal_password)
        login_button = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        login_button.click()
        popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        assert popupMessage.text == POPUP_MESSAGE_TEXT
        #Profilimi oluştur
        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == "Profilini oluştur"
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton.click()
        #Eğitimlerim bölümü
        certificates= self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[5]/span[2]"))
        certificates.click()

    
    #TC 13
    def test_adding_education_information(self):
        self.precondition()
        page_file_upload_button=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[1]/svg"))
        page_file_upload_button.click()

        #Dosya sürükleme kodu yaz

        click_x_button = self.waitForElementVisible((By.XPATH,"//*[@id='uppy_uppy-tobeto/pdf-1e-application/pdf-3578407-1713434434961']/div[2]/div[2]/button"))
        click_x_button.click()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)

        browse_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button"))
        browse_button.click()

        #Dosya seçme kodu

        file_upload_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button"))
        file_upload_button.click()

    #TC 14
    def test_certificate_download_and_deletion(self):
        self.precondition()
        page_file_upload_button=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[1]/svg"))
        page_file_upload_button.click()

        #Dosya sürükleme kodu yaz

        browse_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button"))
        browse_button.click()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)

        browse_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button"))
        browse_button.click()

        #Dosya seçme kodu

        file_upload_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button"))
        file_upload_button.click()

        download_file_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[4]/span[1]"))
        download_file_button.click()

        delete_file_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[4]/span[2]"))
        delete_file_button.click()

        delete_file_yes_button = self.waitForElementVisible((By.XPATH,"/html/body/div[4]/div/div/div/div/div/div[2]/button[2]"))
        delete_file_yes_button.click()

        delete_button_click_text=self.waitForElementVisible((By.XPATH,"/html/body/div[4]/div/div/div/div/div/p[1]"))
        assert delete_button_click_text.text == "Seçilen sertifikayı silmek istediğinize emin misiniz?"

    #TC 15
    def test_certificates_warning_messages(self):
        self.precondition()
        page_file_upload_button=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[1]/svg"))
        page_file_upload_button.click()

        #Tobeto.txt dosyası alana sürüklenir.

        #Sadece image/jpeg, image/png, application/pdf yükleyebilirsiniz uyarı mesajı ekranda görüntülenmelidir."
            
        #Tobeto.png ve Tobeto2.png dosyaları alana sürüklenir.

        #Sadece 1 dosya yükleyebilirsiniz"" uyarı mesajı ekranda görüntülenmelidir.

        




        


        