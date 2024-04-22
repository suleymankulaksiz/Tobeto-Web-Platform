#-------------------BASEURL-----------------------
LOGIN_URL="https://tobeto.com/giris"



#------------------DATAS--------------------------
loginUserName="ozmrym7@gmail.com"
loginPassword="mrym1081"
adSoyad="Can Canan"






#--------------LOCATORS---------------------------
loginEmail_name="email"
loginPassword_name="password"
loginButton_css=".btn.btn-primary.w-100.mt-6"
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