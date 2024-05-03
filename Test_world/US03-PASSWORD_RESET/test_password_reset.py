from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from email.header import decode_header
from selenium.webdriver.common.action_chains import ActionChains
from utilsfunc.helpers import Helpfunc





#Password Reset TC 1-6
@pytest.mark.usefixtures("setup_two")
class Test_password_reset(Helpfunc):
   
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
        self.driver.save_screenshot("images/test_password_less_than_six_characters.png")
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
        assert invalid_mail_popup.text == INVALIDMAILPOPUPXPATH_TEXT
        

    #TC 6
    def test_user_not_found_warning_message(self):
        forgot_password_button = self.waitForElementVisible((By.XPATH,FORGOT_PASSWORD_XPATH))
        forgot_password_button.click()
        forgot_email = self.waitForElementVisible((By.XPATH, FORGOT_EMAIL_XPATH))
        forgot_email.send_keys(input_not_found_email)
        sendButton = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        sendButton.click()
        assert False,NOTFOUNDEMAILPOPUP_TEXT
        



    