import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import exception
from selenium.webdriver.common.by import By



class BasePage:
    default_timeout = 30
    default_delay = 1

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.delay = self.default_delay
        if timeout:
            self.default_timeout = timeout
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def get_web_element(self, item):
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_web_elements(self, item):
        try:
            element = self.wait.until(expected_conditions.presence_of_all_elements_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_visible_element(self, item):
        try:
            element = self.wait.until(expected_conditions.visibility_of_element_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def check_invisible_element(self, item):
        try:
            self.wait.until(expected_conditions.invisibility_of_element_located(item))
            return True
        except TimeoutException:
            return False

    def get_visible_elements(self, item):
        try:
            elements = self.wait.until(expected_conditions.visibility_of_any_elements_located(item))
            return elements
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def click(self, item):
        try:
            element = self.wait.until(expected_conditions.element_to_be_clickable(item))
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)
        element.click()
        return element

    def get_first_visible_element(self, item):
        elements = self.get_visible_elements(item)
        if not elements:
            raise exception.ElementNotFoundException(item)
        return elements[0]

    def get_alert(self):
        return self.wait.until(expected_conditions.alert_is_present())

    def delay_test(self, delay=None):
        time.sleep(delay or self.delay)

    def text_present_in_element(self, item, text):
        try:
            element = self.wait.until(expected_conditions.text_to_be_present_in_element(item, text))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def amount_of_elements(self, item):
        try:
            element = self.wait.until(expected_conditions.presence_of_all_elements_located(item))
            return len(element)
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_element_with_text(self, text):
        item = By.XPATH, '//*[text() = "{}"]'.format(text)
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_elements_with_text(self, text):
        item = 'By.Xpath', '//*[text() = "{}"]'.format(text)
        try:
            element = self.wait.until(expected_conditions.presence_of_all_elements_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_element_contain_text(self, text):
        item = 'By.Xpath', '//*[contains(text(), "{}")]'.format(text)
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

    def get_elements_contains_text(self, text):
        item = By.XPATH, '//*[contains(text(), "{}")]'.format(text)
        try:
            element = self.wait.until(expected_conditions.presence_of_all_elements_located(item))
            return element
        except TimeoutException as e:
            raise exception.ElementNotFoundException(item, e)

