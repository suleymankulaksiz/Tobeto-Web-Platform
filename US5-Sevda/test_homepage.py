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
from datetime import date

class Test_Homepage:
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
    
    
    def homepage_btn_click(self):
        homepage_nav_button=self.waitForElementVisible((By.XPATH, HOMEPAGE_NAV_XPATH))
        homepage_nav_button.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(2)
        
    #anasayfa'ya yönlendirme bildirimi kontrolü
    def test_successful_login(self): #tc1 done
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(email, tobeto_email)
        actions.send_keys_to_element(password, tobeto_password)
        actions.perform()
        # email.send_keys(tobeto_email)
        # password.send_keys(tobeto_password)
        loginBtn=self.waitForElementVisible((By.XPATH, LOGİNBUTTON_XPATH))
        loginBtn.click()
        sleep(2)
        successLogin=self.waitForElementVisible((By.XPATH, SUCCESSFUL_LOGİN_TEXT_XPATH))
        assert "• Giriş başarılı." in successLogin.text and self.driver.current_url == HOMEPAGE_URL
        
    
    def test_top_menu_navigate(self): #tc2 done
        self.test_successful_login()
        self.driver.save_screenshot(f"{self.folderPath}/selected_homepage.png")
        sleep(2)
        profile=self.waitForElementVisible((By.XPATH, PROFİLE_XPATH))
        profile.click()
        sleep(2)
        assessments=self.waitForElementVisible((By.XPATH,ASSESSMENTS_XPATH))
        assessments.click()
        catalog=self.waitForElementVisible((By.XPATH,CATALOG_XPATH))
        catalog.click()
        calendar=self.waitForElementVisible((By.XPATH, CALENDAR_XPATH))
        calendar.click()
        istanbul_kodluyor=self.waitForElementVisible((By.XPATH,İSTANBUL_K_XPATH))
        istanbul_kodluyor.click()
        assert{self.driver.current_url==PROFİLE_URL and 
               self.driver.current_url==ASSESSMENTS_URL and 
               self.driver.current_url==CATALOG_URL and 
               self.driver.current_url==CALENDAR_URL and 
               self.driver.current_url==İSTANBUL_K_URL}
    
    
    def test_welcome_and_ik(self): #tc3 done
        self.test_successful_login()
        sleep(2)
        welcometobeto = self.waitForElementVisible((By.XPATH, WELCOMETOBETO_XPATH))
        tobeto_slogan=self.waitForElementVisible((By.XPATH, TOBETO_SLOGAN_XPATH))
        istanbul_kodluyor_logo=self.waitForElementVisible((By.CSS_SELECTOR, İSTANBUL_KODLUYOR_LOGO_CSS_SELECTOR)) #logo görüntülenmesi için
        name=self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h4"))
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,300)")
        sleep(2)
        free_edu=self.waitForElementVisible((By.XPATH, FREE_EDUC_XPATH))
        aradığın_is_burada = self.waitForElementVisible((By.XPATH, ARADIGIN_İS_XPATH))

        assert {welcometobeto.text == "TOBETO'ya hoş geldin"  and #expectedı kaldır 
                name.text=="Sevda" and
                istanbul_kodluyor_logo.is_displayed(), "Logo görüntülenmiyor." and #eğer logo görüntülenmezse virgülden sonraki uyarıyı verecek.
                tobeto_slogan.text == TOBETO_SLOGAN_TEXT and 
                free_edu.text == FREE_EDUC_TEXT and
                aradığın_is_burada.text == ARADIGIN_İS_TEXT}
    
  
    def test_istanbul_is_coding_panel(self):#tc4 done
        self.test_successful_login()
        self.driver.execute_script("window.scrollTo(0,500)")
        apply_Btn=self.waitForElementVisible((By.ID, APPLY_ID))
        ariaSelected_Value=apply_Btn.get_attribute("aria-selected")
        sleep(2)
        myLessons=self.waitForElementVisible((By.ID, LESSONS_ID))
        myLessons.click()
        myLessonsContent=self.waitForElementVisible((By.ID, LESSONS_CONTENT_ID))
        sleep(2)
        notification=self.waitForElementVisible((By.ID, ANNOUNCEMENT_AND_NEWS_ID))
        no_read_announcements=self.waitForElementVisible((By.XPATH, NO_READ_ANNOUNCEMENT_XPATH))
        notification.click()
        sleep(2)
        notificationContent=self.waitForElementVisible((By.ID, ANNOUNCEMENT_AND_NEWS_CONTENT_ID))
        sleep(2)
        mySurveys=self.waitForElementVisible((By.ID, SURVEY_ID))
        mySurveys.click()
        sleep(2)
        mySurveysContent=self.waitForElementVisible((By.ID, SURVEY_CONTENT_ID))

        assert {ariaSelected_Value=="true" and
                myLessonsContent.is_displayed(), "Eğitimlerim içeriği görüntülenmiyor." and
                notificationContent.is_displayed(), "Duyurular ve Haberlerim görüntülenmiyor." and no_read_announcements.text=="1" and
                mySurveysContent.text==NO_SURVEY_TEXT

               }
    
    
    def test_my_educations(self): #TC5 done
        self.test_successful_login()
        self.driver.execute_script("window.scrollTo(0,700)")
        sleep(2)
        myLessons_btn=self.waitForElementVisible((By.ID, LESSONS_ID))
        myLessons_btn.click()
        shown_lessons=self.driver.find_elements(By.ID, ALL_LESSONS_ID)
        sleep(2)
        showMoreBtn=self.waitForElementVisible((By.XPATH, SHOWMORE_BTN_LESSONS_XPATH))
        showMoreBtn.click()  
        sleep(2)
        go_to_lesson_button=self.waitForElementVisible((By.XPATH, GOTO_LESSON_XPATH))  #herkes için kodlama-3a seçildi
        go_to_lesson_button.click()
        sleep(3)
        details=self.waitForElementVisible((By.XPATH, "//*[@id='dynamicContent']"))
        sleep(3)
        self.driver.save_screenshot(f"{self.folderPath}/details_lesson.png")
        assert {len(shown_lessons)<=4, "4'ten fazla ders görüntülendi." and
                self.driver.current_url==LESSONS_URL and
                details.text=="Herkes İçin Kodlama - 3A\nBaşardın"   #eğitime git butonuna tıkladıktan sonra açılan sayfada görmek istediğim içerik
                }
       
    def test_announcement_and_news(self): #Tc6 done
        self.test_successful_login()
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(2)
        announc_and_news_btn=self.waitForElementVisible((By.ID, ANNOUNCEMENT_AND_NEWS_ID))
        announc_and_news_btn.click()
        shown_announc_and_news=self.driver.find_elements(By.ID, ANNOUNCEMENT_AND_NEWS_CONTENT_ID)
        sleep(2)
        show_more_button=self.waitForElementVisible((By.XPATH, SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH))
        sleep(2)
        show_more_button.click()  
        sleep(2)
        read_more_button=self.waitForElementVisible((By.XPATH, READ_MORE_BUTTON_XPATH))
        read_more_button.click()
        sleep(2)
        about_clickBtn=self.waitForElementVisible((By.XPATH, "/html/body/div[4]/div/div/div[2]"))

        assert { len(shown_announc_and_news)<=3, "3'ten fazla ders görüntülendi." and
                 self.driver.current_url=="https://tobeto.com/duyurular"
               }
    
    def test_my_exams(self): #tc7 done
        self.test_successful_login()
        self.driver.execute_script("window.scrollTo(0,500)")
        exams=self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/span"))
        assert exams.text=="Sınavlarım"
        exams_content=self.waitForElementVisible((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[3]/div/div/div[2]/div"))
        assert exams_content.text=='Herkes İçin Kodlama 3A Değerlendirme Sınavı\nHerkes İçin Kodlama - 3A\n45 Dakika'
        sleep(2)
        exam_Btn=self.waitForElementVisible((By.XPATH, "//div[@id='__next']/div[@class='back-white']//div[@class='plaform-page']/section[3]//div[@class='exams my-3']/div"))       
        exam_Btn.click()
        exam_window=self.waitForElementVisible((By.XPATH, "/html/body/div[4]/div/div"))
        assert exam_window.is_displayed(), "Sınava ait detaylar görüntülenmedi"
        view_the_report_Btn=self.waitForElementVisible((By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[2]/button"))
        view_the_report_Btn.click()
        report_popup=self.waitForElementVisible((By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[1]"))
        assert report_popup.text== 'Doğru\nYanlış\nBoş\n0\nPuan'  #niye 0 var?


        


   
    def test_bottom_ofthe_homepage(self):  #tc8
        self.test_successful_login()
        self.driver.execute_script("window.scrollTo(0,1000)")
        sleep(2)
        areaContol=self.waitForElementVisible((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[4]/div/div"))
        areaContol.text=='Profilini oluştur\nBaşla\n\nKendini değerlendir\nBaşla\n\nÖğrenmeye başla\nBaşla'
        cr_profile_btn=self.waitForElementVisible((By.XPATH, CR_PROFİLE_BUTTON_XPATH))
        cr_profile_btn.click()
        sleep(2)
        #expected_url=PROFİLE_INFO_URL
        self.homePage_btn_click()
        self.driver.execute_script("window.scrollTo(0,1000)")
        imp_yourself_btn=self.waitForElementVisible((By.XPATH,IMP_YOURSELF_BTN_XPATH ))
        imp_yourself_btn.click()
        sleep(2)
        self.homePage_btn_click()
        sleep(2)
        start_to_learn_btn=self.waitForElementVisible((By.XPATH, START_TO_LEARN_BTN_XPATH))
        start_to_learn_btn.click()
        
        assert {areaContol.text=='Profilini oluştur\nBaşla\n\nKendini değerlendir\nBaşla\n\nÖğrenmeye başla\nBaşla' and
                self.driver.current_url==PROFİLE_INFO_URL and
                self.driver.current_url==IMP_YOURSELF_URL and
                self.driver.current_url==LESSONS_URL, f"{LESSONS_URL} değil https://tobeto.com/platform-egitimler adresi geliyor"  #fail done
        }
      





