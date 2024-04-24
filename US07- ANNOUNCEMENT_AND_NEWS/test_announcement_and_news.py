from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep,time
from constants.globalConstants import *
from pathlib import Path
from datetime import datetime



class Test_Announcement_And_News:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        #valid login
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        email.send_keys(tobeto_email)
        password.send_keys(tobeto_password)
        loginBtn=self.waitForElementVisible((By.XPATH, LOGİNBUTTON_XPATH))
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        announc_and_news_btn=self.waitForElementVisible((By.ID, ANNOUNCEMENT_AND_NEWS_ID))
        announc_and_news_btn.click()
        sleep(2)
        show_more_btn=self.waitForElementVisible((By.XPATH,SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH))
        sleep(2)
        show_more_btn.click()  
        sleep(2)
        existing_folder_path= "US07- ANNOUNCEMENT_AND_NEWS/screenshots"
        self.folderPath= existing_folder_path#str("screenshots") 
        Path(self.folderPath).mkdir(parents=True, exist_ok=True) #klasörü oluşturmak için ve o klasördeki veriyi korumak için
        yield
        self.driver.quit()
     


    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    
    def test_filter_search_by_headings(self): 
        shown_announce_a_news=self.driver.find_elements(By.XPATH, SHOWN_ANNOUNCEMENT_AND_NEWS_XPATH)
        search_steps = [
            (By.ID, 'search', 's'),
            (By.ID, 'search', 'ı'),
            (By.ID, 'search', 'nav')
        ]

        for locator, element_id, key in search_steps:
            search_element = self.waitForElementVisible((locator, element_id), timeout=10)
            search_element.click()
            search_element.send_keys(key)
            self.driver.save_screenshot(f"{self.folderPath}/filter_search_with_{key}.png")
        
        search_element.clear()
        search_element.send_keys("q")
        type_news_page=self.waitForElementVisible((By.XPATH, TYPE_NEWS_PAGE_XPATH))
       
        assert {len(shown_announce_a_news)<=9 , "9'dan daha fazla duyuru ve haber var" and
                type_news_page.text== 'Bir duyuru bulunmamaktadır.'
                }
        

    def test_filter_by_type(self): 
        dropdown_button_type=self.waitForElementVisible((By.XPATH, DROPDOWN_BUTTON_TYPE_XPATH)) 
        dropdown_button_type.click()
        type_news_checkbox=self.waitForElementVisible((By.ID, TYPE_NEWS_CHECKBOX_ID))
        type_news_checkbox.click()
        type_news_page=self.waitForElementVisible((By.XPATH, TYPE_NEWS_PAGE_XPATH))
        type_news_checkbox=self.waitForElementVisible((By.ID, TYPE_NEWS_CHECKBOX_ID))
        type_news_checkbox.click()
        type_announcement_checkBox=self.waitForElementVisible((By.ID, TYPE_ANNOUNCEMENT_CHECKBOX_ID))
        type_announcement_checkBox.click()
        shown_announcements_page=self.driver.find_elements(By.XPATH, SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH)
        assert {type_news_page.text== NO_ANNOUNCEMENT_TEXT and
                len(shown_announcements_page)>0, NO_ANNOUNCEMENT_TEXT
                }
        

    def test_filter_of_organization(self): 
        organization_dropdown=self.waitForElementVisible((By.XPATH,ORGANİZATİON_DROPDOWN_XPATH))
        organization_dropdown.click()
        istanbul_code_listbox=self.waitForElementVisible((By.ID, iSTANBUL_CODDİNG_ID))
        istanbul_code_listbox.click()
        organization_dropdown=self.waitForElementVisible((By.XPATH,ORGANİZATİON_DROPDOWN_XPATH))
        organization_dropdown.click()
        self.driver.save_screenshot(f"{self.folderPath}/there_is_no_organization.png")
        sleep(2)
        x_button=self.waitForElementVisible((By.CLASS_NAME, X_BUTTON_CLASSNAME))
        x_button.click()
        sleep(2)
        organization_dropdown1=self.waitForElementVisible((By.XPATH, ORGANİZATİON_DROPDOWN_INPUT_XPATH))
        organization_dropdown1.send_keys("L")
        assert True
      
        
    def test_filter_by_date(self): 
        sorting_elements = self.waitForElementVisible((By.XPATH, SORTİNG_BUTTON_XPATH))
        sorting_elements.click()
        Y_E= self.waitForElementVisible((By.XPATH, DROPDOWN_Y_E_XPATH))
        Y_E.click()
      
        dates_class= self.driver.find_elements(By.CLASS_NAME, "date")
        sleep(5)
        date_list= []
        for dateelement in dates_class:
            date_texts= dateelement.text
            date_list.append(date_texts)
        #tarih_listesi artık tarihleri icinde tutan bir liste.
        date_objects= [datetime.strptime(date, "%d.%m.%Y") for date in date_list]
        ordered_dates = sorted(date_objects, reverse= True)
        ordered_dates_str = [date.strftime("%d.%m.%Y") for date in ordered_dates]
        self.driver.save_screenshot(f"{self.folderPath}/filter_new_to_old.png")
    
        sorting_elements = self.waitForElementVisible((By.XPATH, SORTİNG_BUTTON_XPATH))
        sorting_elements.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        sleep(2)
        E_Y = self.waitForElementVisible((By.XPATH, DROPDOWN_E_Y_XPATH))
        E_Y.click()
        sleep(2)
       
        dates_class= self.driver.find_elements(By.CLASS_NAME, "date")
        sleep(5)
        date_list= []
        for dateelement in dates_class:
            date_texts= dateelement.text
            date_list.append(date_texts)
        #tarih_listesi artık tarihleri icinde tutan bir liste.
        date_objects= [datetime.strptime(date, "%d.%m.%Y") for date in date_list]
        ordered_dates = sorted(date_objects, reverse= True)
        ordered_dates_str = [date.strftime("%d.%m.%Y") for date in ordered_dates]
        self.driver.save_screenshot(f"{self.folderPath}/filter_old_to_new.png")

        assert{ordered_dates_str == date_list and ordered_dates_str == date_list }

    
    
    def test_filder_hide_and_show(self): 
        no_read = self.driver.find_elements(By.XPATH, NO_READ_XPATH)
        found_button = False
        for i in no_read:
         read_more_button = i.find_elements(By.XPATH, READ_MORE_BUTON_XPATH)
         if read_more_button:
            # js ile tıklama işlemi
            self.driver.execute_script("arguments[0].click();", read_more_button[0]) 
            found_button = True
            break
        if not found_button:
         print("Devamını Oku butonu bulunamadı.")
        close_X=self.waitForElementVisible((By.XPATH, CLOSE_X_XPATH))
        close_X.click()
        self.driver.save_screenshot(f"{self.folderPath}/read_hide_before.png")
        read_hide=self.waitForElementVisible((By.XPATH,READ_MORE_BUTTON_XPATH))
        read_hide.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/read_hide_after.png")
        assert False

             


    def test_filter_synchronous_working(self): 
        search=self.waitForElementVisible((By.ID, SEARCH_ID))
        search.click()
        search.send_keys("sınav")                               
        dropdown_button_type=self.waitForElementVisible((By.XPATH, DROPDOWN_BUTTON_TYPE_XPATH)) 
        dropdown_button_type.click()
        sleep(2)
        type_announcement_checkBox=self.waitForElementVisible((By.ID, TYPE_ANNOUNCEMENT_CHECKBOX_ID))
        type_announcement_checkBox.click()
        organization_dropdown=self.waitForElementVisible((By.XPATH, ORGANİZATİON_DROPDOWN_XPATH))
        organization_dropdown.click()
        istanbul_code_listbox=self.waitForElementVisible((By.ID, iSTANBUL_CODDİNG_ID))
        istanbul_code_listbox.click()
        sorting_btn=self.waitForElementVisible((By.XPATH, SORTİNG_BUTTON_XPATH))
        sorting_btn.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        sleep(2)
        E_Y = self.waitForElementVisible((By.XPATH, DROPDOWN_E_Y_XPATH))
        E_Y.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/filter_synchronous_working.png")
        assert True
   