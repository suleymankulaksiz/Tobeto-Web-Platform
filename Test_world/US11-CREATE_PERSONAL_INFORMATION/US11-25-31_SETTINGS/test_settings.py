from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytest
from utilsfunc.helpers import Helpfunc


@pytest.mark.usefixtures("setup_two")
class Test_Settings(Helpfunc):
    
    
    
    
    
#"Ayarlarım" sayfasınında şifre değişikliği kontorlü
    def test_change_password(self):
        self.login()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        old_password.send_keys(input_setting_password)
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password.send_keys(input_setting_newPassword)
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        new_setting_password_again.send_keys(input_setting_newPassword)
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        change_password_alert = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_ALERT_XPATH))
        assert change_password_alert.text == TRUE_CHANGE_PASSWORD_TEXT  


#"Ayarlarım" sayfasında üyelik sonlandırılması.
    def test_termination_user(self):
        self.login_two()
        termination_button =self.waitForElementVisible((By.XPATH,TERMINATION_BUTTON_XPATH))
        termination_button.click() 
        termination_window = self.waitForElementVisible((By.XPATH,TERMINATION_WINDOW_XPATH))
        assert termination_window.text == TERMINATION_WINDOW_TEXT     
        yes_button =self.waitForElementVisible((By.XPATH,TERMINATION_YES_BUTTON_XPATH)) 
        yes_button.click()
        termination_alert = self.waitForElementVisible((By.XPATH,TERMINATION_ALERT_XPATH))
        self.driver.save_screenshot("images/terminationUser.png")
        assert termination_alert.text == TERMINATION_EXPECTED_TEXT
        
        
#"Ayarlarım" sayfasında zorunlu alanların boş bırakılması
    def test_empty_setting_password(self):
        self.login_two()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        if old_password.get_attribute("value") == "" or new_setting_password.get_attribute("value") == "" or new_setting_password_again.get_attribute("value") == "":
           change_password_alert = self.waitForElementVisible((By.XPATH, EMPTY_PASSWORD_ALERT_XPATH))
        assert change_password_alert.text == EMPTY_FIELDS_TEXT     


#"Ayarlarım" sayfasında mevcut şifrenin geçersiz olma durumu  
    def test_wrong_oldPassword_change(self):
        self.login_two()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        old_password.send_keys("999999")
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password.send_keys(input_setting_newPassword)
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        new_setting_password_again.send_keys(input_setting_newPassword)
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        old_change_password_alert = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_ALERT_XPATH))
        assert old_change_password_alert.text == WRONG_OLD_PASSWORD_TEXT


#"Ayarlarım" sayfasında "Yeni Şifre*" ve "Yeni Şifre Tekrar*" bölümleri 6 karakterden az girilmesi durumu
    def test_short_password_change(self):
        self.login_two()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        old_password.send_keys(input_setting_password_two)
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password.send_keys("12345")
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        new_setting_password_again.send_keys("12345")
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        change_newPassword_alert = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_ALERT_XPATH))
        assert change_newPassword_alert.text == SHORT_PASSWORD_TEXT


#"Ayarlarım" sayfasında yenilenen şifrenin eski şifre ile aynı olması durumu
    def test_same_change_password(self):
        self.login_two()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        old_password.send_keys(input_setting_password_two)
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password.send_keys(input_setting_password_two)
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        new_setting_password_again.send_keys(input_setting_password_two)
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        same_password_alert = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_ALERT_XPATH))
        assert same_password_alert.text == SAME_CHANGE_PASSWORD_TEXT


#"Ayarlarım" sayfasında "Yeni Şifre" kutucuğuna ve "Yeni Şifre Tekrar" kutucuğuna farklı şifrelerin girilmesi durumu
    def test_different_newPassword(self):
        self.login_two()
        old_password = self.waitForElementVisible((By.NAME,OLD_PASSWORD_XPATH))
        old_password.send_keys(input_setting_password_two)
        new_setting_password = self.waitForElementVisible((By.NAME,PASSWORD_NAME))
        new_setting_password.send_keys("999999")
        new_setting_password_again = self.waitForElementVisible((By.NAME,NEW_PASSWORD_AREA_XPATH))
        new_setting_password_again.send_keys("888888")
        change_passwordButton = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_BUTTON_XPATH))
        change_passwordButton.click()
        diffrent_newPassword_alert = self.waitForElementVisible((By.XPATH,CHANGE_PASSWORD_ALERT_XPATH))
        assert diffrent_newPassword_alert.text == DIFFRENT_PASSWORD_TEXT
