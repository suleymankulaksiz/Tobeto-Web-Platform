
#--------------------------------------RANDOMAIL--------------------------------------
import random
import string




def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])

        extension = random.choice(['com', 'net', 'org'])

        extension = random.choice(['com', 'net', 'org'])                                       #burada random mail oluşturma işlemi yapıyoruz.

    
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


#--------------------------------------URL--------------------------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
WAITREGISTER_URL ="https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
PLATFORM_URL = "https://tobeto.com/platform"

#--------------------------------------LOCATORS--------------------------------------
FIRSTNAME_NAME = "firstName"
LASTNAME_NAME = "lastName"
EMAIL_NAME ="email"                        
PASSWORD_NAME ="password"
PASSWORDAGAIN_NAME= "passwordAgain"
SIGNUPBUTTON_XPATH ="//*[@id='__next']/div/main/section/div/div/div[1]/div/div/button"

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
LOGIN_POPUP_XPATH = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
LOGIN_POPUP_ALERTQUIT_XPATH = "//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
PROFILETITLE_TEXT_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/h1"
PROFILEBUTTON_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button"
SIGNINEMAIL_ID="identifierId"
LOGINNEXTBUTTON_XPATH = "//*[@id='identifierNext']/div/button/span"
SINGINPASSWORD_XPATH = "//*[@id='password']/div[1]/div/div[1]/input"
LOGINSINGINBUTTON_XPATH = ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"
LASTMAILLINK_CSS = ".zA.zE:nth-child(1)"
EMAILCONTENT_XPATH = "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div"



REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
SIGN_IN = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ARZ0qKLNZc5pRQzHoOzteY4CudTe8H6l8-KtvsTwhZph01Tk5xET568QYhi7ldsRXg71pdveoNSNLg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1341264521%3A1713475719969411&theme=mn&ddm=0"



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
INVALIDMAILPOPUP_XPATH="//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"

"//*[@id='__next']/div/main/div[2]/div/div[2]"
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
INVALIDMAILPOPUPXPATH_TEXT = "• Girdiğiniz e-posta geçersizdir."


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

TCNO_XPATH="/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[6]/input"
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
avatar_photo_path = r"C:\Users\slyma\OneDrive\Masaüstü\Pair3-Tobeto-Proje-1\images\tobeto.png"
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
DELETEBUTTONCLICK_TEXT ="Seçilen sertifikayı silmek istediğinize emin misiniz?"
TXTFILEUPLOADALERT_TEXT = "Sadece image/jpeg, image/png, application/pdf yükleyebilirsiniz"
TWOFILEUPLOADALERT_TEXT = "Sadece 1 dosya yükleyebilirsiniz"




#------------------Sertifikalarım TC 13-15

#XPATH 
UPLOAD_AREA_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div"
SAVEBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
UPLOAD_XPATH="(//input[@type='file'])[1]"
UPLOAD_AREA_XPATH2="/html/body/div[1]/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div"
UPLOAD_FILE_BUTTON_XPATH="//button[@class='uppy-u-reset uppy-c-btn uppy-StatusBar-actionBtn uppy-StatusBar-actionBtn--upload uppy-c-btn-primary']"
CERTIFICATES_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[5]/span[2]"
CLICKXBUTTON_XPATH = "/html/body/div[1]/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/div[2]/div[2]/button"
DOWNLOADFILEBUTTON = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[4]/span[1]"
DELETEFILEBUTTON = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[4]/span[2]"
DELETEFILEYESBUTTON = "/html/body/div[4]/div/div/div/div/div/div[2]/button[2]"
DELETEBUTTONCLICKTEXT_XPATH ="/html/body/div[4]/div/div/div/div/div/p[1]"
TXTFILEUPLOADALERT_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/span/div/p"
TWOFILEUPLOADALERT_XPATH = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[4]/div[2]/span/div/p"


PHONECHECK_XPATH = "/html//input[@id='phoneNumber']"
CONTINUEBUTTON_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"
REGISTERTEXT_XPATH = "/html/body/div[1]/div/main/section/div/div/div/div/span"
IFRAME_XPATH="//iframe[@title='reCAPTCHA']"
CAPTCHA_XPATH = "//*[@id='recaptcha-anchor']"
PASSWORDCONTROL_XPATH = "div[role='alert'] > .toast-body"
EMAILCONTROL_XPATH ="div[role='alert'] > .toast-body"
CONTRACTWINDOWS_XPATH = "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//p[@class='alert-message mx-3']"
LOGIN_BUTTON_XPATH ="/html/body/div[1]/div/main/section/div/div/div[1]/div/form/button"
SETTING_LOGIN_ALERT_XPATH ="//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
HOME_PROFILE_BUTTON_XPATH ="/html/body/div[1]/div/nav/div[1]/div/div/div[2]/button"
PROFILE_INFO_BUTTON_XPATH="/html/body/div[1]/div/nav/div[1]/div/div/div[2]/ul/li[1]/a"
SETTING_BUTTON_XPATH ="/html/body/div[1]/div/main/section/div/div/div[1]/div/a[8]/span[1]"
TERMINATION_BUTTON_XPATH ="/html/body/div[1]/div/main/section/div/div/div[2]/div/div/div[2]/button"
TERMINATION_WINDOW_XPATH ="/html/body/div[4]/div/div/div/div/div/p[1]"
TERMINATION_YES_BUTTON_XPATH="/html/body/div[4]/div/div/div/div/div/div[2]/button[2]"
TERMINATION_ALERT_XPATH ="//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
OLD_PASSWORD_XPATH ="currentPassword"
NEW_PASSWORD_AREA_XPATH="passwordConfirmation"
CHANGE_PASSWORD_BUTTON_XPATH="/html/body/div[1]/div/main/section/div/div/div[2]/div/div/div[1]/button"
CHANGE_PASSWORD_ALERT_XPATH="//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
EMPTY_PASSWORD_ALERT_XPATH ="/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/span"
SET_PROFILE_BUTTON_XPATH="/html/body/div[1]/div/main/div[1]/section[3]/div/div/div[1]/div/button"
PHONE_LONG_SHORT_ALERT_XPATH="/html/body/div[4]/div/div/div/div/div/label[4]/small/p"
WRONG_EMAIL_ALERT_XPATH="/html/body/div[1]/div/main/section/div/div/div[1]/div/div/form/p"
#--------------------------------------INPUTS--------------------------------------
input_firstname ="Can"
input_lastname ="Canan"
input_email ="tobeto@hotmail.com"          #BURADA KAYIT OL AŞAMASINDA FORM VERİLERİ VAR.
input_password ="123456"
input_passwordagain="123456"
input_phone ="549 490 30 04"
input_wronfFormat_email="asdqwe"
input_alreadyemail ="denemehesabi292@outlook.com"
#--------------------------------------BOŞHESAP--------------------------------------
input_emptyuserE = "tobeto@outlook.com.tr"
input_emptyuserpasswordE = "deneme123"
#alttaki komple boş
input_emptyuser = "denemehesabi292@outlook.com"
input_emptyuserpassword = "333333"
#Süleyman ayarlar bölümü için kullanılan hesaplar
input_setting_email ="aarjav.panth@foodfarms.net"
input_setting_password ="123123"
input_setting_newPassword="111111"
input_setting_email_two = "gennaro.adriann@foodfarms.net"
input_setting_password_two="123456"
#--------------------------------------TEXTS--------------------------------------
TRUEREGISTER_TEXT="Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."
EMPTY_FIELDS_TEXT  = "Doldurulması zorunlu alan*"
PASSWORDCONTROL_TEXT ="• Şifreler eşleşmedi"
EMAILCONTROL_TEXT ="• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
CONTRACTWINDOWS_TEXT ="Kayıt oluşturmak için gerekli sözleşmeler"
WRONG_OLD_PASSWORD_TEXT ="• Mevcut şifre geçersizdir."
SHORT_PASSWORD_TEXT = "• Şifreniz en az 6 karakterden oluşmalıdır."
SAME_CHANGE_PASSWORD_TEXT ="• Yeni şifreniz mevcut şifrenizden farklı olmalıdır."
DIFFRENT_PASSWORD_TEXT ="• Girilen şifreler eşleşmiyor kontrol ediniz.."
TERMINATION_WINDOW_TEXT="Hesabınızı silmek istediğinize emin misiniz?"
TERMINATION_EXPECTED_TEXT="Hesabınız silindi."
TRUE_CHANGE_PASSWORD_TEXT ="• Şifreniz güncellenmiştir."
REGISTER_NUMBER_TEXT="Girdiğiniz telefon numarası ile kayıtlı üyelik bulunmaktadır."
PHONE_LONG_LENGTH_TEXT ="En fazla 10 karakter girebilirsiniz."
PHONE_SHORT_LENGTH_TEXT ="En az 10 karakter girmelisiniz."
WRONG_MAIL_TEXT ="Geçersiz e-posta adresi*" 



##### MERYEM
#-------------------BASEURL-----------------------
LOGIN_URL_M="https://tobeto.com/giris"
#------------------DATAS--------------------------
loginUserName="ozmrym7@gmail.com"
loginPassword="mrym1081"
adSoyad="Can Canan"
#--------------LOCATORS---------------------------
loginEmail_name="email"
loginPassword_name="password"
loginButton_css=".btn.btn-primary.w-100.mt-6"
egitimlerimbutton_css="#lessons-tab"
dahaFazlaGoster_xpath="(//div[@class='showMoreBtn'])[1]"
tumEgitimlerim_css="#all-lessons-tab"
devamEttiklerim_css="#started-tab"
tamamladiklarim_css="#done-lessons-tab"
aramaKutusu_css="#search"
aramaSonucu_xpath="(//span[text()='İstanbul Kodluyor Proje Aşamaları'])[1]"
sonuc="İstanbul Kodluyor Proje Aşamaları"
kurumSeciniz_css="#react-select-6-placeholder"
kurumSecinizBosalt_class="select__indicator select__clear-indicator css-1xc3v61-indicatorContainer"
siralama_xpath="(//*[@class='css-8mmkcg'])[4]"
egitimYokMsj_xpath="//p[text()='Size atanan herhangi bir eğitim bulunmamaktadır.']"
msj="Size atanan herhangi bir eğitim bulunmamaktadır."
#CHATBOXPAGE-----------
msjIkon_css=".exw-open-launcher"
kucultmeIkon_css=".exw-minimize-button.header-button"
karsilamaMsjlari_css=".exw-group-message.exw-from-response"
adSoyadBox_css=".exw-inline-response"
memnunOldumMsj_xpath="(//*[@class='exw-sender-response'])[3]"
yardimKonusu_xpath="(//div[@class='exw-reply'])[1]"
emojiButton_css=".exw-add-emoji"
elEmojisi_css="#skintone-button"
renkliEl_xpath="//button[@title='Bir ten rengi seçin (Şu anda Orta-Açık)']"
atachIkon_css=".exw-add-file"
dosyaSecButton_css=".exw-drag-drop-select-button"
gonderButton_xpath="(//button[@class='exw-drag-drop-select-button'])[2]"
dosyaGonderimiDogrulama_xpath="(//*[text()='can canan, üzgünüm tam olarak ne demek istediğinizi anlayamadım. Farklı bir şekilde ifade ederseniz tekrar deneyebilirim. Aşağıdaki konu başlıklarından yardım alabilirsiniz. 😊'])[1]"
expectedResult="can canan, üzgünüm tam olarak ne demek istediğinizi anlayamadım. Farklı bir şekilde ifade ederseniz tekrar deneyebilirim. Aşağıdaki konu başlıklarından yardım alabilirsiniz. 😊"
gorusmeyiSonlandirIkon_css=".exw-end-session-button.header-button"
hayirButton_xpath="//*[text()='Hayır']"
evetButton_xpath="//*[text()='Evet']"
gorusmeSonlandirmaDoğrulama_xpath="//*[text()='Bize puan vermek ister misiniz?']"
expectedDogrulama="Bize puan vermek ister misiniz?"
#PROFIL-SOSYALMEDİA DATA
linkedIn="https://www.linkedin.com/in/meryem-ozgun/"
instagram="instagramHesabimYok"
twitter="twitterHesabimYok"
#PROFİL-SOSYALMEDIA LOCATE
profilButton_css=".mb-0.name"  
medyaHesaplariButton_xpath="//*[text()='Medya Hesaplarım']"
secinizButton_css=".form-select"
sosyalMediaUrlBox_css=".form-control"
kaydetButton_css=".btn.btn-primary.py-2.mt-1.d-inline-block.mobil-btn"
linkedInIko_css=".form-control.input-linkedin"
deleteIkon_css=".btn.social-delete"
editIkonu_css=".fa.fa-pencil-square"  
uyariMsji_xpath="//*[text()='En fazla 3 adet medya seçimi yapılabilir.']"
msjIcerigi="En fazla 3 adet medya seçimi yapılabilir."
sMedyaBasariliEklendiMsj_css=".toast-body"
hesapSilOnayButton_css=".btn.btn-yes.my-3"
buHesapKayitliUyarisi_css=".toast-body"
doldurulmasiZorunluUyarisi_css=".text-danger"
basariylaSilindiMsj_css=".toast-body"




#-------------------------------------KEVSER--------------------------------------
#-------------------------------------US2-----------------------------------------
LOGIN_URL = "https://tobeto.com/giris"
HOMEPAGE_URL= "https://tobeto.com/platform"

#-------------------------------------LOCATORS------------------------------------
loginEmail_name = "email"
loginPassword_name= "password"
loginButton_xpath= "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
invalidLoginError_xpath= "//div[@id='__next']/div/main/div[2]/div/div[2]"
loginEmptyEmail_xpath="//*[@id='__next']/div/main/section/div/div/div[1]/div/form/p[1]"
loginEmptyPassword_xpath= "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/p[2]"
loginSignUp_xpath= "//*[@id='__next']/div/main/section/div/div/div[1]/div/div[2]/label/small/a"
#-------------------------------------INPUTS------------------------------------
input_loginEmail= "kvsyilmaz98@gmail.com"
input_loginPassword= "201618"
input_empty= ""

#------------------------------------TEXTS---------------------------------------
login_invalidLogin_text= "• Geçersiz e-posta veya şifre."
empty_fields_text= "Doldurulması zorunlu alan*"


#------------------------------------US8-----------------------------------------
#------------------------------------URL-----------------------------------------
ASSESSMENTS_URL = "https://tobeto.com/degerlendirmeler"
ASSESSMENT_URL = "https://tobeto.com/profilim/degerlendirmeler/tobeto-iste-basari-modeli/1"

#-------------------------------------LOCATORS------------------------------------
assessments_xpath = "//*[@id='__next']/div/nav/div[1]/ul/li[3]/a" 
assessments_header_xpath= "//*[@id='__next']/div/main/section[1]/div/div[2]/div/h3"
assessment_element_xpath = "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div"
assessmentStart_xpath= "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a"
assessmentStart2_xpath= "//*[@id='__next']/div/main/section/div/div/div/div[3]/a"
assessmentPage_xpath= "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/span/p"
softwareTestInformation1_xpath= "//*[@id='__next']/div/main/section[2]/div/div/div[3]/div"
softwareTest_xpath= "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/div/span"
SoftwareTestStart_xpath= "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/button"
SoftwareTestStart2_xpath= "/html/body/div[4]/div/div/div/div/div[2]/div[2]/button"
softwareTestControl_xpath= "/html/body/div[5]/div/div/div/div/div[1]/div/div[1]"
subscribe_xpath= "//*[@id='__next']/div/main/section[3]/div/div[2]/div/h3"
subscribeInformation1_xpath= "//*[@id='__next']/div/main/section[4]/div/div/div[1]/div"
subscribeInformation2_xpath= "//*[@id='__next']/div/main/section[4]/div/div/div[2]/div"

#------------------------------------TEXTS---------------------------------------
assessmentsHeader_text= "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
assessment_element_text= "Tobeto İşte Başarı Modeli\n80 soru ile yetkinliklerini ölç, önerilen eğitimleri tamamla, rozetini kazan.\nBaşla"
assessmentPage_text= "Belirsizliğin yüksek olduğu zaman ya da ortamlarda ortaya çıkan koşullara uygun olarak anlık çözümler geliştirebilirim."
softwareTestInformation1_text= "Yazılımda Başarı Testi\nÇoktan seçmeli sorular ile teknik bilgini test et.\n>>>"
softwareTest_text= "Front End"
softwareTestStart_text= "Başla"
softwareTestControl_text= "1/25"
subscribe_text= "Aboneliğe özel değerlendirme araçları için"
subscribeInformation1_text= "Kazanım Odaklı Testler\nDijital gelişim kategorisindeki eğitimlere başlamadan öncekonuyla ilgili bilgin ölçülür ve seviyene göre yönlendirilirsin."
subscribeInformation2_text= "Huawei Talent Interview\nTeknik Bilgi Sınavı*\nSertifika alabilmen için, eğitim yolculuğunun sonunda teknik yetkinliklerin ve kod bilgin ölçülür.\n\n4400+ soru | 30+ programlama dili\n4 zorluk seviyesi\n*Türkiye Ar-Ge Merkezi tarafından tasarlanmıştır."



#------------------------------------US9----------------------------------------------
#------------------------------------URL----------------------------------------------
MYPROFILE_URL= "https://tobeto.com/profilim"
EDITPROFILE_URL= "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
REALUSER_URL= "https://tobeto.com/profiller/5bfda759-7de5-42e4-9d30-158a8d25b6cd"
PROFILETEST_URL= "https://tobeto.com/profilim/degerlendirmeler/tobeto-iste-basari-modeli"

#-----------------------------------LOCATORS------------------------------------------
MYPROFILE_XPATH= "//*[@id='__next']/div/nav/div[1]/ul/li[2]/a"
SHARELINK_ID= "dropdown-basic"
SHARELINKCONTROL_XPATH= "//*[@id='__next']/div/main/div/div[1]/div/div/div/div[1]/p"
COPYLINK_XPATH= "//*[@id='__next']/div/main/div/div[1]/div/div/div/div[2]/div/i"
COPYLINKCONTROL_XPATH= "//div[@id='__next']/div/div[2]/div/div[2]"
EDITICON_CLASSNAME= "cv-edit-icon"
HEADERSCONTROL_CLASSNAME= "cv-box-header"
INFORMATIONSCONTROL_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/span[2]"
INFORMATIONSBOX_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[1]"
ABOUT_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[2]/div"
COMPETENCIES_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[3]/div"
FOREIGNLANGUAGES_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[4]/div"
CERTIFICATES_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[5]/div"
SOCIALMEDIA_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[6]/div"
SEEICON_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[3]/div/div[1]/div/span[2]"
OPENCOMPETENCIESCONTROL_XPATH= "/html/body/div[4]/div/div/div[1]"
COMPETENCIESCLOSE_XPATH= "/html/body/div[4]/div/div/div[1]/button"
DOWNLOADCERTIFICATE_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[5]/div/div[2]/div"
SHOWSOCIALMEDIA_XPATH= "//div[@id='__next']/div/main/div/div[2]/div/div/div[6]/div/div[2]/a"
PROFILERIGHTPART_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[2]"
EDUCATIONLIFEELEMENT_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[5]/div/div[2]"
PROFILETESTSTARTBUTTON_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[1]/div/div[2]/div/a"
PROFILETESTREVIEWBUTTON_XPATH= "//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[1]/div/div[1]/div/span[2]"
PROFILETESTALERT_XPATH= "//div[@id='__next']/div/div[3]/div/div[2]"
MYACTIVITY_CSS= ".react-calendar-heatmap-week:nth-child(1) > .empty-data:nth-child(1)"
#------------------------------------TEXTS--------------------------------------------
SHARELINKCONTROL_TEXT= "Profilimi paylaş"
COPYLINKCONTROL_TEXT= "• Url kopyalandı."
HEADERSCONTROL_TEXTS= ['Hakkımda', 'Yetkinliklerim', 'Yabancı Dillerim', 'Sertifikalarım', 'Medya Hesaplarım', 'Tobeto İşte Başarı Modelim', 'Tobeto Seviye Testlerim', 'Yetkinlik Rozetlerim', 'Aktivite Haritam', 'Eğitim Hayatım ve Deneyimlerim']
INFORMATIONSCONTROL_TEXT= "Girilmemiş"
ABOUT_TEXT= "Hakkımda\nKendini kısaca anlat"
COMPETENCIES_TEXT= "Yetkinliklerim\nHenüz bir yetkinlik eklemedin."
FOREIGNLANGUAGES_TEXT= "Yabancı Dillerim\nHenüz bir yabancı dil eklemedin."
CERTIFICATES_TEXT= "Sertifikalarım\nHenüz bir sertifika yüklemedin."
SOCIALMEDIA_TEXT= "Medya Hesaplarım\nHenüz bir hesap eklemedin."
OPENCOMPETENCIESCONTROL_TEXT= "Tüm Yetkinliklerim"
PROFILETESTALERT_TEXT= "• Sınavı bitirmediniz."
MYACTIVITY_TEXT= "Herhangi bir aktiviteniz yok : 0"

#-----------------------------------US10--------------------------------------
#--------------------------------------URL----------------------------------
TESTREPORT_URL= "https://tobeto.com/profilim/degerlendirmeler/rapor/tobeto-iste-basari-modeli/1"

#---------------------------------------LOCATORS-------------------------------
SHOWREPORT_XPATH= "//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a"
REPORTHEADER_XPATH= "//*[@id='__next']/div/main/div/div"
REPORTINFORMATION_CLASSNAME= "legendName"
#REPORTVIEWCONTROL_XPATH= "//*[@id='__next']/div/main/section/div/div"
#REPORTINFORMATION_XPATH= "//*[@id='__next']/div/main/section/div/div/div/div/div[2]/div"
#---------------------------------------TEXTS------------------------------------
REPORTINFORMATIONS_TEXTS= ['Yeni dünyaya hazırlanıyorum', 'Profesyonel duruşumu geliştiriyorum', 'Kendimi tanıyor ve yönetiyorum', 'Yaratıcı ve doğru çözümler geliştiriyorum', 'Başkaları ile birlikte çalışıyorum', 'Kendimi sürekli geliştiriyorum', 'Sonuç ve başarı odaklıyım', 'Anlıyorum ve anlaşılıyorum']

#---------------------------------------------US11-----------------------------
#------------------------------------------URL---------------------------------
SETTINGS_URL= "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
COMPETENCIES_URL= "https://tobeto.com/profilim/profilimi-duzenle/yetkinliklerim"

#------------------------------------------LOCATORS----------------------------
CLOSEALERT_XPATH= "//div[@id='__next']/div/div[2]/div/div/button"
CREATEPROFILBUTTON_XPATH= "//*[@id='__next']/div/main/div[1]/section[4]/div/div/div[1]/div/button"
SETTINGSCOMPETENCIESBUTTON_XPATH= "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[4]"
DROPDOWNCOMPETENCIES_XPATH= "//div[2]/div/div/div/div/div/div[2]"
DROPDOWNOPTION1_ID= "react-select-2-option-0"
DROPDOWNOPTION2_ID= "react-select-2-option-1"
DELETEFIRSTOPTION_XPATH= "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]"
SAVECOMPETENCIES_XPATH= "//div[@id='__next']/div/main/section/div/div/div[2]/button"
COMPETECENTIES_SAVED_CONTROL_XPATH= "//div[@id='__next']/div/div[2]/div/div[2]"
EMPTYCOMPETENCEALERT_XPATH= "//div[@id='__next']/div/div[2]/div/div[2]"
DELETECOMPETENCEBUTTON_XPATH="/html/body/div/div/main/section/div/div/div[2]/div[2]/div[8]/div/span"
DELETECOMPETENCEBUTTON2_XPATH= "//button[2]"
COMPETENCEDELETEDALERT_XPATH= "//div[@id='__next']/div/div[2]/div/div[2]"
#------------------------------------------TEXTS-------------------------------
COMPETENCIES_SAVED_CONTROL_TEXT= "• Yetenek eklendi."
EMPTYCOMPETENCEALERT_TEXT= "• Herhangi bir yetenek seçmediniz!"
COMPETENCEDELETEDALERT_TEXT= "• Yetenek kaldırıldı."








#-----------------------SEVDA--------------------
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
BASIC_LEVEL_XPATH= "//*[contains(text(), 'Temel Seviye ( A1 , A2)')]"
INTERMEDIATE_LEVEL_XPATH="//*[contains(text(), 'Orta Seviye (B1 , B2)')]"
ADVANCED_LEVEL_XPATH="//*[contains(text(), 'İleri Seviye (C1 , C2)')]"
MOTHER_LANGUAGE_LEVEL_XPATH="//*[contains(text(), 'Anadil')]"
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
<<<<<<< HEAD
=======



>>>>>>> master


>>>>>>> c71bea667f15caf0433545c35f3ac595ff5db734



