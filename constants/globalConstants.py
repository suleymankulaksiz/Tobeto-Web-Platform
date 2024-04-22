
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








