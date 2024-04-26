import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from constants.globalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.support.ui import Select



class Test_Register:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(REGISTER_URL)
        yield
        self.driver.quit()
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)) 
    def take_and_show_screenshot(self, image_path):
        screenshot = Image.open(image_path)
        screenshot.show()
    def readInvalidDataFromJSON():
        with open(r'data/data.json', 'r') as file: # ilk baştaki r ön ek # testlerde genelde r kullanılır yani dosyayı okuma modunda açar.
            data = json.load(file) #JSON veriler Python veri yapısına dönüşür.
        return [(user['firstnamex'], user['lastnamex'], user['emailx'], user['passwordx'], user['passwordagainx']) for user in data['invalid_login_users']] #tuple list oluşturur.
    def checkboxs(self):
        checkbox1=self.waitForElementVisible((By.XPATH,CHECKBOX1_XPATH))
        checkbox1.click()
        checkbox2=self.waitForElementVisible((By.XPATH,CHECKBOX2_XPATH))
        checkbox2.click()
        checkbox3=self.waitForElementVisible((By.XPATH,CHECKBOX3_XPATH))
        checkbox3.click()
        checkbox4=self.waitForElementVisible((By.XPATH,CHECKBOX4_XPATH))
        checkbox4.click()
    def registerForm(self):
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
    def phoneContracts(self):
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys(input_phone)
    def country_select(self):
           excelFile = openpyxl.load_workbook('data/countryid_list.xlsx')
           sheet = excelFile.active
           country_ids = [cell.value for cell in sheet['A'][1:]]  # İlk satırı atla (başlık)
           de_ids = [country_id for country_id in country_ids if country_id == 'TR']
           if not de_ids:
             print("TR değeri bulunamadı.")
             excelFile.close()
             return
           
           phone_country_field = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/label[4]/small/div/div/select")
           select = Select(phone_country_field)
           select.select_by_value(de_ids[0])






    # Kullanıcının kayıt olma işlemi
    def test_register(self):
        self.registerForm()
        self.checkboxs()
        self.phoneContracts()
        iframe = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,CAPTCHA_XPATH)))
        captcha.click()
        time.sleep(10)
        self.driver.switch_to.default_content()
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))       
        continue_button.click()
        wait_url = WAITREGISTER_URL
        WebDriverWait(self.driver, 10).until(EC.url_to_be(wait_url))
        alertMessage = self.waitForElementVisible((By.XPATH, REGISTERTEXT_XPATH))
        assert alertMessage.text == TRUEREGISTER_TEXT

    
    
    # Doldurulması zorunlu alanlarının boş bırakılma durumu
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
        sign_up_button = self.waitForElementVisible((By.XPATH, SIGNUPBUTTON_XPATH))
        assert not  sign_up_button.is_enabled(), EMPTY_FIELDS_TEXT      

    
    
    #  E-postanın geçersiz formatta girilmesi durumu       
    def test_wrongFormat_email(self):
        email = self.waitForElementVisible((By.NAME, EMAIL_NAME))
        email.send_keys(input_wronfFormat_email)
        wrongMail_alert=self.waitForElementVisible((By.XPATH,WRONG_EMAIL_ALERT_XPATH))
        assert wrongMail_alert.text ==WRONG_MAIL_TEXT     

    
    
    #  "Şifre" ve "Şifre Tekrar" bölümlerinin eşleşmediği durumlar  
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
        self.checkboxs()
        self.phoneContracts()
        time.sleep(10)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        passwordControl_alert=self.waitForElementVisible((By.CSS_SELECTOR,PASSWORDCONTROL_XPATH))
        assert passwordControl_alert.text ==PASSWORDCONTROL_TEXT


    
    # Kullanıcının sisteme kayıt olduğu e-posta adresinin sistemde mevcut olması
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
        self.checkboxs()
        self.phoneContracts()
        time.sleep(10)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        emailControl_alert =self.waitForElementVisible((By.CSS_SELECTOR,EMAILCONTROL_XPATH))
        assert emailControl_alert.text ==EMAILCONTROL_TEXT


    
    # Kullanıcının sözleşmeler sayfasını görüntüleyebilmesi
    def test_contractsWindow(self):
        self.registerForm()
        contract_windows =self.waitForElementVisible((By.XPATH,CONTRACTWINDOWS_XPATH))
        assert contract_windows.text == CONTRACTWINDOWS_TEXT


    
    #Kullanıcının kayıt olabilmesi için gereken sözleşmeleri onaylamadan devam edememesi durumu      
    def test_contractsPermission(self):
        self.test_contractsWindow()
        self.driver.save_screenshot("images/buttonPasif.png")
        self.take_and_show_screenshot ("images/buttonPasif.png")
        self.checkboxs()
        self.phoneContracts()
        time.sleep(10)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH)) 
        actions = ActionChains(self.driver)
        actions.move_to_element(continue_button).perform()
        try:
           button = self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))
           assert button is not None, "Button is visible"
           print("Button is visible")
        except Exception :
           print("Button is not visible")


    
    #Kullanıcının telefon numarasını belirlenen sınırdan az girmesi
    def test_phone_shortLeng(self):
       self.test_contractsWindow()
       self.checkboxs()
       phone_checkbox = self.waitForElementVisible((By.XPATH, PHONECHECK_XPATH))
       phone_checkbox.click()
       self.country_select()
       input_phone_box = self.waitForElementVisible((By.XPATH, PHONECHECK_XPATH))
       input_phone_box.send_keys("549 490 30 0")
       time.sleep(10)
       continue_button = self.waitForElementVisible((By.XPATH, CONTINUEBUTTON_XPATH))
       continue_button.click()
       warning_phoneL= self.waitForElementVisible((By.XPATH,PHONE_LONG_SHORT_ALERT_XPATH))
       assert warning_phoneL.text == PHONE_SHORT_LENGTH_TEXT


    
    #Kullanıcının telefon numarasını belirlenen sınırdan fazla girmesi
    def test_phone_longLeng(self):
       self.test_contractsWindow()
       self.checkboxs()
       phone_checkbox = self.waitForElementVisible((By.XPATH, PHONECHECK_XPATH))
       phone_checkbox.click()
       self.country_select()
       input_phone_box = self.waitForElementVisible((By.XPATH, PHONECHECK_XPATH))
       input_phone_box.send_keys("TR 549 490 30 049")
       time.sleep(10)
       continue_button = self.waitForElementVisible((By.XPATH, CONTINUEBUTTON_XPATH))
       continue_button.click()
       warning_phoneLongL= self.waitForElementVisible((By.XPATH,PHONE_LONG_SHORT_ALERT_XPATH))
       assert warning_phoneLongL.text == PHONE_LONG_LENGTH_TEXT


    
    #Kullanıcının girdiği telefon numarasının sistemde kayıtlı olması
    def test_registeredNumber(self):
        self.test_contractsWindow()
        self.checkboxs()
        phone_checkbox=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        phone_checkbox.click()
        input_phone_box=self.waitForElementVisible((By.XPATH,PHONECHECK_XPATH))
        input_phone_box.send_keys("549 490 30 04")
        iframe = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,CAPTCHA_XPATH)))
        captcha.click()
        self.driver.switch_to.default_content()
        time.sleep(10)
        continue_button =self.waitForElementVisible((By.XPATH,CONTINUEBUTTON_XPATH))      #BURASI KAYIT OL AŞAMASINDA KAYDOL BUTONUNA TIKLANILDAKTAN SONRA GELEN PENCERİNİN SONUNDAKİ DEVAM BUTONU
        continue_button.click()
        wait_url = WAITREGISTER_URL
        WebDriverWait(self.driver, 10).until(EC.url_to_be(wait_url))
        self.driver.save_screenshot("images/registeredNumber.png")
        self.take_and_show_screenshot("images/registeredNumber.png")
        assert False,REGISTER_NUMBER_TEXT 

    
    
    #Captcha doğrulamasının geçersiz olduğu durum
    def test_faildCaptcha(self):
        self.test_contractsWindow()
        self.checkboxs()
        self.phoneContracts()
        iframe = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,CAPTCHA_XPATH)))
        captcha.click()
        time.sleep(71)
        self.driver.switch_to.default_content()
        self.driver.save_screenshot("images/captchaWarning.png")
        self.take_and_show_screenshot ("images/captchaWarning.png")     
        
         
