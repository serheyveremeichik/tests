import pytest
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPageLocators:
    LOCATOR_USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    LOCATOR_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")


class LoginPage(BasePage):

    def enter_username(self, username):
        name_field = self.find_element(LoginPageLocators.LOCATOR_USERNAME)
        name_field.click()
        name_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find_element(LoginPageLocators.LOCATOR_PASSWORD)
        password_field.click()
        password_field.send_keys(password)

    def click_on_the_login_button(self):
        self.find_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON, time=2).click()
