
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












