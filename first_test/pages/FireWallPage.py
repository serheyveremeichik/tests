import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage


class FirewallPageLocators:
    LOCATOR_FIREWALL_RULES = (By.XPATH, "//a[contains(text(),' Rules ')]")
    LOCATOR_NET_ZONE1_TO_2_TAB = (By.XPATH, "//label[contains(text(),'Net zone 1 → Net zone 2')]")
    LOCATOR_NET_ZONE2_TO_1_TAB = (By.XPATH, "//label[contains(text(),'Net zone 2 → Net zone 1')]")
    LOCATOR_ADD_ROW_BUTTON = (By.XPATH, "//button[contains(text(),' Add row ')]")
    LOCATOR_NET_ZONE1_TO_2_ENABLE = (By.XPATH, "//h2[contains(text(), 'Net zone 1 → Net zone 2')]")
    LOCATOR_NET_ZONE2_TO_1_ENABLE = (By.XPATH, "//h2[contains(text(), 'Net zone 2 → Net zone 1')]")
    LOCATOR_FROM_IP_NETWORK = (By.XPATH, "(//input[@class='form-control__input'])[1]")
    LOCATOR_TO_IP_NETWORK = (By.XPATH, "(//input[@class='form-control__input'])[2]")
    LOCATOR_COMMENT = (By.XPATH, "(//input[@class='form-control__input'])[3]")
    LOCATOR_CHECKBOX_SELECT_ALL = (By.XPATH, "//label[text()='Select All']/preceding-sibling::*")
    LOCATOR_CHECKBOX_LOG = "(//div[@class='col log']//input[@type='checkbox'])"
    LOCATOR_DELETE_ROW_BUTTON = (By.XPATH, "(//div[@class='col delete-column']/button)[last()]")
    LOCATOR_PLUS_ROW_BUTTON = "(//div[@class='col insert-icon']/button)"
    LOCATOR_LAST_ROW = (By.XPATH, "(//span[@class='sequence id-column'])[last()]")
    LOCATOR_CLEAR_SELECTION_BUTTON = (By.XPATH, "//button[text()=' Clear selection ']")
    LOCATOR_NUM_ROWS_SELECTED = (By.XPATH, "//div[@data-testid='tableSelectedBar']/p")
    LOCATOR_DELETE_ALL_ROWS_BUTTON = (By.XPATH, "//button[text()=' Delete ']")
    LOCATOR_TO_PORT = (By.XPATH, "")
    LOCATOR_SELECT_PROTOCOL = (By.XPATH, "//div[contains(@id,'protocol')]//div[@role='button']")
    LOCATOR_PROTOCOL_ALL = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='All']")
    LOCATOR_PROTOCOL_TCP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='TCP']")
    LOCATOR_PROTOCOL_UDP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='UDP']")
    LOCATOR_PROTOCOL_ICMP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='ICMP']")
    LOCATOR_PROTOCOL_GRE = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='GRE']")
    LOCATOR_PROTOCOL_ESP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='ESP']")
    LOCATOR_ACTUAL_PROTOCOL = (By.XPATH, "//div[contains(@id,'protocol')]//div[contains(@class,'selection--comma')]")
    LOCATOR_INPUT_TO_PORT = (By.XPATH, "//div[contains(@id,'port')]//input[@type='text']")
    LOCATOR_ACTUAL_PORT = (By.XPATH, "//div[contains(@id,'dst_port')]//input[@type='hidden']")
    LOCATOR_SELECT_ACTION = (By.XPATH, "//div[contains(@id,'verdict')]//div[@role='button']")
    LOCATOR_ACTUAL_ACTION = (By.XPATH, "//div[contains(@id,'verdict')]//input[@type='hidden']")
    LOCATOR_ACTION_ACCEPT = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Accept']")
    LOCATOR_ACTION_DROP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Drop']")
    LOCATOR_ACTION_REJECT = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Reject']")


class FirewallRulesPage(BasePage):
    def click_on_rules_tab(self):
        return self.find_element(FirewallPageLocators.LOCATOR_FIREWALL_RULES, time=2).click()

    def click_on_net_zone1_to_2_tab(self):
        self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE1_TO_2_TAB, time=2).click()

    def click_on_net_zone2_to_1_tab(self):
        self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE2_TO_1_TAB, time=2).click()

    def click_on_add_row_button(self):
        self.find_element(FirewallPageLocators.LOCATOR_ADD_ROW_BUTTON, time=2).click()

    def set_from_ip_network_value(self, ip_address):
        from_ip_field = self.find_element(FirewallPageLocators.LOCATOR_FROM_IP_NETWORK, time=2)
        from_ip_field.click()
        from_ip_field.send_keys(ip_address, Keys.TAB)

    def set_to_ip_network_value(self, ip_address):
        to_ip_field = self.find_element(FirewallPageLocators.LOCATOR_TO_IP_NETWORK, time=2)
        to_ip_field.click()
        to_ip_field.send_keys(ip_address, Keys.TAB)

    def set_comment_text(self, comment_text):
        comment = self.find_element(FirewallPageLocators.LOCATOR_COMMENT, time=2)
        comment.click()
        comment.send_keys(comment_text, Keys.TAB)

    def get_from_ip_network_value(self):
        return self.find_element(FirewallPageLocators.LOCATOR_FROM_IP_NETWORK, time=2).get_attribute('value')

    def get_to_ip_network_value(self):
        return self.find_element(FirewallPageLocators.LOCATOR_TO_IP_NETWORK, time=2).get_attribute('value')

    def get_comment_text(self):
        return self.find_element(FirewallPageLocators.LOCATOR_COMMENT, time=2).get_attribute('value')

    def click_select_all_checkbox(self):
        self.find_element(FirewallPageLocators.LOCATOR_CHECKBOX_SELECT_ALL, time=2).click()

    def click_log_checkbox(self, num_checkbox=1):
        element_locator = FirewallPageLocators.LOCATOR_CHECKBOX_LOG + "[" + str(num_checkbox) + "]"
        self.find_element((By.XPATH, element_locator), time=2).click()

    def click_delete_row_button(self, num_of_rows=1):
        i = num_of_rows
        while i > 0:
            element = self.find_element(FirewallPageLocators.LOCATOR_DELETE_ROW_BUTTON, time=2)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            element.click()
            i -= 1

    def click_plus_line_button(self, num_of_rows=1):
        i = 1
        while i <= num_of_rows:
            element_xpath = FirewallPageLocators.LOCATOR_PLUS_ROW_BUTTON + "[" + str(i) + "]"
            element = self.find_element((By.XPATH, element_xpath), time=2)
            element.is_displayed()
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            element.click()
            i += 1

    def get_num_of_rows(self):
        return self.find_element(FirewallPageLocators.LOCATOR_LAST_ROW, time=2).get_attribute("textContent")

    def get_num_rows_selected(self):
        return self.find_element(FirewallPageLocators.LOCATOR_NUM_ROWS_SELECTED, time=2).get_attribute("textContent")

    def click_clear_selection_button(self):
        return self.find_element(FirewallPageLocators.LOCATOR_CLEAR_SELECTION_BUTTON, time=2).click()

    def click_delete_all_rows_button(self):
        return self.find_element(FirewallPageLocators.LOCATOR_DELETE_ALL_ROWS_BUTTON, time=2).click()

    def click_input_protocol_field(self):
        return self.find_element(FirewallPageLocators.LOCATOR_SELECT_PROTOCOL, time=2).click()

    def set_port_value(self, num_of_port):
        to_port = self.find_element(FirewallPageLocators.LOCATOR_INPUT_TO_PORT, time=2)
        to_port.click()
        time.sleep(0.5)
        to_port.send_keys(num_of_port, Keys.TAB)

    def set_protocol(self, protocol):
        self.find_element(FirewallPageLocators.LOCATOR_SELECT_PROTOCOL, time=2).click()
        time.sleep(0.5)
        if protocol == "All":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_ALL, time=2).click()
        elif protocol == "TCP":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_TCP, time=2).click()
        elif protocol == "UDP":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_UDP, time=2).click()
        elif protocol == "ICMP":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_ICMP, time=2).click()
        elif protocol == "GRE":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_GRE, time=2).click()
        elif protocol == "ESP":
            self.find_element(FirewallPageLocators.LOCATOR_PROTOCOL_ESP, time=2).click()

    def get_actual_protocol(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_PROTOCOL, time=2).get_attribute("textContent")

    def get_actual_port(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_PORT, time=2).get_attribute("value")

    def set_action(self, action):
        self.find_element(FirewallPageLocators.LOCATOR_SELECT_ACTION, time=2).click()
        time.sleep(0.5)
        if action == "ACCEPT":
            self.find_element(FirewallPageLocators.LOCATOR_ACTION_ACCEPT, time=2).click()
        elif action == "REJECT":
            self.find_element(FirewallPageLocators.LOCATOR_ACTION_REJECT, time=2).click()
        elif action == "DROP":
            self.find_element(FirewallPageLocators.LOCATOR_ACTION_DROP, time=2).click()

    def get_actual_action(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_ACTION, time=2).get_attribute("value")




