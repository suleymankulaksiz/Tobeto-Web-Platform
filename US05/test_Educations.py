import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from EducationPage import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Test_Educations: 
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL_M)
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
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform() 
        egitimlerimButton = self.waitForElementVisible((By.CSS_SELECTOR,egitimlerimbutton_css))
        egitimlerimButton.click()
        dahaFazlaGosterButton = self.waitForElementVisible((By.XPATH,dahaFazlaGoster_xpath))
        dahaFazlaGosterButton.click()

    def test_tc01(self):
        self.test_valid_login()
        tumEgitimler=self.waitForElementVisible((By.CSS_SELECTOR,tumEgitimlerim_css))
        tumEgitimler.click()
        assert len(tumEgitimler) == 16
        devamEttiklerim=self.waitForElementVisible((By.CSS_SELECTOR,devamEttiklerim_css))
        devamEttiklerim.click()
        assert len(devamEttiklerim)==13
        tamamladiklarim=self.waitForElementVisible((By.CSS_SELECTOR,tamamladiklarim_css))
        tamamladiklarim.click()
        assert len(tamamladiklarim)==15

    def test_tc02(self):
        self.test_valid_login()
        aramaKutusu=self.waitForElementVisible((By.CSS_SELECTOR,aramaKutusu_css))
        aramaKutusu.click()
        aramaKutusu.send_keys("is").click()
        aramaSonucu=self.waitForElementVisible((By.XPATH,aramaSonucu_xpath))
        assert aramaSonucu.text==sonuc

    def test_tc03(self):
        self.test_valid_login()
        kurumSeciniz=self.waitForElementVisible((By.CSS_SELECTOR,kurumSeciniz_css))
        kurumSeciniz.click()
        kurumSeciniz.send_keys(Keys.RETURN)
        assert kurumSeciniz.get_attribute("Istanbul Kodluyor"), "kurum seciniz filitresi BOŞ!"
        kurumSecinizBosalt=self.waitForElementVisible((By.CLASS_NAME,kurumSecinizBosalt_class))
        kurumSecinizBosalt.click()
        assert not  kurumSeciniz.get_attribute("Istanbul Kodluyor"), "kurum seciniz filitresi DOLU!"

        #TC04 FAİL

    def test_tc05(self):
        self.test_valid_login()
        aramaKutusu=self.waitForElementVisible((By.CSS_SELECTOR,aramaKutusu_css))
        aramaKutusu.click()
        aramaKutusu.send_keys("i").click()
        kurumSeciniz=self.waitForElementVisible((By.CSS_SELECTOR,kurumSeciniz_css))
        kurumSeciniz.click()
        kurumSeciniz.send_keys(Keys.RETURN)
        siralama=self.waitForElementVisible((By.XPATH,siralama_xpath))
        siralama.click()
        siralama.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
        #doğrulamayı yapamadım 

    def test_tc06(self):  
        self.test_valid_login()
        aramaKutusu=self.waitForElementVisible((By.CSS_SELECTOR,aramaKutusu_css))
        aramaKutusu.click()
        aramaKutusu.send_keys("tobeto").click()
        egitimYokMsj=self.waitForElementVisible((By.XPATH,egitimYokMsj_xpath))
        assert egitimYokMsj.text==msj

        #TC07 FAİL