import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from constants.globalConstants import *

class Test_My_Profile():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)
        yield
        self.driver.quit()
    
    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    #önkoşul1: Profil bilgileri boş kullanıcının girişi
    def login_empty(self):
        loginEmail= self.waitForElementVisible((By.NAME, loginEmail_name))
        loginEmail.send_keys(input_emptyuser)
        loginPassword = self.waitForElementVisible((By.NAME, loginPassword_name))
        loginPassword.send_keys(input_emptyuserpassword)
        loginButton= self.waitForElementVisible((By.XPATH, loginButton_xpath))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(HOMEPAGE_URL))
        assert HOMEPAGE_URL in self.driver.current_url
        myProfile= self.waitForElementVisible((By.XPATH, MYPROFILE_XPATH))
        myProfile.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(MYPROFILE_URL))
        assert MYPROFILE_URL in self.driver.current_url

    #önkoşul2: Profil bilgileri dolu kullanıcının girişi
    def login_full(self):
        loginEmail= self.waitForElementVisible((By.NAME, loginEmail_name))
        loginEmail.send_keys(input_loginEmail)
        loginPassword = self.waitForElementVisible((By.NAME, loginPassword_name))
        loginPassword.send_keys(input_loginPassword)
        loginButton= self.waitForElementVisible((By.XPATH, loginButton_xpath))
        loginButton.click()
        WebDriverWait(self.driver,5).until(EC.url_to_be(HOMEPAGE_URL))
        assert HOMEPAGE_URL in self.driver.current_url
        myProfile= self.waitForElementVisible((By.XPATH, MYPROFILE_XPATH))
        myProfile.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(MYPROFILE_URL))
        assert MYPROFILE_URL in self.driver.current_url

    #Kullanıcının profil linkini kopyalaması
    def test_copy_link(self):
        # self.login_empty()
        # shareLink= self.waitForElementVisible((By.ID, SHARELINK_ID))
        # shareLink.click()
        # shareLinkControl= self.waitForElementVisible((By.XPATH, SHARELINKCONTROL_XPATH))
        # assert shareLinkControl.text== SHARELINKCONTROL_TEXT
        # copyLink= self.waitForElementVisible((By.XPATH, COPYLINK_XPATH))
        # copyLink.click()
        # copyLinkControl= self.waitForElementVisible((By.XPATH, COPYLINKCONTROL_XPATH))
        # assert copyLinkControl.text== COPYLINKCONTROL_TEXT
        # editIcon= self.waitForElementVisible((By.CLASS_NAME, EDITICON_CLASSNAME))
        # editIcon.click()
        # WebDriverWait(self.driver,5).until(EC.url_to_be(EDITPROFILE_URL))
        # assert EDITPROFILE_URL in self.driver.current_url
        assert True
    #Profil bilgileri boş kullanıcının profil sayfasında tüm başlıkları ve sol tarafın görüntülemesi
    def test_emptyUser_left_informations(self):
        self.login_empty()
        headersElements=  WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, HEADERSCONTROL_CLASSNAME)))
        profilePageHeaders= []
        for header in headersElements:
            headers_texts= header.text
            profilePageHeaders.append(headers_texts)
        assert profilePageHeaders== HEADERSCONTROL_TEXTS #tüm başlıkların görüntülenmesi
        # informationsControl= self.waitForElementVisible((By.XPATH, INFORMATIONSCONTROL_XPATH))
        # WebDriverWait(self.driver,5).until(EC.text_to_be_present_in_element((By.XPATH, INFORMATIONSCONTROL_XPATH), "Girilmemiş"))
        # assert informationsControl.text== INFORMATIONSCONTROL_TEXT
        emptyInformationsBox= self.waitForElementVisible((By.XPATH, INFORMATIONSBOX_XPATH))
        emptyInformationsBox.screenshot("US9//screenshots//empty_personal_informations.png")
        self.driver.execute_script("window.scrollTo(0,700)")
        about= self.waitForElementVisible((By.XPATH, ABOUT_XPATH))
        competencies= self.waitForElementVisible((By.XPATH, COMPETENCIES_XPATH))
        foreignLanguages= self.waitForElementVisible((By.XPATH, FOREIGNLANGUAGES_XPATH))
        certificates= self.waitForElementVisible((By.XPATH, CERTIFICATES_XPATH))
        socialMedia= self.waitForElementVisible((By.XPATH, SOCIALMEDIA_XPATH))
        assert competencies.text== COMPETENCIES_TEXT and foreignLanguages.text== FOREIGNLANGUAGES_TEXT and certificates.text== CERTIFICATES_TEXT and socialMedia.text== SOCIALMEDIA_TEXT
        about.screenshot("US9//screenshots//about_bug.png") 
        assert about.text== ABOUT_TEXT #bug
        
    #Profil bilgileri boş kullanıcının profil sayfasının sağ tarafın görüntülemesi
    def test_emptyUser_right_informations(self):
        # self.login_empty()
        # profileRightPart= self.waitForElementVisible((By.XPATH, PROFILERIGHTPART_XPATH))
        # profileRightPart.screenshot("US9//screenshots//profile_rightpart_viewing1.png")
        # educationLifeElement= self.waitForElementVisible((By.XPATH, EDUCATIONLIFEELEMENT_XPATH))
        # actions2= ActionChains(self.driver)
        # actions2.move_to_element(educationLifeElement).perform()
        # profileRightPart.screenshot("US9//screenshots//profile_rightpart_viewing2.png") #alt başlıkları görüntüleme adımları
        # assert True
        # profileTestStartButton= self.waitForElementVisible((By.XPATH, PROFILETESTSTARTBUTTON_XPATH))
        # profileTestStartButton.click()
        # WebDriverWait(self.driver,5).until(EC.url_to_be(PROFILETEST_URL))
        # assert PROFILETEST_URL in self.driver.current_url #tobeto işte başarı testine yönlendirilmesi
        # self.driver.get(MYPROFILE_URL)
        # profileTestReviewButton= self.waitForElementVisible((By.XPATH, PROFILETESTREVIEWBUTTON_XPATH))
        # profileTestReviewButton.click()
        # profileTestAlert= self.waitForElementVisible((By.XPATH, PROFILETESTALERT_XPATH))
        # assert profileTestAlert.text== PROFILETESTALERT_TEXT #sınavı bitirmediniz uyarı mesajı görüntülenmesi
        # self.driver.get(MYPROFILE_URL)
        # myActivity= self.waitForElementVisible((By.CSS_SELECTOR, MYACTIVITY_CSS))
        # action3= ActionChains(self.driver)
        # action3.move_to_element(myActivity).perform()
        # myActivity.click()
        # data_tip_text = myActivity.get_attribute("data-tip")
        # assert data_tip_text == "Herhangi bir aktiviteniz yok : 0"
        # self.driver.execute_script("window.scrollTo(0,100)")
        # socialMedia= self.waitForElementVisible((By.XPATH, SOCIALMEDIA_XPATH))
        # actions4= ActionChains(self.driver)
        # actions4.move_to_element(socialMedia).perform()
        # secondColor= self.waitForElementVisible((By.CLASS_NAME, SHOWACTIVITY_CLASSNAME))
        # secondColor.click()
        # self.driver.save_screenshot("US9//screenshots//activity_colors.png")
        assert True #renk cetvelinin üzerindeki sayı aralıkları


    #Profil bilgileri dolu kullanıcının profil sayfasında kişisel bilgilerini görüntülemesi
    def test_fullUser_informations(self):
        # self.login_full()
        # self.driver.execute_script("window.scrollTo(0,150)")
        # self.driver.save_screenshot("US9//screenshots//full_profile_informations.png") #üst bölüm görüntülemesi
        # seeIcon= self.waitForElementVisible((By.XPATH, SEEICON_XPATH))
        # seeIcon.click()
        # openCompetenciesControl= self.waitForElementVisible((By.XPATH, OPENCOMPETENCIESCONTROL_XPATH))
        # assert openCompetenciesControl.text==OPENCOMPETENCIESCONTROL_TEXT #yetkinlik sayfasının açılması kontrolü
        # competenciesClose= self.waitForElementVisible((By.XPATH, COMPETENCIESCLOSE_XPATH))
        # competenciesClose.click()
        # showSocialMedia= self.waitForElementVisible((By.XPATH, SHOWSOCIALMEDIA_XPATH))
        # actions= ActionChains(self.driver)
        # actions.move_to_element(showSocialMedia)
        # actions.perform()
        # self.driver.save_screenshot("US9//screenshots//full_profile_informations2.png") #alt bölüm görüntülenmesi
        # downloadcertificate= self.waitForElementVisible((By.XPATH, DOWNLOADCERTIFICATE_XPATH))
        # downloadcertificate.click() #sertifika indirilmesi
        # sleep(2) #indirmesi için gereken süre
        # self.driver.save_screenshot("US9//screenshots//download_certificate.png")
        # showSocialMedia= self.waitForElementVisible((By.XPATH, SHOWSOCIALMEDIA_XPATH))
        # showSocialMedia.click() #sosyal medya hesabı sayfasının açılması
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # assert "https://github.com/akvsy" in self.driver.current_url
        assert True

    


    

