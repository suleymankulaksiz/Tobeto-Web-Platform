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


class Test_adding_education_information:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
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
        education_information= self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]"))
        education_information.click()

    def test_adding_education_information(self):
        self.test_precondition()
        #Eğitim seçilir
        dropdown_element_education = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select"))
        )
        dropdown = Select(dropdown_element_education)
        # indekse göre seçim yapın
        dropdown.select_by_index(1)
        
        university_name = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"))
        university_name.send_keys("Gebze Teknik Üniversitesi")

        section_name = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"))
        section_name.send_keys("Bilgisayar Mühendisliği")

        start_year = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input"))
        start_year.click()
        select_year = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]"))
        select_year.click()

        end_year = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input"))
        end_year.click()
        select_end_year = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[7]"))
        select_end_year.click()
        
        education_click_button = self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button"))
        education_click_button.click()

        


        