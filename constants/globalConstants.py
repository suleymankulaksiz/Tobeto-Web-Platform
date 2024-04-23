
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





