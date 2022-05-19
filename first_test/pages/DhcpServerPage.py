from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage


class DhcpServerPageLocators:
    LOCATOR_DHCP_ON = (By.XPATH, "//span[@class='toggle-state toggle-state--on']")
    LOCATOR_DHCP_OFF = (By.XPATH, "//span[@class='toggle-state toggle-state--off']")
    LOCATOR_SAVE_BUTTON = (By.XPATH, "//button[@id='save-button'][@class='button-icon']")
    LOCATOR_DHCP_SERVER_FOR_NETZONE_2 = (By.XPATH, "//span[@class='toggle-slider']")
    LOCATOR_IP_RANGE_START = (
        By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-range-low__CONTROL']")
    LOCATOR_IP_RANGE_END = (
        By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-range-high__CONTROL']")
    LOCATOR_LOCAL_MASK = (By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-netmask__CONTROL']")
    LOCATOR_DEFAULT_GATEWAY = (
        By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-gateway__CONTROL']")
    LOCATOR_DNS_SERVER = (By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-dns__CONTROL']")
    LOCATOR_WINS_SERVER = (By.XPATH, "//input[@id='dhcp-server-page__dhcp-configuration__dhcp-server-wins__CONTROL']")
    LOCATOR_INVALID_IPV4_ADDRESS = (By.XPATH, "//div[text()='Invalid IPv4 address.']")
    LOCATOR_INVALID_IPV4_NETMASK = (By.XPATH, "//div[text()='Invalid IPv4 netmask (CIDR notation).']")
    LOCATOR_THE_CHANGES_WERE_SAVED = (By.XPATH, "//p[contains(text(),' The changes were saved successfully. ')]")


class DhcpServerPage(BasePage):

    def dhcp_for_netzone2_switch(self):
        dhcp_switch = self.find_element(DhcpServerPageLocators.LOCATOR_DHCP_SERVER_FOR_NETZONE_2, time=2)
        dhcp_switch.click()
        if self.find_element(DhcpServerPageLocators.LOCATOR_DHCP_ON, time=2).is_displayed():
            return "ON"
        elif self.find_element(DhcpServerPageLocators.LOCATOR_DHCP_OFF, time=2).is_displayed():
            return "OFF"

    def set_ip_range_start(self, start_ip):
        range_start = self.find_element(DhcpServerPageLocators.LOCATOR_IP_RANGE_START, time=2)
        range_start.click()
        range_start.send_keys(start_ip, Keys.TAB)

    def set_ip_range_end(self, end_ip):
        range_end = self.find_element(DhcpServerPageLocators.LOCATOR_IP_RANGE_END, time=2)
        range_end.click()
        range_end.send_keys(end_ip, Keys.TAB)

    def set_local_mask(self, mask):
        locale_mask = self.find_element(DhcpServerPageLocators.LOCATOR_LOCAL_MASK, time=2)
        locale_mask.click()
        locale_mask.send_keys(mask, Keys.TAB)

    def set_default_gateway(self, gateway):
        default_gateway = self.find_element(DhcpServerPageLocators.LOCATOR_DEFAULT_GATEWAY, time=2)
        default_gateway.click()
        default_gateway.send_keys(gateway, Keys.TAB)

    def set_dns_server(self, dns):
        dns_server = self.find_element(DhcpServerPageLocators.LOCATOR_DNS_SERVER, time=2)
        dns_server.click()
        dns_server.send_keys(dns, Keys.TAB)

    def set_wins_server(self, wins):
        wins_server = self.find_element(DhcpServerPageLocators.LOCATOR_WINS_SERVER, time=2)
        wins_server.click()
        wins_server.send_keys(wins, Keys.TAB)

    def get_ip_range_start(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_IP_RANGE_START, time=2).get_attribute('value')

    def get_ip_range_end(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_IP_RANGE_END, time=2).get_attribute('value')

    def get_local_mask(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_LOCAL_MASK, time=2).get_attribute('value')

    def get_def_gateway(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_DEFAULT_GATEWAY, time=2).get_attribute('value')

    def get_dns_server(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_DNS_SERVER, time=2).get_attribute('value')

    def get_wins_server(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_WINS_SERVER, time=2).get_attribute('value')

    def get_invalid_ipv4_address_message(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_INVALID_IPV4_ADDRESS, time=2).is_displayed()

    def get_invalid_ipv4_netmask_message(self):
        return self.find_element(DhcpServerPageLocators.LOCATOR_INVALID_IPV4_NETMASK, time=2).is_displayed()
