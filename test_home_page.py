from pages.home_page import Edit
import pytest
from pages.home_page import home_locators


@pytest.mark.usefixtures("setup")
class TestEdit:
    def test_to_verify_the_two_step_verification(self):
        edit_driver = Edit(self.driver)
        edit_driver.open_login_page()
        edit_driver.enter_username('unique56@yopmail.com')
        edit_driver.enter_password('Sak@1421')
        edit_driver.clicking_on_sign_in()
