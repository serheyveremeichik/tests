from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageLocators:
    LOCATOR_SAVE_BUTTON = [By.XPATH, "//button[@id='save-button'][@class='button-icon']"]
    LOCATOR_THE_CHANGES_WERE_SAVED = (By.XPATH, "//p[contains(text(),' The changes were saved successfully. ')]")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://192.168.1.1"

    def find_element(self, locator, time=3):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return element

    def go_to_ui(self):
        return self.driver.get(self.base_url)

    def click_save(self):
        save_button = self.find_element(BasePageLocators.LOCATOR_SAVE_BUTTON, time=2)
        save_button.is_displayed()
        save_button.click()

    def delete_value(self, locator):
        field = self.find_element(locator, time=2)
        field.click()
        field.send_keys(Keys.BACKSPACE, Keys.TAB)

    def wait_saved_changes(self):
        while True:
            try:
                self.find_element(BasePageLocators.LOCATOR_THE_CHANGES_WERE_SAVED, time=2).is_displayed()
                break
            except NoSuchElementException:
                continue
