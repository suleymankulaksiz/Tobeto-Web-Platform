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


user32 = ctypes.windll.user32

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

        # link_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,"//a[contains(@href,'https://tobeto.com/reset-password')]")))
        # link_element.click()
        # link_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[7]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div/div/p/span")))
        # link_element.click()

        # link_script = """
        # var links = document.querySelectorAll("a");
        # for(var i = 0; i < links.length; i++) {
        #     if (links[i].href.startsWith("https://tobeto.com/reset-password?code=")) {
        #         links[i].click();
        #         break;
        #     }
        # }
        # """
        # self.driver.execute_script(link_script)

        email_content_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=':1z']/div[1]/div/div/div/p/span/a")))
        email_content = email_content_element.text
        link_start_index = email_content.find("https://")  # Linkin başlangıç indeksi
        link_end_index = email_content.find(" ", link_start_index)  # Linkin sonraki boşluk karakterine kadar olan kısmı alır

        if link_start_index != -1 and link_end_index != -1:
            link_url = email_content[link_start_index:link_end_index]  # Linki al
            # Linki tarayıcıda aç
            self.driver.get(link_url)

        sleep(5)
        

        # first_message = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "//a[contains(@href,'https://tobeto.com/reset-password?code=')]")))
        # first_message.click()

        reset_password = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_XPATH))
        reset_password.send_keys(input_reset_password)
        reset_password_again = self.waitForElementVisible((By.XPATH,RESET_PASSWORD_AGAIN_XPATH))
        reset_password_again.send_keys(input_reset_password_again)
        send_button = self.waitForElementVisible((By.XPATH,SENDBUTTON_XPATH))
        send_button.click()






    