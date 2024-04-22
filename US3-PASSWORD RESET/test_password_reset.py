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
import time
import ctypes
from imap_tools import MailBox
from imap_tools import AND, OR, NOT
import re
import requests


# user32 = ctypes.windll.user32

#Password Reset TC 1-6
class Test_password_reset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()
    
    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def precondition(self):
        forgot_password_button = self.waitForElementVisible((By.XPATH,FORGOT_PASSWORD_XPATH))
        forgot_password_button.click()
        forgot_email = self.waitForElementVisible((By.XPATH, FORGOT_EMAIL_XPATH))
        forgot_email.send_keys(input_forgot_email)
        sendButton = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        sendButton.click()

        popupMessage = self.waitForElementVisible((By.XPATH,FORGOT_EMAIL_POPUP_XPATH))
        assert popupMessage.text == FORGOT_EMAIL_POPUP_TEXT

        self.driver.get(SIGN_IN)    
        sign_in_email = self.waitForElementVisible((By.ID,"identifierId"))
        sign_in_email.send_keys(input_forgot_email)
        next_button = self.waitForElementVisible((By.XPATH,"//*[@id='identifierNext']/div/button/span"))
        next_button.click()
        sign_in_password = self.waitForElementVisible((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))
        sign_in_password.send_keys(input_sign_in_password)
        sign_in_button = self.waitForElementVisible((By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"))
        sign_in_button.click()
        #Last mail click
        last_mail_link = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".zA.zE:nth-child(1)"))) 
        last_mail_link.click()
        sleep(4)
        #Açılan sayfaya geçer
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        #Mail içerisindeki linke tıklar.
        email_content_xpath = "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div"
        email_content_element = self.waitForElementVisible((By.XPATH,email_content_xpath))
        email_content = email_content_element.text
        link_start_index = email_content.find("https://")  # Linkin başlangıç indeksi
        link_end_index = email_content.find(" ", link_start_index)  # Linkin sonraki boşluk karakterine kadar olan kısmı alır

        if link_start_index != -1:
            link_url = email_content[link_start_index:link_end_index]  # Linki al
            # Linki tarayıcıda aç
            self.driver.get(link_url)

    #TC 1
    def test_password_reset(self):
        self.precondition()

        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_reset_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_reset_password_again)
        reset_send_button = self.waitForElementVisible((By.XPATH,RESETSENDBUTTON_XPATH))
        reset_send_button.click()

    #TC 2
    def test_password_less_than_six_characters(self):
        self.precondition()
        #Ekran görüntüsü alır
        self.driver.save_screenshot("images/sendButtonPassive.png")
        #Butonun pasif olma durumunu kontrol eder.
        try:
           reset_send_button = self.waitForElementVisible((By.XPATH,RESETSENDBUTTON_XPATH))
           assert reset_send_button is not None, "Button is visible"
           print("Button is visible")
        except Exception :
           print("Button is not visible")

        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_min_reset_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_min_reset_password_again)
        reset_send_button = self.waitForElementVisible((By.XPATH,RESETSENDBUTTON_XPATH))
        reset_send_button.click()
        assert False,INCORRECTPASSWORDPOPUP_TEXT

    #TC 3
    def test_passwords_not_matching(self):
        self.precondition()

        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_different_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_different_password_again)
        reset_send_button = self.waitForElementVisible((By.XPATH,RESETSENDBUTTON_XPATH))
        reset_send_button.click()
        password_not_matched_popup = self.waitForElementVisible((By.XPATH,PASSWORDNOTMATCHEDPOPUP_XPATH))
        assert password_not_matched_popup.text == PASSWORDNOTMATCHEDPOPUP_TEXT
    
    #TC 4
    def test_same_old_password(self):
        self.precondition()

        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_same_old_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_same_old_password_again)
        reset_send_button = self.waitForElementVisible((By.XPATH,RESETSENDBUTTON_XPATH))
        reset_send_button.click()
        assert False,SAMEOLDPASSWORDPOPUP_TEXT

    #TC 5   
    def test_email_invalid_format(self):
        forgot_password_button = self.waitForElementVisible((By.XPATH,FORGOT_PASSWORD_XPATH))
        forgot_password_button.click()
        forgot_email = self.waitForElementVisible((By.XPATH, FORGOT_EMAIL_XPATH))
        forgot_email.send_keys(input_forgot_invalid_email)
        sendButton = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        sendButton.click()
        invalid_mail_popup = self.waitForElementVisible((By.XPATH,INVALIDMAILPOPUP_XPATH))
        assert invalid_mail_popup.text == "• Girdiğiniz e-posta geçersizdir."

    #TC 6
    def test_user_not_found_warning_message(self):
        forgot_password_button = self.waitForElementVisible((By.XPATH,FORGOT_PASSWORD_XPATH))
        forgot_password_button.click()
        forgot_email = self.waitForElementVisible((By.XPATH, FORGOT_EMAIL_XPATH))
        forgot_email.send_keys(input_not_found_email)
        sendButton = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        sendButton.click()
        assert False,NOTFOUNDEMAILPOPUP_TEXT




    