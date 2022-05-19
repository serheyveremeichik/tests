from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePageLocators:
    LOCATOR_NETWORK = (By.XPATH, "//a[@id='SUBMENU_LINK__network-page']")
    LOCATOR_NETWORK_SECURITY = (By.XPATH, "//a[@id='SUBMENU_LINK__network-security']")
    LOCATOR_DHCP_CHAPTER = (By.XPATH, "//a[text()='DHCP server ']")
    LOCATOR_FIREWALL_CHAPTER = (By.XPATH, "//a[text()='Firewall ']")


class HomePage(BasePage):

    def go_to_dhcp_server_tab(self):
        self.find_element(HomePageLocators.LOCATOR_NETWORK, time=2).click()
        self.find_element(HomePageLocators.LOCATOR_DHCP_CHAPTER, time=2).click()

    def go_to_firewall_tab(self):
        self.find_element(HomePageLocators.LOCATOR_NETWORK_SECURITY, time=2).click()
        self.find_element(HomePageLocators.LOCATOR_FIREWALL_CHAPTER, time=2).click()
