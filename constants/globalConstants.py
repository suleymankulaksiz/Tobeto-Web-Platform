import random
import string


#-------------------------------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
#-------------------------
EMAIL_NAME ="email"                        #  BUNLAR KAYIT OL AŞAMASINDAKİ FORMUN LOCATORLARI
PASSWORD_NAME ="password"



#SEVDA
LOGIN_URL = "https://tobeto.com/giris"
HOMEPAGE_URL="https://tobeto.com/platform"
PROFILE_URL="https://tobeto.com/profilim"
ASSESSMENTS_URL="https://tobeto.com/degerlendirmeler"
CATALOG_URL="https://tobeto.com/platform-katalog"
CALENDAR_URL="https://tobeto.com/takvim"
ISTANBUL_K_URL="https://tobeto.com/istanbul-kodluyor"
PROFILE_INFO_URL="https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
IMP_YOURSELF_URL= "https://tobeto.com/degerlendirmeler"
LESSONS_URL= "https://tobeto.com/egitimlerim"
ANNOUNCEMENTS_URL="https://tobeto.com/duyurular"

#-------------------------------------INPUT
tobeto_email="sevdayilmazf@gmail.com"
tobeto_password="34325Keys."
#-----------------------NAME
EMAIL_NAME ="email"                        
PASSWORD_NAME ="password"

#----------------XPATH
LOGINBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
SUCCESSFUL_LOGIN_TEXT_XPATH= "//div[@id=\'__next\']/div/div[2]/div/div[2]"
HOMEPAGE_NAV_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[1]/a"
PROFILE_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[2]/a"
ASSESSMENTS_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[3]/a"
CATALOG_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[4]/a"
CALENDAR_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[5]/a"
ISTANBUL_K_XPATH="//*[@id='__next']/div/nav/div[1]/ul/li[6]/a"
NAME_XPATH= "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/h4"  #kayıt olurken yazan isim
WELCOMETOBETO_XPATH = "/html/body/div[1]/div/main/div[1]/section[1]/div/div[2]/div/h3"
TOBETO_SLOGAN_XPATH = "//*[@id='__next']/div/main/div[1]/section[1]/div/div[2]/div/p"
IK_LOGO_XPATH = "//*[@id='__next']/div/main/div[1]/section[2]/div/div/div[1]/div[1]/span/img"
FREE_EDUC_XPATH = "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[1]/div[2]/span[1]"
ARADIGIN_IS_XPATH = "//*[@id='__next']/div/main/div[1]/section[2]/div/div/div[1]/div[2]/span[2]"
CR_PROFILE_BUTTON_XPATH = "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[1]/div/button"
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
ORGANIZATION_DROPDOWN_XPATH= "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div[1]"
ORGANIZATION_DROPDOWN_INPUT_XPATH="//*[@id='react-select-2-input']"
ISTANBUL_CODE__LISTBOX_XPATH="/html//div[@id='exaironWebchat']//div[@class='exw-widget-container']/div"
SORTING_BUTTON_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/button"
DROPDOWN_Y_E_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[1]/a"
DROPDOWN_E_Y_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[2]/a"
READ_MORE_BUTTON_XPATH="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[2]"
CLOSE_X_XPATH="//body/div[@role='dialog']/div//button[@type='button']"
READ_HIDE_BUTTON_XPATH="//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[2]/button"
NO_READ_XPATH="//div[contains(@style, 'background-color: rgb(237, 237, 237)')]"
READ_MORE_BUTON_XPATH=".//span[contains(text(), 'Devamını Oku')]"
ABOUT_CLICK_BUTTON_XPATH="/html/body/div[4]/div/div/div[2]"
EXAMS_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/span"
EXAMS_CONTENT_XPATH="/html/body/div[1]/div/main/div[1]/section[3]/div/div/div[2]/div"
EXAMS_BUTTON_XPATH="//div[@id='__next']/div[@class='back-white']//div[@class='plaform-page']/section[3]//div[@class='exams my-3']/div"
EXAMS_WİNDOW_XPATH="/html/body/div[4]/div/div"
VIEW_THE_REPORT_BUTTON_XPATH="/html/body/div[4]/div/div/div/div/div[2]/div[2]/button"
REPORT_POPUP_XPATH="/html/body/div[4]/div/div/div/div/div/div[1]"
DETAILS_XPATH="//*[@id='dynamicContent']"
AREA_CONTROL_BOTTOM_XPATH="//*[@id='__next']/div/main/div[1]/section[4]/div/div"
#YABANCI DİL XPATH:
RIGHT_NAME_DROPDOWN_XPATH= "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button/div[2]" 
MY_LANGUAGE_SIDEBAR_XPATH="//*[contains(text(),'Yabancı Dillerim')]"
SELECT_THE_LANGUAGE_DROPDOWN_XPATH="//*[contains(text(), 'Dil Seçiniz')]"
SELECT_LEVEL_XPATH= "//*[contains(text(), 'Seviye Seçiniz')]"
OPTION_GERMAN_XPATH="//*[contains(text(), 'Almanca')]"
OPTION_CEKCE_XPATH= "//*[contains(text(), 'Çekçe')]"
OPTION_CHINESE_XPATH="//*[contains(text(), 'Çince (Mandarin)')]"
OPTION_NORVEGIAN_XPATH="//*[contains(text(), 'Norveççe')]"
OPTION_ENGLISH_XPATH= "//*[contains(text(), 'İngilizce')]"
BASIC_LEVEL_XPATH= "//*[contains(text(), 'Temel Seviye ( A1 , A2)')]"
INTERMEDIATE_LEVEL_XPATH="//*[contains(text(), 'Orta Seviye (B1 , B2)')]"
ADVANCED_LEVEL_XPATH="//*[contains(text(), 'İleri Seviye (C1 , C2)')]"
MOTHER_LANGUAGE_LEVEL_XPATH="//*[contains(text(), 'Anadil')]"
SELECTED_NORVEGIAN="//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]"
SELECTED_GERMAN_XPATH="//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
SAVE_BUTTON_XPATH= "//*[contains(text(), 'Kaydet')]"
ANSWER_YES_XPATH= "//*[contains(text(), 'Evet')]"
LANS_SECTION_XPATH="//div[@class='tobeto-light-bg section-p my-langs']"
LANG_EDIT_ELEMENT_XPATH="//div[@class='lang-edit']"
SELECTED_LANGUAGES_XPATH= "//*[@id='__next']/div/main/section/div/div/div[2]/div/div"
LANGUAGE_REQUIRED_FIELD_XPATH=  "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/p"
LEVEL_REQUIRED_FIELD_XPATH= "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/p"
ADDED_XPATH= "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
REMOVED_MESSAGE_XPATH= "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
ALREADY_ADDED_MESSAGE_XPATH= "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
GO_TO_LANGUAGE_XPATH="/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/div/div/div[1]"
DELETE_ELEMENT_XPATH="/html/body/div[1]/div/main/section/div/div/div[2]/div/div/div[1]/span[2]"

#----------------TEXT
SUCCESSFUL_LOGIN_TEXT="• Giriş başarılı."
TOBETO_SLOGAN_TEXT="Yeni nesil öğrenme deneyimi ile Tobeto kariyer yolculuğunda senin yanında!"
FREE_EDUC_TEXT= "Ücretsiz eğitimlerle, geleceğin mesleklerinde sen de yerini al."
ARADIGIN_IS_TEXT = "Aradığın  “İş”  Burada!"
MEMBER_NAME_TEXT="Sevda"
WELCOMETOBETO_TEXT= "TOBETO'ya hoş geldin"
NO_SURVEY_TEXT="Atanmış herhangi bir anketiniz bulunmamaktadır"
NO_ANNOUNCEMENT_TEXT="Bir duyuru bulunmamaktadır."
REQUIRED_FIELD_TEXT= "Doldurulması zorunlu alan*"
ADDED_LANGUAGE_TEXT="• Yabancı dil bilgisi eklendi."
LANGUAGE_REMOVED_TEXT="• Yabancı dil kaldırıldı."
ALREADY_EXISTS_LANGUAGE_TEXT="• Bu dil zaten mevcut."
EXAMS_CONTENT_TEXT='Herkes İçin Kodlama 3A Değerlendirme Sınavı\nHerkes İçin Kodlama - 3A\n45 Dakika'
REPORT_POPUP_TEXT='Doğru\nYanlış\nBoş\n0\nPuan' 
AREA_CONTROL_BOTTOM_TEXT='Profilini oluştur\nBaşla\n\nKendini değerlendir\nBaşla\n\nÖğrenmeye başla\nBaşla'
DETAILS_TEXT="Herkes İçin Kodlama - 3A\nBaşardın" 
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
ISTANBUL_CODDING_ID="react-select-2-listbox"

#------------CSS SELECTOR
ISTANBUL_KODLUYOR_LOGO_CSS_SELECTOR= ".p-4 > span > img"

#-----------CLASS NAME
X_BUTTON_CLASSNAME="css-8mmkcg"
DROPDOWN_PROFILE_INFO_CLASS_NAME=  "dropdown-item"




























