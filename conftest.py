from selenium import webdriver
from constants.globalConstants import *
import pytest

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(REGISTER_URL)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="class")
def setup_two(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(LOGIN_URL)
    request.cls.driver = driver
    yield
    driver.quit()


