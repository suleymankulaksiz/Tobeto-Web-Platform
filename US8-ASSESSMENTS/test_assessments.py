import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *


class Test_Assessments():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()
    
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    #önkoşul
    def login(self):
        loginEmail= self.waitForElementVisible((By.NAME, loginEmail_name))
        loginEmail.send_keys(input_emptyuser)
        loginPassword = self.waitForElementVisible((By.NAME, loginPassword_name))
        loginPassword.send_keys(input_emptyuserpassword)
        loginButton= self.waitForElementVisible((By.XPATH, loginButton_xpath))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(HOMEPAGE_URL))
        assert HOMEPAGE_URL in self.driver.current_url
        assessments= self.waitForElementVisible((By.XPATH, assessments_xpath))
        assessments.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(ASSESSMENTS_URL))
        assert ASSESSMENTS_URL in self.driver.current_url
    
    #Kullanıcının değerlendirme alanını görüntülemesi ve Tobeto İşte Başarı Modeli testine yönlendirilmesi
    def test_assessment(self):
        self.login()
        assessments_header= self.waitForElementVisible((By.XPATH, assessments_header_xpath))
        assessments_element= self.waitForElementVisible((By.XPATH, assessment_element_xpath))
        assert assessments_header.text == assessmentsHeader_text 
        assert assessments_element.text== assessment_element_text
        # assessmentStart= self.waitForElementVisible((By.XPATH, assessmentStart_xpath))
        # assessmentStart.click()
        # assessmentStart2= self.waitForElementVisible((By.XPATH, assessmentStart2_xpath))
        # assessmentStart2.click  
        # assessmentPage= self.waitForElementVisible((By.XPATH, assessmentPage_xpath))
        # assert assessmentPage.text== assessmentPage_text
    
    #Kullanıcının Yazılımda Başarı Testi bölümü görüntülemesi ve sınava yönlendirilmesi
    def test_software_test(self): 
        self.login()
        softwareTestInformation1 = self.waitForElementVisible((By.XPATH, softwareTestInformation1_xpath))
        softwareTest = self.waitForElementVisible((By.XPATH, softwareTest_xpath))
        softwareTestStart= self.waitForElementVisible((By.XPATH, SoftwareTestStart_xpath))
        assert softwareTestInformation1.text== softwareTestInformation1_text and softwareTest.text== softwareTest_text and softwareTestStart.text ==softwareTestStart_text
        # softwareTestStart.click()
        # SoftwareTestStart2= self.waitForElementVisible((By.XPATH, SoftwareTestStart2_xpath))
        # SoftwareTestStart2.click()
        # softwareTestControl = self.waitForElementVisible((By.XPATH, softwareTestControl_xpath))
        # assert softwareTestControl.text== softwareTestControl_text
        
    #Kullanıcının "Aboneliğe özel değerlendirme araçlarını görüntülemesi
    def test_subscriber(self):
        self.login()
        subscribe= self.waitForElementVisible((By.XPATH, subscribe_xpath))
        subscribeInformation1= self.waitForElementVisible((By.XPATH, subscribeInformation1_xpath))
        subscribeInformation2=self.waitForElementVisible((By.XPATH, subscribeInformation2_xpath))
        assert subscribe.text== subscribe_text and subscribeInformation1.text== subscribeInformation1_text and subscribeInformation2.text== subscribeInformation2_text
    
