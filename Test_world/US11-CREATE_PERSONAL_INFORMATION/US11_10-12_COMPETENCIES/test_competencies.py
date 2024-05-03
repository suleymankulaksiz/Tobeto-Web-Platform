import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from constants.globalConstants import *





@pytest.mark.usefixtures("setup_two")
class Test_Settings_Competencies():
   
    
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    #Kullanıcının giriş yapması ve Profili Oluştur sayfasında yetkinlik ekleyebilmesi
    def login(self):
        loginEmail= self.waitForElementVisible((By.NAME, loginEmail_name))
        loginEmail.send_keys(input_loginEmail)
        loginPassword = self.waitForElementVisible((By.NAME, loginPassword_name))
        loginPassword.send_keys(input_loginPassword)
        loginButton= self.waitForElementVisible((By.XPATH, loginButton_xpath))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(HOMEPAGE_URL))
        assert HOMEPAGE_URL in self.driver.current_url
        closeAlert= self.waitForElementVisible((By.XPATH, CLOSEALERT_XPATH))
        closeAlert.click() 
        createProfileButton= self.waitForElementVisible((By.XPATH, CREATEPROFILBUTTON_XPATH))
        action= ActionChains(self.driver)
        action.move_to_element(createProfileButton).perform()
        createProfileButton.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(SETTINGS_URL))
        assert SETTINGS_URL in self.driver.current_url
        settingsCompetenciesButton= self.waitForElementVisible((By.XPATH, SETTINGSCOMPETENCIESBUTTON_XPATH))
        action2= ActionChains(self.driver)
        action2.move_to_element(settingsCompetenciesButton).perform()
        settingsCompetenciesButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(COMPETENCIES_URL))
        assert COMPETENCIES_URL in self.driver.current_url

    #Kullanıcının yetkinlik ekleyebilmesinin kontrolü
    def test_add_competence(self):
        self.login()
        dropDownCompetencies= self.waitForElementVisible((By.XPATH, DROPDOWNCOMPETENCIES_XPATH))
        dropDownCompetencies.click()
        dropDownOption1= self.waitForElementVisible((By.ID, DROPDOWNOPTION1_ID))
        dropDownOption1.click()
        dropDownCompetencies.click()
        self.driver.save_screenshot("US11//screenshots//c#is_not_on_theList.png")
        assert True #seçilen ögenin açılır listede görüntülenmediğinin kontrolü
        dropDownOption2= self.waitForElementVisible((By.ID, DROPDOWNOPTION2_ID))
        dropDownOption2.click()
        deleteFirstOption= self.waitForElementVisible((By.XPATH, DELETEFIRSTOPTION_XPATH))
        deleteFirstOption.click()
        self.driver.save_screenshot("US11//screenshots//deleted_first_option.png")
        assert True #seçilen ögenin çarpı butonuyla yetkinlik ekle bölümünden silinmesi
        saveCompetencies= self.waitForElementVisible((By.XPATH, SAVECOMPETENCIES_XPATH))
        saveCompetencies.click()
        competenciesSavedControl= self.waitForElementVisible((By.XPATH, COMPETECENTIES_SAVED_CONTROL_XPATH))
        assert competenciesSavedControl.text== COMPETENCIES_SAVED_CONTROL_TEXT
    
    #Kullanıcının yetkinlik eklemeden kaydet butonuna tıkladığında uyarı mesajı alması
    def test_empty_competence(self):
        self.login()
        saveCompetencies= self.waitForElementVisible((By.XPATH, SAVECOMPETENCIES_XPATH))
        saveCompetencies.click()
        emptyCompetenceAlert= self.waitForElementVisible((By.XPATH, EMPTYCOMPETENCEALERT_XPATH))
        assert emptyCompetenceAlert.text== EMPTYCOMPETENCEALERT_TEXT


    #Kullanıcının yetkinlik silme işlemi
    def test_delete_competence(self):
        self.login()
        deleteCompetenceButton= self.waitForElementVisible((By.XPATH, DELETECOMPETENCEBUTTON_XPATH))
        action3= ActionChains(self.driver)
        action3.move_to_element(deleteCompetenceButton).perform()
        deleteCompetenceButton.click()
        deleteCompetenceButton2= self.waitForElementVisible((By.XPATH, DELETECOMPETENCEBUTTON2_XPATH))
        deleteCompetenceButton2.click()
        competenceDeletedAlert= self.waitForElementVisible((By.XPATH, COMPETENCEDELETEDALERT_XPATH))
        assert competenceDeletedAlert.text== COMPETENCEDELETEDALERT_TEXT



    
        
        


        

