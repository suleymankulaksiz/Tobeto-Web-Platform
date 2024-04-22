import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from ChatboxPage import *
from constants.globalConstants import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Test_Chatbox: 
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        sleep(2)

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def test_valid_login(self):
        userNameInput = self.waitForElementVisible((By.NAME,loginEmail_name))
        passwordInput = self.waitForElementVisible((By.NAME,loginPassword_name))
        userNameInput.send_keys(loginUserName)
        passwordInput.send_keys(loginPassword)
        loginButton = self.waitForElementVisible((By.CSS_SELECTOR,loginButton_css))
        loginButton.click()
        #mesaj ikonunun tikla bunun için iframe gec
        iframe=self.driver.find_element(By.ID,"popUpIframe")
        self.driver.switch_to.frame(iframe)
        msjIkon=self.waitForElementVisible((By.CSS_SELECTOR,msjIkon_css))
        msjIkon.click()
        #self.driver.switch_to.default_content()   #iframeden cık
        
    def test_tc01(self): #msj kutusunu kücültme ıkonun testi
        self.test_valid_login()
        kucultmeIkon=self.waitForElementVisible((By.CSS_SELECTOR,kucultmeIkon_css))
        kucultmeIkon.click()
        msjIkon=self.waitForElementVisible((By.CSS_SELECTOR,msjIkon_css))
        assert not msjIkon.is_displayed, "Mesaj kutusu hala acik"

    def test_tc02(self): #karsılama msjları ve ad-soyad bilgisi testi
        self.test_valid_login()
        karsilamaMsjlari=self.waitForElementVisible((By.CSS_SELECTOR,karsilamaMsjlari_css))
        assert karsilamaMsjlari.is_displayed, "Karsilama msjlari görüntülenmiyor"
        adSoyadBox=self.waitForElementVisible((By.CSS_SELECTOR,adSoyadBox_css))
        assert adSoyadBox.is_displayed, "Ad-soyad kutusu görüntülenemiyor"
        adSoyadBox.send_keys(adSoyad,Keys.ENTER)
        memnunOldumMsj=self.waitForElementVisible((By.XPATH,memnunOldumMsj_xpath))
        assert memnunOldumMsj.is_displayed,"isime memnun oldum msjı görüntülenmedi"

    def test_tc03(self): #emojilerin testi
        self.test_valid_login()
        adSoyadBox=self.waitForElementVisible((By.CSS_SELECTOR,adSoyadBox_css))
        adSoyadBox.click()
        adSoyadBox.send_keys(adSoyad,Keys.ENTER)
        yardimKonusu=self.waitForElementVisible((By.XPATH,yardimKonusu_xpath))
        yardimKonusu.click()
        emojiButton=self.waitForElementVisible((By.CSS_SELECTOR,emojiButton_css))
        emojiButton.click()
        elEmojisi=self.waitForElementVisible((By.CSS_SELECTOR,elEmojisi_css))
        elEmojisi.click()
        elEmojisi.send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)  #orta-acık el rengi secildi
        sleep(2)
        renkliEl=self.waitForElementVisible((By.XPATH,renkliEl_xpath))
        #el emojisi renginin değistiğini doğrulama yapılacak!!!
        #assert renkliEl.value_of_css_property("color") == "renk_kodu", "El emojisinin rengi değişmedi!"
        
    def test_tc04(self): #atach testi
        self.test_valid_login()
        adSoyadBox=self.waitForElementVisible((By.CSS_SELECTOR,adSoyadBox_css))
        adSoyadBox.click()
        adSoyadBox.send_keys(adSoyad,Keys.ENTER)
        yardimKonusu=self.waitForElementVisible((By.XPATH,yardimKonusu_xpath))
        yardimKonusu.click()
        atachIkon=self.waitForElementVisible((By.CSS_SELECTOR,atachIkon_css))
        atachIkon.click()
        dosyaSecButton=self.waitForElementVisible((By.CSS_SELECTOR,dosyaSecButton_css)).click()
        yuklenecekDosyaPath='C:\\Users\\my\\Desktop\\Pair3-Tobeto-Project\\Pair3-Tobeto-Proje\\US6\\theFileForChatbox.png'
        #burdaki hatayı anlayamadım çözemedim
        dosyaSecButton.send_keys(yuklenecekDosyaPath,Keys.ENTER)
        gonderButton=self.waitForElementVisible((By.XPATH,gonderButton_xpath))
        gonderButton.click()
        dosyaGonderimiDogrulama=self.waitForElementVisible((By.XPATH,dosyaGonderimiDogrulama_xpath))
        assert dosyaGonderimiDogrulama.text==expectedResult
        
        #TC05 FAİL

    def test_tc06(self): #Gorusmeyi sonlandırma
        self.test_valid_login()
        gorusmeyiSonlandirIkon=self.waitForElementVisible((By.CSS_SELECTOR,gorusmeyiSonlandirIkon_css))
        gorusmeyiSonlandirIkon.click()
        hayirButton=self.waitForElementVisible((By.XPATH,hayirButton_xpath))
        hayirButton.click()
        evetButton=self.waitForElementVisible((By.XPATH,evetButton_xpath))
        evetButton.click()
        gorusmeSonlandirmaDoğrulama=self.waitForElementVisible((By.XPATH,gorusmeSonlandirmaDoğrulama_xpath))
        assert gorusmeSonlandirmaDoğrulama.text==expectedDogrulama