import requests
import json
import pytest
from API.API_constants import *

class Test_API():
    def valid_login(self):

        with open('data/API_data.json') as json_file:
            self.json_payload= json.load(json_file)
        
        header= {'Content-Type': 'application/json'}
        response= requests.post(url= (BASE_URL+LOGIN_ENDPOINT), headers=header, json=self.json_payload["users"]["valid_user"])
        
        if response.status_code == 200:
            print("Başarıyla giriş yaptın!")
            self.token= response.json()['jwt']
            return self.token
        else:
            print(f"Giriş başarısız! Hata kodu {response.status_code}")

    def test_invalid_password(self):
        self.valid_login()
        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}
        response= requests.post(url=(BASE_URL+CHANGE_PASSWORD_ENDPOINT), headers=header, json=self.json_payload["passwords"]["invalid_password"])
        
        if response.status_code == 400:
            invalid_error_message = response.json()["error"]["message"]
            assert invalid_error_message == INVALID_PASSWORD_ERROR_MESSAGE #yeni sifrenin mevcut sifre ile ayni olmasi
            
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False

    def test_short_password(self):
        self.valid_login()

        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

        response= requests.post(url=(BASE_URL+CHANGE_PASSWORD_ENDPOINT), headers=header, json=self.json_payload["passwords"]["short_password"])
        
        if response.status_code == 400:
            short_error_message = response.json()["error"]["message"]
            assert short_error_message == SHORT_PASSWORD_ERROR_MESSAGE
             
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False

    def test_unmatched_password(self):
        self.valid_login()
    
        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

        response= requests.post(url=(BASE_URL+CHANGE_PASSWORD_ENDPOINT), headers=header, json=self.json_payload["passwords"]["unmatched_password"])
        
        if response.status_code == 400:
            unmatched_error_message = response.json()["error"]["message"]
            assert unmatched_error_message ==  UNMATCHED_PASSWORD_ERROR_MESSAGE
             
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False


    def test_current_password(self):
        self.valid_login()
              
        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

        response= requests.post(url=(BASE_URL+CHANGE_PASSWORD_ENDPOINT), headers=header, json=self.json_payload["passwords"]["old_password"])
        
        if response.status_code == 400:
            current_error_message = response.json()["error"]["message"]
            assert current_error_message == CURRENT_PASSWORD_ERROR_MESSAGE
             
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False

    def test_empty_password(self):
        self.valid_login()
        
        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

        response= requests.post(url=BASE_URL+CHANGE_PASSWORD_ENDPOINT, headers=header, json=self.json_payload["passwords"]["empty_password"])
        
        if response.status_code == 400:
            empty_error_message = response.json()["error"]["message"]
            assert empty_error_message == EMPTY_PASSWORD_ERROR_MESSAGE
             
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False
    
    def test_remove_account(self):
        self.valid_login()
        
        header= {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'}

        response= requests.post(url=BASE_URL+REMOVE_ACCOUNT_ENDPOINT, headers=header)
        
        if response.status_code == 200:
            assert True
             
        else:
            print(f"Hata kodu {response.status_code}")
            print(f"Hata mesajı: {response.text}")
            assert False

