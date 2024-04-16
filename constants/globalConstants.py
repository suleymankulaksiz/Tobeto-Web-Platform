import random
import string


def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])
        extension = random.choice(['com', 'net', 'org'])
    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom


#-------------------------------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
SIGN_IN = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=service%3A%3Aaccount.microsoft.com%3A%3AMBI_SSL+openid+profile+offline_access&response_type=code&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin-oauth&client-request-id=d7f1d419-964c-4163-a89e-749c64f1940d&x-client-SKU=MSAL.Desktop&x-client-Ver=4.58.1.0&x-client-OS=Windows+Server+2019+Datacenter&prompt=login&client_info=1&state=H4sIAAAAAAAEAAXBS4JDMAAA0LvM1mKMFrWkSEKLUeKzKxWk4pN2krann_e-bKHOe2lKN79DaXRwIoETgaFs8003-8PUZQ0YN9YBbFPAtUbkMvRKRHSm_NogHeNO2kHCpiLzp8u90HRaU-vnvPABG1W2tm3L8HzcY1kPLtF79pQp0XcCpg79BL62qtjQzPLA84xU1KvUMFvDt9mQFI95-JHmJtYY3KIIHaV0F4_sr4ZjQqdI_sS3ONzhzFnFq16x7LLO-On5xoVEU-vGYq5ZWSXau6_ZuKWnWIHqULUPDBcgfazilxzPZ-otL3Y1qE-v8HIK3cKLobOiptkteKMW4g9XPPIAJVuO_PFGCUiHeoxdhCKuWH0ffv0DMZBRVEIBAAA&msaoauth2=true&lc=1055"
#-------------------------------------------
FIRSTNAME_NAME = "firstName"
LASTNAME_NAME = "lastName"
EMAIL_NAME ="email"                        #  BUNLAR KAYIT OL AŞAMASINDAKİ FORMUN LOCATORLARI
PASSWORD_NAME ="password"
PASSWORDAGAIN_NAME= "passwordAgain"
SIGN_IN_EMAIL_NAME= "loginfmt"
SING_IN_PASSWORD_NAME= "passwd"
RESET_PASSWORD_XPATH= "///input[@name='password']"
RESET_PASSWORD_AGAIN_XPATH="//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form//input[@name='passwordConfirmation']"


#-------------------------------------------
input_firstname ="Can"
input_lastname ="Canan"
input_email ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXtobeto@hotmail.com"          #BURADA KAYIT OL AŞAMASINDA FORM VERİLERİ VAR.
input_password ="123456"
input_passwordagain="123456"

#ŞİFRE YENİLEME INPUT
input_forgot_email ="tobeto@outlook.com.tr"  #şifre yenileme e mail 
input_forgot_password = "//*[@id='__next']/div/main/section/div/div/div/input"
input_sign_in_password = "123456"
input_reset_password = "1234567"    #Buraya tekrar bak
input_reset_password_again="1234567"  #Buraya tekrar bak


#------------------------------------------
SIGNUPBUTTON_XPATH ="//*[@id='__next']/div/main/section/div/div/div[1]/div/div/button"    #-KAYIT OL AŞAMASINDAKİ BUTON



NAVMENU_XPATH ="//*[@id='O365_MainLink_NavMenu']"
NAVMENU_OUTLOOK_XPATH="//*[@id='O365_AppTile_Mail']/div[1]/div/span"
CLICK_MAIL_LINK_XPATH = "//*[@id='UniqueMessageBody']/div/div/div/div/div"
SENDBUTTON_XPATH = "//*[@id='__next']/div/main/section/div/form/div/div/button"
CLICK_MAIL_XPATH="//*[@id='MailList']/div/div/div/div/div/div/div/div[2]"





#ŞİFREMİ UNUTTUM
FORGOT_PASSWORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p"  #ŞİFREMİ UNUTTUM BUTONU
FORGOT_EMAIL_XPATH="//*[@id='__next']/div/main/section/div/div/div/input"
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

FORGOT_EMAIL_POPUP_XPATH = "//*[@id='__next']/div/main/div[2]/div/div[2]"

TRUEREGISTER_TEXT="Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."
FORGOT_EMAIL_POPUP_TEXT="• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."





#-----------------------------------------TEST-1-4 My Personal Information------------------------------------

#---------TEST-1-4 My Personal Information---------

#XPATH
LOGIN_MAIL_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']"
LOGIN_PASSWORD_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']"
LOGIN_BUTTON_XPATH = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']"
LOGIN_POPUP_XPATH = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
PROFILETITLE_TEXT_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/h1"
PROFILEBUTTON_XPATH="//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button"
NAMETEXTBOX_XPATH="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='name']"
SURNAMETEXTBOX_XPATH ="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='surname']"
NAME_TEXT_XPATH="//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']/form[@action='#']//input[@name='name']"
DATEOFBIRTH_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/input"
MAILCLICK_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/input"
COUNTRYBOXCLICK_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[8]/input"
DROPDOWN_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[9]/select"
TOWNBOX_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[10]/select"
SAVEBUTTON_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
TCNO_XPATH="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/input"


#INPUT
input_personal_mail="tobeto@outlook.com.tr"
input_personal_password="123456"
input_dateofbirth = "31.08.2000"
input_country="Türkiye"
input_tcno="11111111111"

#TEXT
POPUP_MESSAGE_TEXT="• Giriş başarılı."





























