from selenium import webdriver
from selenium.webdriver.common.by import By
       from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Dynamic wait (adjustable)

    def wait_until_element_visible(self, locator):
        """Wait until the element is visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Click on the element identified by the locator"""
        element = self.wait_until_element_visible(locator)
        element.click()

    def send_keys(self, locator, value):
        """Send keys to the element identified by the locator"""
        element = self.wait_until_element_visible(locator)
        element.clear()  # Clear any pre-existing text before entering new text
        element.send_keys(value)

    def perform_action_chain(self, locator, action='click'):
        """Perform Action Chain actions like hover, click, etc."""
        element = self.wait_until_element_visible(locator)
        action_chain = ActionChains(self.driver)

        if action == 'click':
            action_chain.click(element).perform()
        elif action == 'double_click':
            action_chain.double_click(element).perform()
        elif action == 'hover':
            action_chain.move_to_element(element).perform()
        elif action == 'right_click':
            action_chain.context_click(element).perform()
        elif action == 'drag_and_drop':
            # Example of drag and drop action
            source = element
            target = self.wait_until_element_visible((By.XPATH, '//div[@id="target"]'))  # Example target element
            action_chain.drag_and_drop(source, target).perform()
        elif action == 'key_press':
            action_chain.send_keys(Keys.ENTER).perform()
        else:
            print("Action not supported.")

    def scroll_to_element(self, locator):
        """Scroll to the element to ensure it's in view before interacting"""
        element = self.wait_until_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def clear_and_send_keys(self, locator, value):
        """Clear and send new keys"""
        element = self.wait_until_element_visible(locator)
        element.clear()
        element.send_keys(value)

    # Handling Multiple Windows/Popups
    def switch_to_window(self, window_index):
        """Switch to a window by its index"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index])

    def switch_to_new_window(self):
        """Switch to the last opened window"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        """Close the current window"""
        self.driver.close()

    def switch_to_parent_window(self):
        """Switch to the parent window"""
        parent_window = self.driver.window_handles[0]
        self.driver.switch_to.window(parent_window)

    # Handling Alerts
    def accept_alert(self):
        """Accept a JavaScript alert"""
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        """Dismiss a JavaScript alert"""
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        """Get text from a JavaScript alert"""
        alert = self.driver.switch_to.alert
        return alert.text

    def send_keys_to_alert(self, value):
        """Send text to a JavaScript prompt alert"""
        alert = self.driver.switch_to.alert
        alert.send_keys(value)
        alert.accept()

    # Special Methods
    def get_current_url(self):
        """Get the current page URL"""
        return self.driver.current_url

    def get_page_title(self):
        """Get the current page title"""
        return self.driver.title

    def take_screenshot(self, file_name):
        """Take a screenshot of the current page"""
        self.driver.save_screenshot(file_name)

    def get_element_text(self, locator):
        """Get the text of an element"""
        element = self.wait_until_element_visible(locator)
        return element.text

    def wait_for_element_to_be_clickable(self, locator):
        """Wait until the element is clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Implicit Wait
    def set_implicit_wait(self, seconds):
        """Set implicit wait for the driver"""
        self.driver.implicitly_wait(seconds)

    # Page Load Timeout
    def set_page_load_timeout(self, seconds):
        """Set page load timeout"""
        self.driver.set_page_load_timeout(seconds)

    # Script Timeout
    def set_script_timeout(self, seconds):
        """Set script timeout"""
        self.driver.set_script_timeout(seconds)

    # Window Handling Methods
    def maximize_window(self):
        """Maximize the browser window"""
        self.driver.maximize_window()

    def fullscreen_window(self):
        """Set the window to fullscreen"""
        self.driver.fullscreen_window()

    def set_window_size(self, width, height):
        """Set the window size"""
        self.driver.set_window_size(width, height)

    def get_window_size(self):
        """Get the window size"""
        return self.driver.get_window_size()

    def get_window_handle(self):
        """Get the current window handle"""
        return self.driver.current_window_handle

    def set_window_position(self, x, y):
        """Set the window position"""
        self.driver.set_window_position(x, y)

    def get_window_position(self):
        """Get the window position"""
        return self.driver.get_window_position()

    # Locator Strategies
    def find_element_by_id(self, element_id):
        """Find element by ID"""
        return self.driver.find_element(By.ID, element_id)

    def find_element_by_name(self, element_name):
        """Find element by Name"""
        return self.driver.find_element(By.NAME, element_name)

    def find_element_by_class_name(self, class_name):
        """Find element by Class Name"""
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def find_element_by_tag_name(self, tag_name):
        """Find element by Tag Name"""
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def find_element_by_link_text(self, link_text):
        """Find element by Link Text"""
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def find_element_by_partial_link_text(self, partial_link_text):
        """Find element by Partial Link Text"""
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    def find_element_by_css_selector(self, css_selector):
        """Find element by CSS Selector"""
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_element_by_xpath(self, xpath):
        """Find element by XPath"""
        return self.driver.find_element(By.XPATH, xpath)

    # Example of multiple locators
    def find_element(self, locator, strategy='xpath'):
        """Find element by various strategies"""
        if strategy == 'id':
            return self.driver.find_element(By.ID, locator)
        elif strategy == 'name':
            return self.driver.find_element(By.NAME, locator)
        elif strategy == 'class':
            return self.driver.find_element(By.CLASS_NAME, locator)
        elif strategy == 'tag':
            return self.driver.find_element(By.TAG_NAME, locator)
        elif strategy == 'link_text':
            return self.driver.find_element(By.LINK_TEXT, locator)
        elif strategy == 'partial_link_text':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
        elif strategy == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        elif strategy == 'xpath':
            return self.driver.find_element(By.XPATH, locator)
        else:
            raise ValueError("Invalid locator strategy")


if __name__ == "__main__":
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Open a website
    driver.get("https://www.example.com")

    # Create an instance of SeleniumActions
    actions = SeleniumActions(driver)

    # Set various timeouts
    actions.set_implicit_wait(10)
    actions.set_page_load_timeout(30)
    actions.set_script_timeout(20)

    # Window handling examples
    actions.maximize_window()
    actions.set_window_size(1024, 768)
    print("Window size:", actions.get_window_size())
    actions.set_window_position(100, 200)
    print("Window position:", actions.get_window_position())

    # Handle an alert
    actions.accept_alert()  # Assuming there is an alert to accept
    actions.dismiss_alert()  # Dismiss if an alert exists

    # Example of sending keys to an input field
    actions.send_keys((By.ID, "username"), "testuser")

    # Find an element by different locators
    actions.find_element_by_id("submit_button").click()

    # Wait before closing the browser
    time.sleep(3)
    driver.quit()
