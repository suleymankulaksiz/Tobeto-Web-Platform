import random
import string


def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])
        extension = random.choice(['com', 'net', 'org'])
    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom


#--------------------URL-----------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
SIGN_IN = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKLNZc5pRQzHoOzteY4CudTe8H6l8-KtvsTwhZph01Tk5xET568QYhi7ldsRXg71pdveoNSNLg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1341264521%3A1713475719969411&theme=mn&ddm=0"

#-------------------------------------------
FIRSTNAME_NAME = "firstName"
LASTNAME_NAME = "lastName"
EMAIL_NAME ="email"                        #  BUNLAR KAYIT OL AŞAMASINDAKİ FORMUN LOCATORLARI
PASSWORD_NAME ="password"
PASSWORDAGAIN_NAME= "passwordAgain"
SIGN_IN_EMAIL_NAME= "loginfmt"
SING_IN_PASSWORD_NAME= "passwd"




#-------------------------------------------
input_firstname ="Can"
input_lastname ="Canan"
input_email ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXtobeto@hotmail.com"          #BURADA KAYIT OL AŞAMASINDA FORM VERİLERİ VAR.
input_password ="123456"
input_passwordagain="123456"

#ŞİFRE YENİLEME INPUT

input_forgot_password = "//*[@id='__next']/div/main/section/div/div/div/input"

  #Buraya tekrar bak


#------------------------------------------
SIGNUPBUTTON_XPATH ="//*[@id='__next']/div/main/section/div/div/div[1]/div/div/button"    #-KAYIT OL AŞAMASINDAKİ BUTON



NAVMENU_XPATH ="//*[@id='O365_MainLink_NavMenu']"
NAVMENU_OUTLOOK_XPATH="//*[@id='O365_AppTile_Mail']/div[1]/div/span"
CLICK_MAIL_LINK_XPATH = "//*[@id='UniqueMessageBody']/div/div/div/div/div"

CLICK_MAIL_XPATH="//*[@id='MailList']/div/div/div/div/div/div/div/div[2]"





#ŞİFREMİ UNUTTUM
FORGOT_PASSWORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p"  #ŞİFREMİ UNUTTUM BUTONU

SENDBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div/button"

next_login_button_id = "idSIButton9"
sign_in_button_id = "idSIButton9"
decline_button_id = "declineButton"






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



#---------------------------Preconditions-------------------------
#Login
profileTitleText= "Profilini oluştur"
LOGIN_MAIL_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']"
LOGIN_PASSWORD_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']"
LOGIN_BUTTON_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']"
LOGIN_POPUP_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
PROFILETITLE_TEXT_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/h1"
PROFILEBUTTON_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button"




#-----------------------------------------S03 TEST User Password Reset TC 1-4 ----------------------------------------

#XPATH

#ŞİFREMİ UNUTTUM BUTONU
FORGOT_PASSWORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p"


FORGOT_EMAIL_XPATH="//*[@id='__next']/div/main/section/div/div/div/input"
SENDBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/div/div/button"
RESETSENDBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/form/div/div/button"
FORGOT_EMAIL_POPUP_XPATH = "//*[@id='__next']/div/main/div[2]/div/div[2]"
FORGOT_EMAIL_POPUP_TEXT="• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
RESET_PASSWORD_XPATH= "//*[@id='__next']/div/main/section/div/form/div/div/input[1]"
RESET_PASSWORD_AGAIN_XPATH="//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form//input[@name='passwordConfirmation']"
PASSWORDNOTMATCHEDPOPUP_XPATH="//*[@id='__next']/div/main/div[2]/div/div[2]"
INVALIDMAILPOPUP_XPATH="//*[@id='__next']/div/main/div[2]/div/div[2]"

#INPUT
input_forgot_email ="tobetotest3@gmail.com" 
input_not_found_email = "tobetokayıtsız@gmail.com"
input_forgot_invalid_email ="a"
input_sign_in_password = "deneme123"
input_reset_password = "1234567"    
input_reset_password_again="1234567"
input_min_reset_password = "9876"    
input_min_reset_password_again="9876"
input_different_password = "9876"
input_different_password_again = "98765"
input_same_old_password = "deneme123"
input_same_old_password_again = "deneme123"
#ALERT TEXT
INCORRECTPASSWORDPOPUP_TEXT ="Şifreniz en az 6 karakterden oluşmalıdır."
SAMEOLDPASSWORDPOPUP_TEXT="Yeni şifreniz mevcut şifrenizden farklı olmalıdır."
NOTFOUNDEMAILPOPUP_TEXT = "Kullanıcı bulunamadı."
PASSWORDNOTMATCHEDPOPUP_TEXT = "• Şifreler Eşleşmedi"


#-----------------------------------------TEST My Personal Information------------------------------------

#---------TEST-1-4 My Personal Information---------

#XPATH
NAMETEXTBOX_XPATH="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='name']"
SURNAMETEXTBOX_XPATH ="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='surname']"
EMAILNAMETEXTBOX_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/input"
NAME_TEXT_XPATH="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='name']"
DATEOFBIRTH_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input"
MAILCLICK_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/input"
COUNTRYBOXCLICK_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/input"
DROPDOWN_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select"
TOWNBOX_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select"

TCNO_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input"
STREET_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/textarea"
ABOUTME_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/textarea"
TCNOALERT_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span[2]"
DATEOFBIRTHALERT_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/span"
COUNTRYBOXALERT_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span"
DROPDOWNELEMENTCITYALERT_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/span"
DROPDOWNELEMENTTOWNALERT_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/span"
STREETBOXALERT_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[11]/span"
ABOUTMEALERT_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[12]/span"
COUNTRYBOXALERT_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/span"
AVATARBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div"
AVATARPOPUPTEXT1_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]"
IMAGEUPLOADBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button"


DUSTBIN_CSS=".photo-delete"



UPLOAD_AREA_CLASS="uppy-Dashboard-overlay"
UPLOAD_FILE_BUTTON_XPATH1="//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button"

#PATH
avatar_photo_path = "C:/Users/Admin/Desktop/Tobeto Pair 3 Proje/Pair3-Tobeto-Proje/images/tobeto.png"
tobeto_png_path = "C:/Users/Admin/Desktop/Tobeto Pair 3 Proje/Pair3-Tobeto-Proje/images/tobeto.png"
tobeto_png2_path = "C:/Users/Admin/Desktop/Tobeto Pair 3 Proje/Pair3-Tobeto-Proje/images/tobeto2.png"

certificates_data_path = "C:/Users/Admin/Desktop/Tobeto Pair 3 Proje/Pair3-Tobeto-Proje/data/Tobeto.pdf"
txt_data_path ="C:/Users/Admin/Desktop/Tobeto Pair 3 Proje/Pair3-Tobeto-Proje/data/Tobeto.txt"

#ID
PHONETEXTBOX_ID = "phoneNumber"


#INPUT
input_personal_mail="tobetotest3@gmail.com"
input_personal_password="1234567"
input_dateofbirth = "31.08.2000"
input_country="Türkiye"
input_long_country="türkiyetürkiyetürkiyetürkiyetür"
input_incorrect_country="t"
input_tcno="11111111111"
input_incorrect_tcno="1111111111"
input_string_tcno="e"
input_incorrect_tcno2="111111111111"
input_street=long_text = "a" * 201
input_aboutme=long_text = "a" * 301

#ASSERT TEXT
POPUP_MESSAGE_TEXT="• Giriş başarılı."
TCNOALERT_TEXT="TC Kimlik Numarası 11 Haneden Az olamaz"
DATEOFBIRTH_ALERT_TEXT_XPATH = "Doldurulması zorunlu alan*"
COUNTRYBOX_ALERT_TEXT = "Doldurulması zorunlu alan*"
DROPDOWNELEMENTCITY_ALERT_TEXT = "Doldurulması zorunlu alan*"
DROPDOWNELEMENTTOWN_ALERT_TEXT = "Doldurulması zorunlu alan*"
STREETBOX_ALERT_TEXT = "En fazla 200 karakter girebilirsiniz"
ABOUTME_ALERT_TEXT = "En fazla 300 karakter girebilirsiniz" 
COUNTRYBOXALERT_TEXT = "En fazla 30 karakter girebilirsiniz"
AVATARPOPUPALERT_TEXT1 = "Sürükleyip bırak, yapıştır veya\ngözat"




#---------TEST-5-7 My Experience---------
#ALERT TEXT
EMPTY_ALERT_ALERT="Doldurulması zorunlu alan*"
MINCHARACTERS_POSITION_ALERT = "En az 5 karakter girmelisiniz"
MAXCHARACTER_ORGANIZATION_ALERT = "En fazla 50 karakter girebilirsiniz"
MINCHARACTERS_DESCRIPTION_ALERT = "En fazla 300 karakter girebilirsiniz"
CITYFALSEASSERT_TEXT ="Doldurulması zorunlu alan* Gözükmemektedir!"
PROFILETITLETEXT = "Profilini oluştur"


#PATH
SAVE_SCREENSHOT_PATH = "images//experienceViewing.png"

#COLOR CODE
city_border_color_text = "rgb(179, 166, 192)"


#XPATH
EXPERIENCEBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]"
INPUTORGANIZATIONNAME_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
POSITIONNAMEXPATH_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
SECTORNAME_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
DROPDOWNELEMENTCITY_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select"
JOBSTARTDATE_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input"
DROPDOWNELEMENTDATE_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input"
DROPDOWNELEMENTDATEMONTH_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"
SELECTDAY_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]"
EXPERIENCECHECKBOX_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/label[2]/input"
JOBDESCRIPTION_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea"
EXPERIENCEBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]/span[2]"
EXPERIENCESAVEBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"

#CSS SELECTOR
city_border_color_view_CSS = "#__next > div > main > section > div > div > div.col-12.col-lg-9 > form > div > div:nth-child(4) > select"

#ALERT XPATH
input_organization_name_alert_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/span"
position_name_name_alert_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
sector_name_name_alert_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
job_description_name_alert_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/span"
#INPUT 
job_start_date_input="01.01.2024"
input_organization_name_text = "Tobeto"
position_name_text ="Tester"
sector_name_text = "Yazılım"
job_description_text="abc"
input_organization_name_text=long_text = "E" * 51
job_description_name_text= "E"* 301
position_name_text = "e"



#---------TEST-8-9 Education---------

#XPATH
EDUCATIONSAVEBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
EDUCATIONSAVEBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]"
DROPDOWNELEMENTEDUCATION_XPATH= "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select"
EDUCATIONUNIVERSITYNAME_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
EDUCATIONSECTIONNAME_XPATH ="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
EDUCATIONSTARTYEAR_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input"
EDUCATIONSELECTYEAR_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]"
EDUCATIONENDYEAR_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input"
EDUCATIONSELECTENDYEAR_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[7]"
EDUCATIONUNIVERSITYNAME_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"

#TEXT
profileTitleText= "Profilini oluştur"
universityNameText = "Gebze Teknik Üniversitesi"
education_section_name = "Bilgisayar Mühendisliği"





#------------------Sertifikalarım TC 13-15

#XPATH 
UPLOAD_AREA_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div"
SAVEBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
UPLOAD_XPATH="(//input[@type='file'])[1]"
UPLOAD_AREA_XPATH2="/html/body/div[1]/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div"
UPLOAD_FILE_BUTTON_XPATH="//button[@class='uppy-u-reset uppy-c-btn uppy-StatusBar-actionBtn uppy-StatusBar-actionBtn--upload uppy-c-btn-primary']"
CERTIFICATES = "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[5]/span[2]"













