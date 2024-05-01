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


def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

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
        popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        assert popupMessage.text == POPUP_MESSAGE_TEXT

        alert_quit = self.waitForElementVisible((By.XPATH, LOGIN_POPUP_ALERTQUIT_XPATH))
        alert_quit.click()
        
        #Profilimi oluştur
        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == PROFILETITLETEXT
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton = self.waitForElementVisible((By.XPATH, PROFILEBUTTON_XPATH))
        self.scroll()
        profileButton.click()
        #Deneyimler bölümüne gidilir
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        experienceButton  = self.waitForElementVisible((By.XPATH,EXPERIENCEBUTTON_XPATH))
        experienceButton.click()