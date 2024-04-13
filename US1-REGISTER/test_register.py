import json
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image



class Test_Register:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                   #Buna baktım bu dosya içinde tutulması okunaklı ve olmasına adına daha çok tercih ediliyormuş diğer kullanım önerilmiyor.
        self.driver.get(REGISTER_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def take_and_show_screenshot(self, image_path):
        screenshot = Image.open(image_path)
        screenshot.show()

    


# Kullanıcının kayıt olma işlemi
    def test_register(self):
        emailrandom = generate_random_email()
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))
        firstname.send_keys(input_firstname)
        lastname.send_keys(input_lastname)
        email.send_keys(emailrandom)
        password.send_keys(input_password)
        password_again.send_keys(input_passwordagain)
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        sign_up_button.click()
        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys(input_phone)
        # iframe = self.waitForElementVisible((By.XPATH, IFRAME_XPATH))
        # self.driver.switch_to.frame(iframe)
        # captcha = self.waitForElementVisible((By.XPATH,CAPTCHA_XPATH))
        # captcha.click() 
        # self.driver.switch_to.frame(iframe)
                                             #bu şimdilik robot doğrulama geçmek için manuel yapıyorum.
        sleep(15)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        
        wait_url = WAITREGISTER_URL
        WebDriverWait(self.driver, 10).until(EC.url_to_be(wait_url))
        
        alertMessage = self.waitForElementVisible((By.XPATH, REGISTERTEXT_XPATH))
        assert alertMessage.text == TRUEREGISTER_TEXT


    
    def readInvalidDataFromJSON():
        with open(r'data/data.json', 'r') as file: # ilk baştaki r ön ek # testlerde genelde r kullanılır yani dosyayı okuma modunda açar.
            data = json.load(file) #JSON veriler Python veri yapısına dönüşür.
        return [(user['firstnamex'], user['lastnamex'], user['emailx'], user['passwordx'], user['passwordagainx']) for user in data['invalid_login_users']] #tuple list oluşturur.
    

    



# #Doldurulması zorunlu alanlarının boş bırakılma durumu
    @pytest.mark.parametrize("firstnamex, lastnamex,emailx,passwordx,passwordagainx", readInvalidDataFromJSON())
    def test_loginPass_box(self, firstnamex, lastnamex,emailx,passwordx,passwordagainx):
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))
        firstname.send_keys(firstnamex)
        lastname.send_keys(lastnamex)
        email.send_keys(emailx)
        password.send_keys(passwordx)
        password_again.send_keys(passwordagainx)
        # email.clear()
        # email_alert = self.waitForElementVisible(By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/div/form/p[1]") bu mecbur böyle çünkü otomasyonda email sonradan silince hata gözükmüyor.
        # assert email_alert.text
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        assert not  sign_up_button.is_enabled(), INVALIDLOGIN_TEXT
        
        


# # E-postanın geçersiz formatta girilmesi durumu       
    def test_wrongFormat_email(self):
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        email.send_keys(input_wronfFormat_email)
        wrongMail_alert=self.waitForElementVisible((By.XPATH,"/html/body/div[1]/div/main/section/div/div/div[1]/div/div/form/p"))
        assert wrongMail_alert.text =="Geçersiz e-posta adresi*"
        

     
# # "Şifre" ve "Şifre Tekrar" bölümlerinin eşleşmediği durumlar  
    def  test_passwordControl(self):
        emailrandom = generate_random_email()
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))
        firstname.send_keys(input_firstname)
        lastname.send_keys(input_lastname)
        email.send_keys(emailrandom)
        password.send_keys(input_password)
        password_again.send_keys("12345")
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        sign_up_button.click()
        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys(input_phone)
        sleep(15)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()

        passwordControl_alert=self.waitForElementVisible((By.CSS_SELECTOR,PASSWORDCONTROL_XPATH))
        assert passwordControl_alert.text ==PASSWORDCONTROL_TEXT

# #Kullanıcının sisteme kayıt olduğu e-posta adresinin sistemde mevcut olması
    def test_emailagain(self):
        
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))
        firstname.send_keys(input_firstname)
        lastname.send_keys(input_lastname)
        email.send_keys(input_alreadyemail)
        password.send_keys(input_password)
        password_again.send_keys(input_passwordagain)
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        sign_up_button.click()
        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys(input_phone)
        sleep(15)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        emailControl_alert =self.waitForElementVisible((By.CSS_SELECTOR,EMAILCONTROL_XPATH))
        assert emailControl_alert.text ==EMAILCONTROL_TEXT

# #Kullanıcının sözleşmeler sayfasını görüntüleyebilmesi
    def test_contractsWindow(self):
        emailrandom = generate_random_email()
        firstname = self.waitForElementVisible((By.NAME, FIRSTNAME_NAME))
        lastname = self.waitForElementVisible((By.NAME, LASTNAME_NAME))
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        password = self.waitForElementVisible((By.NAME, PASSWORD_NAME))
        password_again = self.waitForElementVisible((By.NAME, PASSWORDAGAIN_NAME))
        firstname.send_keys(input_firstname)
        lastname.send_keys(input_lastname)
        email.send_keys(emailrandom)
        password.send_keys(input_password)
        password_again.send_keys(input_passwordagain)
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        sign_up_button.click()
        contract_windows =self.waitForElementVisible((By.XPATH,CONTRACTWINDOWS_XPATH))
        assert contract_windows.text == CONTRACTWINDOWS_TEXT
        
    def test_contractsPermission(self):
        self.test_contractsWindow()
        self.driver.save_screenshot("images/buttonPasif.png")
        self.take_and_show_screenshot ("images/buttonPasif.png")
        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys(input_phone)
        sleep(15)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH)) 
        actions = ActionChains(self.driver)
        actions.move_to_element(continue_button).perform()
        self.driver.save_screenshot("images/buttonActive.png")
        self.take_and_show_screenshot ("images/buttonActive.png")
