from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage


class FirewallPageLocators:
    LOCATOR_FIREWALL_RULES = (By.XPATH, "//a[contains(text(),' Rules ')]")
    LOCATOR_NET_ZONE1_TO_2_TAB = (By.XPATH, "//div[@data-testid='buttonOne']")
    LOCATOR_NET_ZONE2_TO_1_TAB = (By.XPATH, "//div[@data-testid='buttonTwo']")
    LOCATOR_NET_ZONE1_TO_2_SELECTED = (By.XPATH, "//input[@id='one'][@disabled='disabled']")
    LOCATOR_NET_ZONE2_TO_1_SELECTED = (By.XPATH, "//input[@id='two'][@disabled='disabled']")
    LOCATOR_ADD_ROW_BUTTON = (By.XPATH, "//button[contains(text(),' Add row ')]")
    LOCATOR_FROM_IP_NETWORK = (By.XPATH, "(//input[@class='form-control__input'])[1]")
    LOCATOR_TO_IP_NETWORK = (By.XPATH, "(//input[@class='form-control__input'])[2]")
    LOCATOR_COMMENT = (By.XPATH, "(//input[@class='form-control__input'])[3]")
    LOCATOR_CHECKBOX_SELECT_ALL = (By.XPATH, "//label[text()='Select All']/preceding-sibling::*")
    LOCATOR_CHECKBOX_LOG = "(//div[@class='col log']//input[@type='checkbox'])"
    LOCATOR_DELETE_ROW_BUTTON = (By.XPATH, "//div[@class='col delete-column']//button[@class='delete hovered-row']")
    LOCATOR_PLUS_ROW_BUTTON = "(//div[@class='col insert-icon']/button)"
    LOCATOR_LAST_ROW = (By.XPATH, "(//span[@class='sequence id-column'])[last()]")
    LOCATOR_CLEAR_SELECTION_BUTTON = (By.XPATH, "//button[text()=' Clear selection ']")
    LOCATOR_NUM_ROWS_SELECTED = (By.XPATH, "//div[@data-testid='tableSelectedBar']/p")
    LOCATOR_DELETE_ALL_ROWS_BUTTON = (By.XPATH, "//button[text()=' Delete ']")
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
    LOCATOR_ARROW_UP_ELEMENT = (By.XPATH, "//div[contains(@id,'dst_port')]//div[@class='v-input__icon "
                                          "v-input__icon--append']")
    LOCATOR_SELECT_ACTION = (By.XPATH, "//div[contains(@id,'verdict')]//div[@role='button']")
    LOCATOR_ACTUAL_ACTION = (By.XPATH, "//div[contains(@id,'verdict')]//input[@type='hidden']")
    LOCATOR_ACTION_ACCEPT = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Accept']")
    LOCATOR_ACTION_DROP = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Drop']")
    LOCATOR_ACTION_REJECT = (By.XPATH, "//div[contains(@class,'v-menu__content theme')]//div[text()='Reject']")
    LOCATOR_DUPLICATE_ENTRIES_MESSAGE = (By.XPATH, "//div[@class='duplicated-rows-warning']")
    LOCATOR_DELETE_DUPLICATE_BUTTON = (By.XPATH, "//button[@class='duplicated-rows-button']")
    LOCATOR_ROW = "//div[@data-index="
    LOCATOR_NET_ZONE_TO_NET_ZONE_LABEL = (By.XPATH, "//div[@is-visible='true']//h2[@class='heading']")

    LOCATOR_FROM_IP_NETWORK_INVALID_MESSAGE = (By.XPATH, "(//div[text()='Invalid IPv4 address or network (CIDR "
                                                         "notation).'])[1]")
    LOCATOR_TO_IP_NETWORK_INVALID_MESSAGE = (By.XPATH, "(//div[text()='Invalid IPv4 address or network (CIDR "
                                                       "notation).'])[2]")
    LOCATOR_PROTOCOL_ERROR_MESSAGE = (By.XPATH, "//div[text()='Allowed port values: 1 … 65535, port range with "
                                                "delimiter ‘:’, or ‘All’']")


class FirewallRulesPage(BasePage):
    def click_on_rules_tab(self):
        self.find_element(FirewallPageLocators.LOCATOR_FIREWALL_RULES, time=2).click()

    def click_on_net_zone1_to_2_tab(self):
        self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE1_TO_2_TAB, time=2).click()

    def click_on_net_zone2_to_1_tab(self):
        self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE2_TO_1_TAB, time=2).click()

    def click_on_add_row_button(self):
        self.find_element(FirewallPageLocators.LOCATOR_ADD_ROW_BUTTON, time=2).click()

    def set_from_ip_network_value(self, ip_address):
        from_ip_field = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_FROM_IP_NETWORK))
        from_ip_field.click()
        from_ip_field.send_keys(ip_address, Keys.TAB)

    def set_to_ip_network_value(self, ip_address):
        to_ip_field = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_TO_IP_NETWORK))
        to_ip_field.click()
        to_ip_field.send_keys(ip_address, Keys.TAB)

    def set_comment_text(self, comment_text):
        comment = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_COMMENT))
        comment.click()
        comment.send_keys(comment_text, Keys.TAB)

    def get_from_ip_network_value(self):
        return WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_FROM_IP_NETWORK)).get_attribute('value')

    def get_to_ip_network_value(self):
        return WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_TO_IP_NETWORK)).get_attribute('value')

    def get_comment_text(self):
        return WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_COMMENT)).get_attribute('value')

    def click_select_all_checkbox(self):
        element = self.find_element(FirewallPageLocators.LOCATOR_CHECKBOX_SELECT_ALL, time=2)
        element.click()
        if element.is_selected():
            return True
        else:
            return False

    def click_log_checkbox(self, num_checkbox=1):
        element_locator = FirewallPageLocators.LOCATOR_CHECKBOX_LOG + "[" + str(num_checkbox) + "]"
        element = self.find_element((By.XPATH, element_locator), time=2)
        element.click()
        if element.is_selected():
            return True
        else:
            return False

    def click_delete_row_button(self, num_of_rows=1):
        i = num_of_rows
        while i > 0:
            row_xpath = FirewallPageLocators.LOCATOR_ROW + "'" + str(i - 1) + "']"
            element = self.find_element((By.XPATH, row_xpath), time=2)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            row_button = self.find_element(FirewallPageLocators.LOCATOR_DELETE_ROW_BUTTON, time=2)
            hover = ActionChains(self.driver).move_to_element(row_button)
            hover.perform()
            row_button.click()
            i -= 1

    def click_plus_line_button(self, num_of_rows=1):
        i = 1
        while i <= num_of_rows:
            row_xpath = FirewallPageLocators.LOCATOR_ROW + "'" + str(i - 1) + "']"
            row = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, row_xpath)))
            hover = ActionChains(self.driver).move_to_element(row)
            hover.perform()
            plus_button_xpath = FirewallPageLocators.LOCATOR_PLUS_ROW_BUTTON + "[" + str(i) + "]"
            plus_button = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, plus_button_xpath)))
            hover = ActionChains(self.driver).move_to_element(plus_button)
            hover.perform()
            plus_button.click()
            i += 1

    def get_num_of_last_row(self):
        return self.find_element(FirewallPageLocators.LOCATOR_LAST_ROW, time=2).get_attribute("textContent")

    def get_num_rows_selected(self):
        return self.find_element(FirewallPageLocators.LOCATOR_NUM_ROWS_SELECTED, time=2).get_attribute("textContent")

    def click_clear_selection_button(self):
        self.find_element(FirewallPageLocators.LOCATOR_CLEAR_SELECTION_BUTTON, time=2).click()

    def click_delete_all_rows_button(self):
        self.find_element(FirewallPageLocators.LOCATOR_DELETE_ALL_ROWS_BUTTON, time=2).click()

    def click_input_protocol_field(self):
        self.find_element(FirewallPageLocators.LOCATOR_SELECT_PROTOCOL, time=2).click()

    def set_port_value(self, num_of_port):
        to_port = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_INPUT_TO_PORT))
        to_port.click()
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_ARROW_UP_ELEMENT))
        to_port.send_keys(num_of_port, Keys.TAB)

    def set_protocol(self, protocol):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_SELECT_PROTOCOL)).click()
        if protocol == "All":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_ALL)).click()
        elif protocol == "TCP":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_TCP)).click()
        elif protocol == "UDP":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_UDP)).click()
        elif protocol == "ICMP":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_ICMP)).click()
        elif protocol == "GRE":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_GRE)).click()
        elif protocol == "ESP":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_ESP)).click()

    def get_actual_protocol(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_PROTOCOL, time=2).get_attribute("textContent")

    def get_actual_port(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_PORT, time=2).get_attribute("value")

    def set_action(self, action):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_SELECT_ACTION)).click()
        if action == "ACCEPT":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_ACTION_ACCEPT)).click()
        elif action == "REJECT":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_ACTION_REJECT)).click()
        elif action == "DROP":
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_ACTION_DROP)).click()

    def get_actual_action(self):
        return self.find_element(FirewallPageLocators.LOCATOR_ACTUAL_ACTION, time=2).get_attribute("value")

    def check_visibility_of_duplicate_entries_warning_message_and_button(self):
        message = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_DUPLICATE_ENTRIES_MESSAGE))
        button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_DELETE_DUPLICATE_BUTTON))
        if message and button:
            return True
        else:
            return False

    def check_invisibility_of_duplicate_entries_warning_message_and_button(self):
        message = WebDriverWait(self.driver, 2).until(
            EC.invisibility_of_element_located(FirewallPageLocators.LOCATOR_DUPLICATE_ENTRIES_MESSAGE))
        button = WebDriverWait(self.driver, 2).until(
            EC.invisibility_of_element_located(FirewallPageLocators.LOCATOR_DELETE_DUPLICATE_BUTTON))
        if message and button:
            return True
        else:
            return False

    def click_delete_duplicate_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(FirewallPageLocators.LOCATOR_DELETE_DUPLICATE_BUTTON)).click()

    def get_net_zone_1_to_net_zone_2_is_selected(self):
        if self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE1_TO_2_SELECTED, time=2):
            return True
        else:
            return False

    def get_net_zone_2_to_net_zone_1_is_selected(self):
        if self.find_element(FirewallPageLocators.LOCATOR_NET_ZONE2_TO_1_SELECTED, time=2):
            return True
        else:
            return False

    def get_from_ip_network_error_message(self):
        return self.find_element(FirewallPageLocators.LOCATOR_FROM_IP_NETWORK_INVALID_MESSAGE, time=2).is_displayed()

    def get_to_ip_network_error_message(self):
        return self.find_element(FirewallPageLocators.LOCATOR_TO_IP_NETWORK_INVALID_MESSAGE, time=2).is_displayed()

    def get_protocol_error_message(self):
        return WebDriverWait(self.driver, 2).until(
            EC.invisibility_of_element_located(FirewallPageLocators.LOCATOR_PROTOCOL_ERROR_MESSAGE)).is_displayed()
