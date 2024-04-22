from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import json
from time import sleep
from constants.globalConstants import *
from pathlib import Path

class Test_Languages:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                
        self.driver.get(LOGIN_URL)
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        email.send_keys(tobeto_email)
        password.send_keys(tobeto_password)
        loginBtn=self.waitForElementVisible((By.XPATH, LOGİNBUTTON_XPATH))
        loginBtn.click()
        sleep(10)
        right_name_dropdown=self.waitForElementVisible((By.XPATH, RİGHT_NAME_DROPDOWN_XPATH))
        right_name_dropdown.click()
        dropdown_profile_info=self.waitForElementVisible((By.CLASS_NAME, DROPDOWN_PROFİLE_INFO_CLASS_NAME))
        dropdown_profile_info.click()
        sleep(2)
        my_language_sidebar=self.waitForElementVisible((By.XPATH, MY_LANGUAGE_SİDEBAR_XPATH))
        my_language_sidebar.click()
        self.folderPath= str("screenshots") 
        Path(self.folderPath).mkdir(exist_ok=True) #klasörü oluşturmak için ve o klasördeki veriyi korumak için
        yield
        self.driver.quit()

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def select_german(self):
        select_the_language_dropdown=self.waitForElementVisible((By.XPATH, SELECT_THE_LANGUAGE_DROPDOWN_XPATH))
        sleep(2)
        select_the_language_dropdown.click()
        selection_german=self.waitForElementVisible((By.XPATH, OPTİON_GERMAN_XPATH))
        selection_german.click()
        select_level=self.waitForElementVisible((By.XPATH, SELECT_LEVEL_XPATH))
        select_level.click()
        add_basic_level=self.waitForElementVisible((By.XPATH, BASİC_LEVEL_XPATH))
        add_basic_level.click()
        save_button=self.waitForElementVisible((By.XPATH, SAVE_BUTTON_XPATH))
        save_button.click()
    
    
    def test_my_languages(self):
        self.select_german()
        added=self.waitForElementVisible((By.XPATH, ADDED_XPATH))
        assert added.text==ADDED_LANGUAGE_TEXT
        #çekçe
        select_the_language_dropdown=self.waitForElementVisible((By.XPATH, SELECT_THE_LANGUAGE_DROPDOWN_XPATH))
        sleep(2)
        select_the_language_dropdown.click()
        selection_cekce=self.waitForElementVisible((By.XPATH, OPTİON_CEKCE_XPATH))
        selection_cekce.click()
        select_level=self.waitForElementVisible((By.XPATH, SELECT_LEVEL_XPATH))
        select_level.click()
        add_advanced_level=self.waitForElementVisible((By.XPATH, ADVANCED_LEVEL_XPATH))
        add_advanced_level.click()
        save_button=self.waitForElementVisible((By.XPATH, SAVE_BUTTON_XPATH))
        save_button.click()
        #çince
        select_the_language_dropdown=self.waitForElementVisible((By.XPATH, SELECT_THE_LANGUAGE_DROPDOWN_XPATH))
        sleep(2)
        select_the_language_dropdown.click()
        selection_cince=self.waitForElementVisible((By.XPATH, OPTİON_CHINESE_XPATH))
        selection_cince.click()
        select_level=self.waitForElementVisible((By.XPATH, SELECT_LEVEL_XPATH))
        select_level.click()
        add_mother_language_level=self.waitForElementVisible((By.XPATH, MOTHER_LANGUAGE_LEVEL_XPATH))
        add_mother_language_level.click()
        save_button=self.waitForElementVisible((By.XPATH, SAVE_BUTTON_XPATH))
        save_button.click()
        langs_section = self.driver.find_element(By.XPATH, LANS_SECTİON_XPATH)
        sleep(2)
        lang_edit_elements = langs_section.find_elements(By.XPATH, LANG_EDİT_ELEMENT_XPATH)
        assert len(lang_edit_elements)==3     
        
   
    def test_required_field(self): #DONE
        save_button=self.waitForElementVisible((By.XPATH, SAVE_BUTTON_XPATH))
        save_button.click()
        language_required_field=self.waitForElementVisible((By.XPATH, LANGUAGE_REQUİRED_FİELD_XPATH))
        level_required_field=self.waitForElementVisible((By.XPATH, LEVEL_REQUİRED_FİELD_XPATH))
        assert language_required_field, level_required_field== REQUİRED_FİELD_TEXT
    
    def test_delete_language(self): #DONE
        go_to_language=self.waitForElementVisible((By.XPATH, GO_TO_LANGUAGE_XPATH)) 
        actions = ActionChains(self.driver)
        actions.move_to_element(go_to_language).perform()
        delete_element = self.waitForElementVisible((By.XPATH, DELETE_ELEMENT_XPATH))
        delete_element.click()
        sleep(2)
        answer_yes=self.waitForElementVisible((By.XPATH, ANSWER_YES_XPATH))
        answer_yes.click()
        sleep(2)
        successful_message=self.waitForElementVisible((By.XPATH, REMOVED_MESSAGE_XPATH))
        assert successful_message.text==LANGUAGE_REMOVED_TEXT
    
    def test_added_same_language(self): #DONE
        self.select_german()
        already_added=self.waitForElementVisible((By.XPATH, ALREADY_ADDED_MESSAGE_XPATH))
        assert already_added.text==ALREADY_EXİSTS_LANGUAGE_TEXT
 
        
    #@pytest.mark.skip()
    def test_my_foreign_language(self): #Yukarıdakileri tek def içinde denedim
        save_button=self.waitForElementVisible((By.XPATH, SAVE_BUTTON_XPATH))
        save_button.click()
        language_required_field=self.waitForElementVisible((By.XPATH, LANGUAGE_REQUİRED_FİELD_XPATH))
        level_required_field=self.waitForElementVisible((By.XPATH, LEVEL_REQUİRED_FİELD_XPATH))
        self.select_german()
        added=self.waitForElementVisible((By.XPATH, ADDED_XPATH))   
        sleep(2)
        self.select_german()
        already_added=self.waitForElementVisible((By.XPATH, ALREADY_ADDED_MESSAGE_XPATH))
        sleep(1)
        go_to_language=self.waitForElementVisible((By.XPATH, GO_TO_LANGUAGE_XPATH)) 
        actions = ActionChains(self.driver)
        actions.move_to_element(go_to_language).perform()
        delete_element = self.waitForElementVisible((By.XPATH, DELETE_ELEMENT_XPATH))
        delete_element.click()
        sleep(2)
        answer_yes=self.waitForElementVisible((By.XPATH, ANSWER_YES_XPATH))
        answer_yes.click()
        successful_message=self.waitForElementVisible((By.XPATH, REMOVED_MESSAGE_XPATH))
        assert {language_required_field, level_required_field== REQUİRED_FİELD_TEXT and
                added.text==ADDED_LANGUAGE_TEXT and 
                already_added.text==ALREADY_EXİSTS_LANGUAGE_TEXT and
                successful_message.text==LANGUAGE_REMOVED_TEXT}
        
        
        
        

