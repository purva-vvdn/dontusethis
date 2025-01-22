
import re
import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators import home_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Edit:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def open_login_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button_premium'))).click()
        for attempt in range(3):
            try:
                self.driver.find_element(home_locators.enter_username_locator)
                print("Username field to locate.")
                break
            except Exception as e:
                print(f"Attempt {attempt + 1}: Username field not found. Retrying...")
                try:
                    self.driver.find_element(By.ID, 'button_premium').click()
                    print(f"Retrying click on 'button_premium' (Attempt {attempt + 1})...")
                    time.sleep(6)
                except Exception as retry_exception:
                    print(f"Retry click failed on attempt {attempt + 1}: {retry_exception}")



    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(home_locators.enter_username_locator)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(home_locators.enter_password_locator)).send_keys(password)

    def clicking_on_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(home_locators.click_on_login_locator)).click()
        time.sleep(2)