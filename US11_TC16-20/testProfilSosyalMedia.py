import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from profilSosyalMediaPage import *
from constants.globalConstants import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Test_Chatbox: 
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        sleep(2)

    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_valid_login(self):
        userNameInput = self.waitForElementVisible((By.NAME,loginEmail_name))
        passwordInput = self.waitForElementVisible((By.NAME,loginPassword_name))
        userNameInput.send_keys(loginUserName)
        passwordInput.send_keys(loginPassword)
        loginButton = self.waitForElementVisible((By.CSS_SELECTOR,loginButton_css))
        loginButton.click()
        profilButton=self.waitForElementVisible((By.CSS_SELECTOR,profilButton_css))
        profilButton.click()
        profilButton.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
        medyaHesaplariButton=self.waitForElementVisible((By.XPATH,medyaHesaplariButton_xpath))
        medyaHesaplariButton.click()

    def test_tc16(self): #sosyal medya hesabi ekleme testi
        self.test_valid_login()
        secinizButton=self.waitForElementVisible((By.CSS_SELECTOR,secinizButton_css))
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox=self.waitForElementVisible((By.CSS_SELECTOR,sosyalMediaUrlBox_css))
        sosyalMediaUrlBox.click()
        sosyalMediaUrlBox.send_keys(linkedIn)
        kaydetButton=self.waitForElementVisible((By.CSS_SELECTOR,kaydetButton_css))
        kaydetButton.click()
        linkedInIkon=self.waitForElementVisible((By.CSS_SELECTOR,linkedInIko_css))
        assert linkedInIkon.is_displayed, "LinkedIn ikonu görünmüyor"
        deleteIkon=self.waitForElementVisible((By.CSS_SELECTOR,deleteIkon_css))
        assert deleteIkon.is_displayed, "Delete ikonu gorunmuyor"
        editIkonu=self.waitForElementVisible((By.CSS_SELECTOR,editIkonu_css))
        assert editIkonu.is_displayed, "Edit ikonu gorunmuyor"
        uyariMsji=self.waitForElementVisible((By.XPATH,uyariMsji_xpath))
        assert uyariMsji.text == msjIcerigi
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox.send_keys(instagram)
        kaydetButton.click()
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox.send_keys(twitter)
        kaydetButton.click()
        sMedyaBasariliEklendiMsj=self.waitForElementVisible((By.CSS_SELECTOR,sMedyaBasariliEklendiMsj_css))
        assert sMedyaBasariliEklendiMsj.is_displayed,"sosyal medya başariyla eklendi msji görüntülenmedi!!"
        deleteIkon.click()
        hesapSilOnayButton=self.waitForElementVisible((By.CSS_SELECTOR,hesapSilOnayButton_css))
        hesapSilOnayButton.click()
        sleep(3)
        deleteIkon.click()
        hesapSilOnayButton.click()
        sleep(3)
        deleteIkon.click()
        hesapSilOnayButton.click()
        sleep(3)

    def test_tc17(self): #ayni hesabi yeniden ekleme
        self.test_valid_login()
        sosyalMediaUrlBox=self.waitForElementVisible((By.CSS_SELECTOR,sosyalMediaUrlBox_css))
        sosyalMediaUrlBox.click()
        sosyalMediaUrlBox.send_keys(twitter)
        kaydetButton=self.waitForElementVisible((By.CSS_SELECTOR,kaydetButton_css))
        kaydetButton.click()
        doldurulmasiZorunluUyarisi=self.waitForElementVisible((By.CSS_SELECTOR,doldurulmasiZorunluUyarisi_css))
        assert doldurulmasiZorunluUyarisi.is_displayed,"uyari msji goruntulenmedi!"
        secinizButton=self.waitForElementVisible((By.CSS_SELECTOR,secinizButton_css))
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox.click()
        sosyalMediaUrlBox.send_keys(linkedIn)
        kaydetButton.click()
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox.send_keys(linkedIn)
        kaydetButton.click()
        buHesapKayitliUyarisi=self.waitForElementVisible((By.CSS_SELECTOR,buHesapKayitliUyarisi_css))
        assert buHesapKayitliUyarisi.is_displayed,"bu sosyal medya zaten mevcut uyarisi gorulmedi!! "
        deleteIkon=self.waitForElementVisible((By.CSS_SELECTOR,deleteIkon_css))
        hesapSilOnayButton=self.waitForElementVisible((By.CSS_SELECTOR,hesapSilOnayButton_css))
        hesapSilOnayButton.click()
        sleep(3)
        deleteIkon.click()

        #TC18 FAİL

    def test_tc19(self): #sosyal medya hesabi silme testi
        self.test_valid_login()
        secinizButton=self.waitForElementVisible((By.CSS_SELECTOR,secinizButton_css))
        secinizButton.click()
        secinizButton.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
        sosyalMediaUrlBox=self.waitForElementVisible((By.CSS_SELECTOR,sosyalMediaUrlBox_css))
        sosyalMediaUrlBox.send_keys(linkedIn)
        kaydetButton=self.waitForElementVisible((By.CSS_SELECTOR,kaydetButton_css))
        kaydetButton.click()
        deleteIkon=self.waitForElementVisible((By.CSS_SELECTOR,deleteIkon_css))
        hesapSilOnayButton=self.waitForElementVisible((By.CSS_SELECTOR,hesapSilOnayButton_css))
        hesapSilOnayButton.click()
        sleep(3)
        deleteIkon.click()
        basariylaSilindiMsj=self.waitForElementVisible((By.CSS_SELECTOR,basariylaSilindiMsj_css))
        assert basariylaSilindiMsj.is_displayed, "sosyal medya hesabiniz basariyla kaldirildi msji gorulmedi!!"
        
        #TC20 FAİL