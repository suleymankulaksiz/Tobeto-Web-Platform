import random
import string


#-------------------------------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
#-------------------------------------------
FIRSTNAME_NAME = "firstName"
LASTNAME_NAME = "lastName"
EMAIL_NAME ="email"                        #  BUNLAR KAYIT OL AŞAMASINDAKİ FORMUN LOCATORLARI
PASSWORD_NAME ="password"
PASSWORDAGAIN_NAME= "passwordAgain"
#-------------------------------------------
input_firstname ="Can"
input_lastname ="Canan"
input_email ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXtobeto@hotmail.com"          #BURADA KAYIT OL AŞAMASINDA FORM VERİLERİ VAR.
input_password ="123456"
input_passwordagain="123456"
#------------------------------------------
SIGNUPBUTTON_XPATH ="//*[@id='__next']/div/main/section/div/div/div[1]/div/div/button"    #-KAYIT OL AŞAMASINDAKİ BUTON
#------------------------------------------
CHECKBOX1_XPATH = "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='contact']"
CHECKBOX2_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='membershipContrat']"
CHECKBOX3_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='emailConfirmation']"
CHECKBOX4_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//input[@name='phoneConfirmation']"
#------------------------------------------
PHONECHECK = "/html//input[@id='phoneNumber']"
input_phone ="549 490 30 04"
#------------------------------------------
CONTINUEBUTTON_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"
#------------------------------------------
REGISTERTEXT_XPATH = "/html/body/div[1]/div/main/section/div/div/div/div/span"

TRUEREGISTER_TEXT="Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."







#sevda
from selenium.webdriver.common.by import By


LOGIN_URL = "https://tobeto.com/giris"
HOMEPAGE_URL="https://tobeto.com/platform"
PROFİLE_URL="https://tobeto.com/profilim"
ASSESSMENTS_URL="https://tobeto.com/degerlendirmeler"
CATALOG_URL="https://tobeto.com/platform-katalog"
CALENDAR_URL="https://tobeto.com/takvim"
İSTANBUL_K_URL="https://tobeto.com/istanbul-kodluyor"
PROFİLE_INFO_URL="https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
IMP_YOURSELF_URL= "https://tobeto.com/degerlendirmeler"
LESSONS_URL= "https://tobeto.com/egitimlerim"

#-------------------------------------INPUT
tobeto_email="sevdayilmazf@gmail.com"
tobeto_password="34325Sevo."
#-----------------------NAME
EMAIL_NAME ="email"                        
PASSWORD_NAME ="password"

#----------------XPATH
LOGİNBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
SUCCESSFUL_LOGİN_TEXT_XPATH= "//div[@id=\'__next\']/div/div[2]/div/div[2]"
HOMEPAGE_NAV_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[1]/a"
PROFİLE_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[2]/a"
ASSESSMENTS_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"
CATALOG_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[4]/a"
CALENDAR_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[5]/a"
İSTANBUL_K_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[6]/a"
NAME_XPATH= "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h4"  #kayıt olurken yazan isim
WELCOMETOBETO_XPATH = "/html/body/div[1]/div/main/div[1]/section[1]/div/div[2]/div/h3"
TOBETO_SLOGAN_XPATH = "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/p"
İK_LOGO_XPATH = "//*[@id='__next']/div/main/div[1]/section[2]/div/div/div[1]/div[1]/span/img"
FREE_EDUC_XPATH = "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[1]/div[2]/span[1]"
ARADIGIN_İS_XPATH = "//*[@id='__next']/div/main/div[1]/section[2]/div/div/div[1]/div[2]/span[2]"
CR_PROFİLE_BUTTON_XPATH = "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[1]/div/button"
IMP_YOURSELF_BTN_XPATH= "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[2]/div/button"
START_TO_LEARN_BTN_XPATH="//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[3]/div/button"
NO_SURVEY_XPATH="//*[@id='mySurvey-tab-pane']/div/div/p"
SHOWMORE_BTN_LESSONS_XPATH= "//*[@id='lessons-tab-pane']/div/div/div[2]"
GOTO_LESSON_XPATH= "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/a"
İCERİK_XPATH="//*[@id='rc-tabs-0-tab-content']/div/span"
NO_READ_ANNOUNCEMENT_XPATH="//*[@id='myTab']/li[3]/div/span"
SHOWMORE_BTN_ANNOUNCEMENT_AND_NEWS_XPATH="/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[3]/div/div[3]/div/div[4]"
SHOWN_ANNOUNCEMENT_AND_NEWS_XPATH= "//*[@id='__next']/div/main/div[2]/div[2]"
TYPE_NEWS_PAGE_XPATH="//*[@id='__next']/div/main/div[2]/div[2]/div/p"
DROPDOWN_BUTTON_TYPE_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]"
ORGANİZATİON_DROPDOWN_XPATH= "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div[1]"
iSTANBUL_CODE__LİSTBOX_XPATH="/html//div[@id='exaironWebchat']//div[@class='exw-widget-container']/div"
SORTİNG_BUTTON_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/button"
DROPDOWN_Y_E_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[1]/a"
DROPDOWN_E_Y_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[2]/a"
READ_MORE_BUTTON_XPATH="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[2]"
#----------------text
SUCCESSFUL_LOGİN_TEXT="• Giriş başarılı."
TOBETO_SLOGAN_TEXT="Yeni nesil öğrenme deneyimi ile Tobeto kariyer yolculuğunda senin yanında!"
FREE_EDUC_TEXT= "Ücretsiz eğitimlerle, geleceğin mesleklerinde sen de yerini al."
ARADIGIN_İS_TEXT = "Aradığın  “İş”  Burada!"
#MEMBER_NAME_TEXT="Sevda"
WELCOMETOBETO_TEXT= "TOBETO'ya hoş geldin"
NO_SURVEY_TEXT="Atanmış herhangi bir anketiniz bulunmamaktadır"
NO_ANNOUNCEMENT_TEXT="Bir duyuru bulunmamaktadır."






#--------------ID
APPLY_ID = "apply-tab"
LESSONS_ID = "lessons-tab"  #daha fazla gösteri kapsıyor
ANNOUNCEMENT_AND_NEWS_ID = "notification-tab"
SURVEY_ID = "mySurvey-tab"
APPLY_CONTENT_ID = "apply-tab-pane"
LESSONS_CONTENT_ID = "lessons-tab-pane"
ALL_LESSONS_ID="all-lessons-tab-pane"
ANNOUNCEMENT_AND_NEWS_CONTENT_ID= "notification-tab-pane"
SURVEY_CONTENT_ID="mySurvey-tab-pane"  
TYPE_NEWS_CHECKBOX_ID="typeNews"
TYPE_ANNOUNCEMENT_CHECKBOX_ID="typeAnnouncement"
SEARCH_ID="search"
iSTANBUL_CODDİNG_ID="react-select-2-listbox"
#------------CSS SELECTOR
İSTANBUL_KODLUYOR_LOGO_CSS_SELECTOR= ".p-4 > span > img"

#-----------CLASS NAME
X_BUTTON_CLASSNAME="css-8mmkcg"


#YABANCI DİL:

RİGHT_NAME_DROPDOWN_XPATH= (By.XPATH, "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]" )
DROPDOWN_PROFİLE_INFO_CLASS_NAME= (By.CLASS_NAME, "dropdown-item")
MY_LANGUAGE_SİDEBAR_XPATH=(By.XPATH, "//*[contains(text(),'Yabancı Dillerim')]")
SELECT_THE_LANGUAGE_DROPDOWN_XPATH= (By.XPATH, "//*[contains(text(), 'Dil Seçiniz')]")
SELECT_LEVEL_XPATH=(By.XPATH, "//*[contains(text(), 'Seviye Seçiniz')]")
OPTİON_ALMANCA_XPATH=(By.XPATH, "//*[contains(text(), 'Almanca')]")
OPTİON_CEKCE_XPATH=(By.XPATH, "//*[contains(text(), 'Çekçe')]")
OPTİON_CİNCE_XPATH=(By.XPATH, "//*[contains(text(), 'Çince (Mandarin)')]")
OPTİON_NORVECCE_XPATH=(By.XPATH, "//*[contains(text(), 'Norveççe')]")
OPTİON_ENGLİSH_XPATH=(By.XPATH, "//*[contains(text(), 'İngilizce')]")
BASİC_LEVEL_XPATH=(By.XPATH, "//*[contains(text(), 'Temel Seviye ( A1 , A2)')]")
INTERMEDİATE_LEVEL_XPATH=(By.XPATH, "//*[contains(text(), 'Orta Seviye (B1 , B2)')]")
ADVANCED_LEVEL_XPATH=(By.XPATH, "//*[contains(text(), 'İleri Seviye (C1 , C2)')]")
MOTHER_LANGUAGE_LEVEL_XPATH= (By.XPATH, "//*[contains(text(), 'Anadil')]")
SELECTED_NORVEGİAN="//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]"
SELECTED_GERMAN_XPATH=(By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")

SAVE_BUTTON_XPATH=(By.XPATH, "//*[contains(text(), 'Kaydet')]")
ANSWER_YES_XPATH=(By.XPATH, "//*[contains(text(), 'Evet')]")

SELECTED_LANGUAGES_XPATH= "//*[@id='__next']/div/main/section/div/div/div[2]/div/div"
LANGUAGE_REQUİRED_FİELD_XPATH= (By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/p")
LEVEL_REQUİRED_FİELD_XPATH=(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/p")


ADDED_XPATH=(By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
REMOVED_MESSAGE_XPATH=(By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
ALREADY_ADDED_MESSAGE_XPATH=(By.XPATH, "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']")
GO_TO_LANGUAGE_XPATH=(By.XPATH,"/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]")
DELETE_ELEMENT_XPATH=(By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[2]/div/div/div[1]/span[2]")

REQUİRED_FİELD_TEXT= "Doldurulması zorunlu alan*"
ADDED_LANGUAGE_TEXT="• Yabancı dil bilgisi eklendi."
LANGUAGE_REMOVED_TEXT="• Yabancı dil kaldırıldı."
ALREADY_EXİSTS_LANGUAGE_TEXT="• Bu dil zaten mevcut."


























