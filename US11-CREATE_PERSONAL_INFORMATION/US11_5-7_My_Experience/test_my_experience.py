import json
from time import sleep
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


#Deneyimlerim TC 5-7
class Test_my_personal_information:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()


    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    
    
    def precondition(self):
        #Login
        login_email = self.waitForElementVisible((By.XPATH,LOGIN_MAIL_XPATH))
        login_email.send_keys(input_personal_mail)
        login_password = self.waitForElementVisible((By.XPATH,LOGIN_PASSWORD_XPATH))
        login_password.send_keys(input_personal_password)
        login_button = self.waitForElementVisible((By.XPATH,LOGIN_BUTTON_XPATH))
        login_button.click()
        # popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        # assert popupMessage.text == POPUP_MESSAGE_TEXT
        popupMessage = self.waitForElementVisible((By.XPATH,LOGIN_POPUP_XPATH))
        assert popupMessage.text == POPUP_MESSAGE_TEXT

        alert_quit = self.waitForElementVisible((By.XPATH, LOGIN_POPUP_ALERTQUIT_XPATH))
        alert_quit.click()
        
        #Profilimi oluştur
        profileTitleText=self.waitForElementVisible((By.XPATH,PROFILETITLE_TEXT_XPATH))
        assert profileTitleText.text == PROFILETITLETEXT
        profileButton=self.waitForElementVisible((By.XPATH,PROFILEBUTTON_XPATH))
        profileButton = self.waitForElementVisible((By.XPATH, PROFILEBUTTON_XPATH))
        self.scroll()
        profileButton.click()
        #Deneyimler bölümüne gidilir
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        experienceButton  = self.waitForElementVisible((By.XPATH,EXPERIENCEBUTTON_XPATH))
        experienceButton.click()
    
    def job_start_end_date2(self):
        job_start_date = self.waitForElementVisible((By.XPATH,JOBSTARTDATE_XPATH))
        job_start_date.send_keys(job_start_date_input)

        dropdown_element_date = self.waitForElementVisible((By.XPATH, DROPDOWNELEMENTDATE_XPATH))
        dropdown_element_date.click()
        #İş bitiş takviminden ay seçilir
        dropdown_element_date_month = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWNELEMENTDATEMONTH_XPATH))
        )
        dropdown = Select(dropdown_element_date_month)
        # indekse göre seçim yapın
        dropdown.select_by_index(4)
        select_day = self.waitForElementVisible((By.XPATH, SELECTDAY_XPATH))
        select_day.click()
        sleep(2)

    def test_job_start_end_date(self):
        self.precondition()
        #İş başlangıç ve bitiş tarihleri seçilir
        job_start_date = self.waitForElementVisible((By.XPATH,JOBSTARTDATE_XPATH))
        job_start_date.send_keys(job_start_date_input)

        dropdown_element_date = self.waitForElementVisible((By.XPATH, DROPDOWNELEMENTDATE_XPATH))
        dropdown_element_date.click()
        #İş bitiş takviminden ay seçilir
        dropdown_element_date_month = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWNELEMENTDATEMONTH_XPATH))
        )
        dropdown = Select(dropdown_element_date_month)
        # indekse göre seçim yapın
        dropdown.select_by_index(4)
        select_day = self.waitForElementVisible((By.XPATH, SELECTDAY_XPATH))
        select_day.click()
        sleep(2)
 

    #TC 5
    def test_adding_experience(self):
        self.precondition()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)

        input_organization_name = self.waitForElementVisible((By.XPATH,INPUTORGANIZATIONNAME_XPATH))
        input_organization_name.send_keys(input_organization_name_text)

        position_name = self.waitForElementVisible((By.XPATH,POSITIONNAMEXPATH_XPATH))
        position_name.send_keys(position_name_text)

        sector_name = self.waitForElementVisible((By.XPATH,SECTORNAME_XPATH))
        sector_name.send_keys(sector_name_text)

        #Şehir seçilir
        dropdown_element_city = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWNELEMENTCITY_XPATH))
        )
        dropdown = Select(dropdown_element_city)
        # indekse göre seçim yapın
        dropdown.select_by_index(40)
        sleep(2)
        #İş başlangıç ve bitiş tarihleri seçilir
        self.job_start_end_date2()
        
        # Onay kutusu tıklanma durumu kontrolü
        experience_checkbox = self.driver.find_element(By.XPATH, EXPERIENCECHECKBOX_XPATH)
        assert experience_checkbox.is_selected() == False

        #İş açıklaması
        job_description = self.waitForElementVisible((By.XPATH,JOBDESCRIPTION_XPATH))
        job_description.send_keys(job_description_text)

        #Kaydet butonu
        experience_save_button = self.waitForElementVisible((By.XPATH,EXPERIENCESAVEBUTTON_XPATH))
        experience_save_button.click()

        sleep(3)
    #TC 6
    def test_fields_left_empty(self):
        self.precondition()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)
        sleep(3)

        #Kurum girişi yapılır
        input_organization_name = self.waitForElementVisible((By.XPATH,INPUTORGANIZATIONNAME_XPATH))
        input_organization_name.send_keys(input_organization_name_text)

        position_name = self.waitForElementVisible((By.XPATH,POSITIONNAMEXPATH_XPATH))
        position_name.send_keys(position_name_text)
        

        #Şehir seçilir "İstanbul"
        dropdown_element_city = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, DROPDOWNELEMENTCITY_XPATH))
        )
        dropdown = Select(dropdown_element_city)
        # indekse göre seçim yapın
        dropdown.select_by_index(40)

        #İş başlangıç ve bitiş tarihleri seçilir
        self.job_start_end_date2()

        #İş açıklaması
        job_description = self.waitForElementVisible((By.XPATH,JOBDESCRIPTION_XPATH))
        job_description.send_keys(job_description_name_text)

        #Kaydet butonu
        experience_save_button = self.waitForElementVisible((By.XPATH,EXPERIENCESAVEBUTTON_XPATH))
        experience_save_button.click()

        input_organization_name_alert = self.waitForElementVisible((By.XPATH,input_organization_name_alert_XPATH))
        position_name_name_alert = self.waitForElementVisible((By.XPATH,position_name_name_alert_XPATH))
        sector_name_name_alert = self.waitForElementVisible((By.XPATH,sector_name_name_alert_XPATH))
        job_description_name_alert = self.waitForElementVisible((By.XPATH,job_description_name_alert_XPATH))

        
        assert {
            input_organization_name_alert.text == MAXCHARACTER_ORGANIZATION_ALERT and position_name_name_alert.text == MINCHARACTERS_POSITION_ALERT and
            sector_name_name_alert.text == EMPTY_ALERT_ALERT and job_description_name_alert.text == MINCHARACTERS_DESCRIPTION_ALERT
        }
        sleep(3)
    
    #TC 7
    def test_color_marker(self):
        
        self.precondition()

        #Görüntüleme işlemi için ekran görüntüsü alınır
        self.driver.save_screenshot(SAVE_SCREENSHOT_PATH)

        input_organization_name = self.waitForElementVisible((By.XPATH,INPUTORGANIZATIONNAME_XPATH))
        input_organization_name.send_keys(input_organization_name_text)

        position_name = self.waitForElementVisible((By.XPATH,POSITIONNAMEXPATH_XPATH))
        position_name.send_keys(position_name_text)

        sector_name = self.waitForElementVisible((By.XPATH,SECTORNAME_XPATH))
        sector_name.send_keys(sector_name_text)

        #İş başlangıç ve bitiş tarihleri seçilir
        self.job_start_end_date2()
        
        #İş açıklaması
        job_description = self.waitForElementVisible((By.XPATH,JOBDESCRIPTION_XPATH))
        job_description.send_keys(job_description_text)
        
        #Kaydet butonu
        experience_save_button = self.waitForElementVisible((By.XPATH,EXPERIENCESAVEBUTTON_XPATH))
        experience_save_button.click()

        city_border_color_view = self.waitForElementVisible((By.CSS_SELECTOR, city_border_color_view_CSS))

        # Uyarı rengini kontrol edilir
        city_border_color = city_border_color_view.value_of_css_property("border-color")
        assert city_border_color == city_border_color_text

        assert False,CITYFALSEASSERT_TEXT




