import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os
import random
import string

def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])

        extension = random.choice(['com', 'net', 'org'])

        extension = random.choice(['com', 'net', 'org'])                                       #burada random mail oluşturma işlemi yapıyoruz.

    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom





class Helpfunc:
    def waitForElementVisible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    


class Test_Smokes(Helpfunc):
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/kayit-ol")
    
    def teardown_method(self):
        self.driver.quit()
    
    
    def test_register(self):
        emailrandom = generate_random_email()
        firstname = self.waitForElementVisible((By.NAME, "firstName"))
        lastname = self.waitForElementVisible((By.NAME, "lastName"))
        email = self.waitForElementVisible((By.NAME, "email" ))
        password = self.waitForElementVisible((By.NAME, "password"))
        password_again = self.waitForElementVisible((By.NAME, "passwordAgain"))
        firstname.send_keys("Ali Kemal")
        lastname.send_keys("Sinan Kaya")
        email.send_keys(emailrandom)
        password.send_keys("123456")
        password_again.send_keys("123456")
        sign_up_button = self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div/button"))
        sign_up_button.click()
        checkbox1=self.waitForElementVisible((By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='contact']"))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='membershipContrat']"))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='emailConfirmation']"))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='phoneConfirmation']"))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,"/html//input[@id='phoneNumber']"))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,"/html//input[@id='phoneNumber']"))
        input_phone_box.send_keys("549 490 30 04")
        iframe = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='recaptcha-anchor']")))
        captcha.click()
        time.sleep(20)
        self.driver.switch_to.default_content()
        continue_button =self.waitForElementVisible((By.XPATH,"/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"))       
        continue_button.click()
        wait_url = "https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(wait_url))
        alertMessage = self.waitForElementVisible((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/span"))
        assert alertMessage.text == "Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."


class Test_Smoke(Helpfunc):
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tobeto.com/giris")
    
    def teardown_method(self):
        self.driver.quit()
    
    
    def test_login(self):
        loginEmail= self.waitForElementVisible((By.NAME, "email"))
        loginEmail.send_keys("kvsyilmaz98@gmail.com")
        loginPassword = self.waitForElementVisible((By.NAME, "password"))
        loginPassword.send_keys("201618")
        loginButton= self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be("https://tobeto.com/platform"))
        assert "https://tobeto.com/platform" in self.driver.current_url






source_path = r"C:\Users\slyma\OneDrive\Masaüstü\Pair3-Tobeto-Proje-2\smoke_tests\test_smoke.py"
destination_path = r"C:\Program Files\Jenkins\TobetoSmokeTest"

shutil.copy(source_path, destination_path)