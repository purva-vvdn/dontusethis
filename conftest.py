import pytest
from selenium import webdriver
from pages.home_page import Edit
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = "https://insight.netgear.com/#/landingPage"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
