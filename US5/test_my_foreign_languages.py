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
    def setup_method(self):
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
        right_name_dropdown=self.waitForElementVisible(RİGHT_NAME_DROPDOWN_XPATH)
        right_name_dropdown.click()
        dropdown_profile_info=self.waitForElementVisible(DROPDOWN_PROFİLE_INFO_CLASS_NAME)
        dropdown_profile_info.click()
        sleep(2)
        my_language_sidebar=self.waitForElementVisible(MY_LANGUAGE_SİDEBAR_XPATH)
        my_language_sidebar.click()
        self.folderPath= str("screenshots") #==>12.04.2024
        Path(self.folderPath).mkdir(exist_ok=True) #klasörü oluşturmak için ve o klasördeki veriyi korumak için

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    

    def test_my_languages(self):
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        selection_almanca=self.waitForElementVisible(OPTİON_ALMANCA_XPATH).click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH).click()
        add_basic_level=self.waitForElementVisible(BASİC_LEVEL_XPATH).click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH).click()
        added=self.waitForElementVisible(ADDED_XPATH)
        assert added.text==ADDED_LANGUAGE_TEXT
        #çekçe
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        selection_cekce=self.waitForElementVisible(OPTİON_CEKCE_XPATH)
        selection_cekce.click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH)
        select_level.click()
        add_advanced_level=self.waitForElementVisible(ADVANCED_LEVEL_XPATH)
        add_advanced_level.click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        #çince
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        selection_cince=self.waitForElementVisible(OPTİON_CİNCE_XPATH)
        selection_cince.click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH)
        select_level.click()
        add_mother_language_level=self.waitForElementVisible(MOTHER_LANGUAGE_LEVEL_XPATH)
        add_mother_language_level.click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        langs_section = self.driver.find_element(By.XPATH, "//div[@class='tobeto-light-bg section-p my-langs']")
        lang_edit_elements = langs_section.find_elements(By.XPATH, "//div[@class='lang-edit']")
        assert len(lang_edit_elements)==4 #burası yanlıs     
   
    def test_required_field(self):
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        language_required_field=self.waitForElementVisible(LANGUAGE_REQUİRED_FİELD_XPATH)
        level_required_field=self.waitForElementVisible(LEVEL_REQUİRED_FİELD_XPATH)
        assert language_required_field, level_required_field== REQUİRED_FİELD_TEXT
    
    def test_delete_language(self):
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        selection_norvecce=self.waitForElementVisible(OPTİON_NORVECCE_XPATH)
        selection_norvecce.click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH)
        select_level.click()
        add_basic_level=self.waitForElementVisible(BASİC_LEVEL_XPATH)
        add_basic_level.click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        #added=self.waitForElementVisible((By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"))
        #assert added.text=="• Yabancı dil bilgisi eklendi."
        sleep()
        selected_norvecce= self.waitForElementVisible((By.XPATH, SELECTED_NORVEGİAN))
        delete=self.waitForElementVisible((By.CSS_SELECTOR, "div:nth-of-type(2) > .delete-lang"))
        actions = ActionChains(self.driver)
        actions.move_to_element(selected_norvecce).move_to_element(delete).click().perform() #niye görmüyo burayıııııııı????
        answer_yes=self.waitForElementVisible(ANSWER_YES_XPATH)
        answer_yes.click()
        sleep(2)
        successful_message=self.waitForElementVisible(REMOVED_MESSAGE_XPATH)
        assert successful_message.text==LANGUAGE_REMOVED_TEXT
    
    def test_added_same_language(self): #done
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        selection_english=self.waitForElementVisible(OPTİON_ENGLİSH_XPATH)
        selection_english.click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH)
        select_level.click()
        add_intermediate_level=self.waitForElementVisible(INTERMEDİATE_LEVEL_XPATH)
        add_intermediate_level.click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        already_added=self.waitForElementVisible(ALREADY_ADDED_MESSAGE_XPATH)
        assert already_added.text==ALREADY_EXİSTS_LANGUAGE_TEXT
 
        
    @pytest.mark.skip()
    def test_my_foreign_language(self): #tukarıdakilerş tek def içinde denedim
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH)
        save_button.click()
        language_required_field=self.waitForElementVisible(LANGUAGE_REQUİRED_FİELD_XPATH)
        level_required_field=self.waitForElementVisible(LEVEL_REQUİRED_FİELD_XPATH)
        assert language_required_field, level_required_field== REQUİRED_FİELD_TEXT

        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        sleep(2)
        select_the_language_dropdown.click()
        select_german=self.waitForElementVisible(OPTİON_ALMANCA_XPATH).click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH).click()
        add_basic_level=self.waitForElementVisible(BASİC_LEVEL_XPATH).click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH).click()
        added=self.waitForElementVisible(ADDED_XPATH)
        assert added.text==ADDED_LANGUAGE_TEXT
        sleep(2)
        select_the_language_dropdown=self.waitForElementVisible(SELECT_THE_LANGUAGE_DROPDOWN)
        select_the_language_dropdown.click()
        select_german=self.waitForElementVisible(OPTİON_ALMANCA_XPATH).click()
        select_level=self.waitForElementVisible(SELECT_LEVEL_XPATH).click()
        add_basic_level=self.waitForElementVisible(BASİC_LEVEL_XPATH).click()
        save_button=self.waitForElementVisible(SAVE_BUTTON_XPATH).click()
        sleep(5)
        already_added=self.waitForElementVisible(ALREADY_ADDED_MESSAGE_XPATH)
        assert already_added.text==ALREADY_EXİSTS_LANGUAGE_TEXT

        find_german=self.waitForElementVisible(SELECTED_GERMAN_XPATH)
        delete=self.waitForElementVisible((By.XPATH, DELETE_XPATH))
        actions=ActionChains(self.driver)
        actions.move_to_element_with_offset(find_german, -14, 0).click().perform()


