from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep
from constantss.globalConstants import *
from pathlib import Path
from datetime import date, datetime






class Test_Announcement_And_News:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                
        self.driver.get(LOGIN_URL)
        
        self.folderPath= str("screenshots") #==>12.04.2024
        Path(self.folderPath).mkdir(exist_ok=True) #klasörü oluşturmak için ve o klasördeki veriyi korumak için

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    

    def environment(self): #tc1 done
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        email.send_keys(tobeto_email)
        password.send_keys(tobeto_password)
        loginBtn=self.waitForElementVisible((By.XPATH, LOGİNBUTTON_XPATH))
        loginBtn.click()
        sleep(5)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        announc_and_news_btn=self.waitForElementVisible((By.ID, ANNOUNCEMENT_AND_NEWS_ID))
        announc_and_news_btn.click()
        show_more_btn=self.waitForElementVisible((By.XPATH,SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH))
        sleep(2)
        show_more_btn.click()  
        sleep(2)
        # self.driver.execute_script("window.scrollTo(0,300)")
        # assert self.driver.current_url=="https://tobeto.com/duyurular"
        # sleep(3)


    
    def test_filter_search_by_headings(self): #tc1 harf harf filtreleme kısmı eklenecek
        self.environment()
        sleep(2)
        shown_announce_a_news=self.driver.find_elements(By.XPATH, SHOWN_ANNOUNCEMENT_AND_NEWS_XPATH)
        assert len(shown_announce_a_news)<=9 , "9'dan daha fazla duyuru ve haber var"
        search=self.waitForElementVisible((By.ID, "search"))
        search.click()
        search.send_keys("s")
        self.driver.save_screenshot(f"{self.folderPath}/filter_search_with_s.png")
        search=self.waitForElementVisible((By.ID, "search"))
        search.click()
        search.send_keys("ı")
        self.driver.save_screenshot(f"{self.folderPath}/filter_search_with_sı.png")
        search=self.waitForElementVisible((By.ID, "search"))
        search.click()
        search.send_keys("nav")
        self.driver.save_screenshot(f"{self.folderPath}/filter_search_with_sınav.png")
        search.clear()
        search=self.waitForElementVisible((By.ID, "search"))
        search.click()
        search.send_keys("q")
        type_news_page=self.waitForElementVisible((By.XPATH, TYPE_NEWS_PAGE_XPATH))
        assert type_news_page.text== NO_ANNOUNCEMENT_TEXT
    

    def test_filter_by_type(self): #tc2 done
        self.environment()
        dropdown_button_type=self.waitForElementVisible((By.XPATH, DROPDOWN_BUTTON_TYPE_XPATH)) 
        dropdown_button_type.click()
        sleep(3)
        type_news_checkbox=self.waitForElementVisible((By.ID, TYPE_NEWS_CHECKBOX_ID))
        type_news_checkbox.click()
        type_news_page=self.waitForElementVisible((By.XPATH, TYPE_NEWS_PAGE_XPATH))
        assert type_news_page.text== "Bir duyuru bulunmamaktadır."
        type_news_checkbox=self.waitForElementVisible((By.ID, TYPE_NEWS_CHECKBOX_ID))
        type_news_checkbox.click()
        sleep(2)
        type_announcement_checkBox=self.waitForElementVisible((By.ID, TYPE_ANNOUNCEMENT_CHECKBOX_ID))
        type_announcement_checkBox.click()
        shown_announcements_page=self.driver.find_elements(By.XPATH, SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH)
        assert len(shown_announcements_page)>0, "Bir duyuru bulunmamaktadır"
        # if shown_announcements:
        #     print("Duyurular:")
        #     for duyurular in shown_announcements:
        #         print(duyurular.text)
        #     else:
        #         print("Bir duyuru bulunmamaktadır.")

    def test_filter_of_organization(self): #tc3 organizasyona harf girişi tekrar dene
        self.environment()
        organization_dropdown=self.waitForElementVisible((By.XPATH,ORGANİZATİON_DROPDOWN_XPATH))
        organization_dropdown.click()
        istanbul_code_listbox=self.waitForElementVisible((By.XPATH, iSTANBUL_CODE__LİSTBOX_XPATH))
        istanbul_code_listbox.click()
        sleep(2)
        x_button=self.waitForElementVisible((By.CLASS_NAME, X_BUTTON_CLASSNAME))
        x_button.click()
        sleep(2)
        organizationDropdown1=self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]"))
        organizationDropdown1.click()
        #organizationDropdown1.send_keys("L") niye çalışmıyooooo???
        
    def test_filter_by_date(self): #tc4 bitmedi
        self.environment()
        sorting_btn=self.waitForElementVisible((By.XPATH, SORTİNG_BUTTON_XPATH))
        sorting_btn.click()
        dropdown_Y_E=self.waitForElementVisible((By.XPATH, DROPDOWN_Y_E_XPATH))
        dropdown_Y_E.click()
        sleep(3)
        sorting_btn=self.waitForElementVisible((By.XPATH, SORTİNG_BUTTON_XPATH))
        sorting_btn.click()   
        sleep(2)
        #self.driver.find_element(By.CSS_SELECTOR, ".show:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "Tarihe Göre (E-Y)").click()
        sleep(2)
        dates=self.driver.find_elements(By.CLASS_NAME, "date")
        
    def test_filder_hide_and_show(self): #tc5
        self.environment()
        #no_read=self.driver.find_elements(By.CSS_SELECTOR, "div[style='background-color: rgb(237, 237, 237);']")
        no_read=self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[2]/div"))
        read_more_buttons=self.driver.find_element(By.XPATH, READ_MORE_BUTTON_XPATH)
        read_more_buttons.click()
        close_X=self.waitForElementVisible((By.XPATH, "/html/body/div[3]/div/div/div[1]/button"))
        close_X.click()
        self.driver.save_screenshot(f"{self.folderPath}/read_hide_before.png")
        read_hide=self.waitForElementVisible((By.XPATH,"//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[2]/button"))
        read_hide.click()
        self.driver.save_screenshot(f"{self.folderPath}/read_hide_after.png")
        #fail

             


    def test_filter_synchronous_working(self): #tc6 bitmedi
        self.environment() 
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
        dropdown_E_Y=self.driver.find_element(By.XPATH, DROPDOWN_E_Y_XPATH)
        dropdown_E_Y.click()
   