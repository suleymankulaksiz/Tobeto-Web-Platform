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

#EDUCATION TC 8-9
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
    
    def save_buttons(self):
        education_save_button = self.waitForElementVisible((By.XPATH,EDUCATIONSAVEBUTTON_XPATH))
        education_save_button.click()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def precondition(self):
        #Login
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
        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == PROFILETITLETEXT
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        self.scroll()
        profileButton.click()
        #Eğitimlerim bölümü
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        education_information= self.waitForElementVisible((By.XPATH,EDUCATIONSAVEBUTTON_XPATH))
        education_information.click()

    #TC-8
    def test_adding_education_information(self):
        self.precondition()
        #Eğitim seçilir
        dropdown_element_education = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWNELEMENTEDUCATION_XPATH))
        )
        dropdown = Select(dropdown_element_education)
        # indekse göre seçim yapın
        dropdown.select_by_index(1)
        
        university_name = self.waitForElementVisible((By.XPATH,EDUCATIONUNIVERSITYNAME_XPATH))
        university_name.send_keys(universityNameText)

        section_name = self.waitForElementVisible((By.XPATH,EDUCATIONSECTIONNAME_XPATH))
        section_name.send_keys(education_section_name)

        start_year = self.waitForElementVisible((By.XPATH,EDUCATIONSTARTYEAR_XPATH))
        start_year.click()
        select_year = self.waitForElementVisible((By.XPATH,EDUCATIONSELECTYEAR_XPATH))
        select_year.click()

        end_year = self.waitForElementVisible((By.XPATH,EDUCATIONENDYEAR_XPATH))
        end_year.click()
        select_end_year = self.waitForElementVisible((By.XPATH,EDUCATIONSELECTENDYEAR_XPATH))
        select_end_year.click()
        
        self.save_buttons()
    #TC-9
    def test_warning_messages(self):
        self.precondition()
        section_name = self.waitForElementVisible((By.XPATH,EDUCATIONSECTIONNAME_XPATH))
        section_name.send_keys("e")

        university_name = self.waitForElementVisible((By.XPATH,EDUCATIONUNIVERSITYNAME_XPATH))
        university_name.send_keys("e"* 301)  

        self.save_buttons()



        


        