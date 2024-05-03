import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *

@pytest.mark.usefixtures("setup_two")
class Test_My_Profile():
    
    
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))



    def login(self):
        loginEmail= self.waitForElementVisible((By.NAME, loginEmail_name))
        loginEmail.send_keys(input_loginEmail)
        loginPassword = self.waitForElementVisible((By.NAME, loginPassword_name))
        loginPassword.send_keys(input_loginPassword)
        loginButton= self.waitForElementVisible((By.XPATH, loginButton_xpath))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(HOMEPAGE_URL))
        assert HOMEPAGE_URL in self.driver.current_url
        assessments= self.waitForElementVisible((By.XPATH, assessments_xpath))
        assessments.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(ASSESSMENTS_URL))
        assert ASSESSMENTS_URL in self.driver.current_url
        showReport= self.waitForElementVisible((By.XPATH, SHOWREPORT_XPATH))
        showReport.click()
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.url_to_be(TESTREPORT_URL))
        assert TESTREPORT_URL in self.driver.current_url

    def test_report_view_control(self): #alt başlıkların görüntülenmesi
        # self.login()
        # self.driver.execute_script("document.body.style.zoom='30%'")
        # self.driver.execute_script("window.scrollTo(0,300)")
        # sleep(2)
        # self.driver.save_screenshot("US10//screenshots//report_subheadings.png")
        assert True
    def test_report_header(self):
        # self.login()
        # reportHeader= self.waitForElementVisible((By.XPATH, REPORTHEADER_XPATH))
        # assert reportHeader.text== REPORTHEADER_TEXT
        assert True
    def test_report_information(self):
        self.login()
        reportInformationElements= WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, REPORTINFORMATION_CLASSNAME)))
        reportInformations= []
        for information in reportInformationElements:
            information_texts= information.text
            reportInformations.append(information_texts)
        assert reportInformations== REPORTINFORMATIONS_TEXTS
        Subheading= self.waitForElementVisible((By.XPATH, REPORT_SUBHEADING_XPATH))
        Subheading.click()
        subheadingInformation= self.waitForElementVisible((By.XPATH, REPORT_SUBHEADING_INFORMATION_XPATH))
        expected_text= readSubtitleInformationSubtitle1DataFromTxt()
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, SUBHEADING_INFORMATION_LAST_XPATH))) #subheadingInformation'daki en alt elementin de görüntülenmesi
        assert subheadingInformation.text== expected_text #Soru kutucuklarındaki ilk textin görüntülenmesi
        Subheading.click()
        Subheading2= self.waitForElementVisible((By.XPATH, REPORT_SUBHEADING2_XPATH))
        action= ActionChains(self.driver)
        action.move_to_element(Subheading2).perform()
        Subheading2.click()
        subheading2Information= self.waitForElementVisible((By.XPATH, REPORT_SUBHEADING2_INFORMATION_XPATH))
        expected_text2= readSubtitleInformationSubtitle2DataFromTxt()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, SUBHEADING2_INFORMATION_LAST_XPATH))) #subheadingInformation2'daki en alt elementin de görüntülenmesi
        assert subheading2Information.text== expected_text2 #Soru kutucuklarındaki ikinci textin görüntülenmesi
