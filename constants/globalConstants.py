
#--------------------------------------RANDOMAIL--------------------------------------
import random
import string

def generate_random_email():
        # Rastgele bir e-posta adresi oluştur
        username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        domain = random.choice(['gmail', 'hotmail', 'outlook', 'yahoo', 'yandex'])
        extension = random.choice(['com', 'net', 'org'])                                       #burada random mail oluşturma işlemi yapıyoruz.
    
        emailrandom = f"{username}@{domain}.{extension}"
        return emailrandom
#--------------------------------------URL--------------------------------------
REGISTER_URL = "https://tobeto.com/kayit-ol"
LOGIN_URL = "https://tobeto.com/giris"
WAITREGISTER_URL ="https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
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
PHONECHECK_XPATH = "/html//input[@id='phoneNumber']"
CONTINUEBUTTON_XPATH ="/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//button[@class='btn btn-yes my-3']"
REGISTERTEXT_XPATH = "/html/body/div[1]/div/main/section/div/div/div/div/span"
IFRAME_XPATH="//iframe[@title='reCAPTCHA']"
CAPTCHA_XPATH = "//*[@id='recaptcha-anchor']"
PASSWORDCONTROL_XPATH = "div[role='alert'] > .toast-body"
EMAILCONTROL_XPATH ="div[role='alert'] > .toast-body"
CONTRACTWINDOWS_XPATH = "/html/body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']//p[@class='alert-message mx-3']"
#--------------------------------------INPUTS--------------------------------------
input_firstname ="Can"
input_lastname ="Canan"
input_email ="tobeto@hotmail.com"          #BURADA KAYIT OL AŞAMASINDA FORM VERİLERİ VAR.
input_password ="123456"
input_passwordagain="123456"
input_phone ="549 490 30 04"
input_wronfFormat_email="asdqwe"
input_alreadyemail ="denemehesabi292@outlook.com"
#--------------------------------------TEXTS--------------------------------------
TRUEREGISTER_TEXT="Tobeto Platform'a kaydınız başarıyla gerçekleşti.\nGiriş yapabilmek için e-posta adresinize iletilen doğrulama linkine tıklayarak hesabınızı aktifleştirin."
INVALIDLOGIN_TEXT  = "Doldurulması zorunlu alan*"
PASSWORDCONTROL_TEXT ="• Şifreler eşleşmedi"
EMAILCONTROL_TEXT ="• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
CONTRACTWINDOWS_TEXT ="Kayıt oluşturmak için gerekli sözleşmeler"















