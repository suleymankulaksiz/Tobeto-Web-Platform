import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
import imaplib
import email
from email.header import decode_header
from selenium.webdriver.common.action_chains import ActionChains


class Test_password_reset:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                  
        self.driver.get(LOGIN_URL)

        # # Outlook IMAP sunucusu ve bağlantı noktası
        # self.imap_server = 'outlook.office365.com'
        # self.port = 993

        # # E-posta adresi ve şifre
        # self.username = input_forgot_email
        # self.password = input_sign_in_password

        # # IMAP bağlantısı kurma
        # self.mail = imaplib.IMAP4_SSL(self.imap_server, self.port)
        # self.mail.login(self.username, self.password)
        
                

    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    def test_password_reset(self):
        forgot_password_button = self.waitForElementVisible((By.XPATH,FORGOT_PASSWORD_XPATH))
        forgot_password_button.click()
        forgot_email = self.waitForElementVisible((By.XPATH, FORGOT_EMAIL_XPATH))
        forgot_email.send_keys(input_forgot_email)
        sendButton = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        sendButton.click()

        popupMessage = self.waitForElementVisible((By.XPATH,FORGOT_EMAIL_POPUP_XPATH))
        assert popupMessage.text == FORGOT_EMAIL_POPUP_TEXT

        self.driver.get(SIGN_IN)    
        sign_in_email = self.waitForElementVisible((By.NAME,SIGN_IN_EMAIL_NAME))
        sign_in_email.send_keys(input_forgot_email)
        next_button = self.waitForElementVisible((By.ID,next_login_button_id))
        next_button.click()
        sign_in_password = self.waitForElementVisible((By.NAME,SING_IN_PASSWORD_NAME))
        sign_in_password.send_keys(input_sign_in_password)
        sign_in_button = self.waitForElementVisible((By.ID,sign_in_button_id))
        sign_in_button.click()
        click_no_button = self.waitForElementVisible((By.ID,decline_button_id))
        click_no_button.click()
        sleep(5)
        click_nav_menu = self.waitForElementVisible((By.XPATH,NAVMENU_XPATH))
        click_nav_menu.click()
        click_outlook = self.waitForElementVisible((By.XPATH,NAVMENU_OUTLOOK_XPATH))
        click_outlook.click()
        sleep(10)
        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_reset_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_reset_password_again)
        send_button = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        send_button.click()






    