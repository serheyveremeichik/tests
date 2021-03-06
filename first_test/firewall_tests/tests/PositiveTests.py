import pytest

from pages.FireWallPage import FirewallRulesPage


@pytest.mark.parametrize("from_ip_network", ["192.168.1.0/24"])
@pytest.mark.parametrize("to_ip_network", ["192.168.2.0/24"])
def test_net_zones_from_ip_to_ip_fields(login, open_firewall_chapter, browser, from_ip_network, to_ip_network):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_from_ip_network_value(from_ip_network)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert from_ip_network == firewall_page.get_from_ip_network_value()
    firewall_page.set_to_ip_network_value(to_ip_network)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert to_ip_network == firewall_page.get_to_ip_network_value()
    firewall_page.click_delete_row_button()
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_from_ip_network_value(from_ip_network)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert from_ip_network == firewall_page.get_from_ip_network_value()
    firewall_page.set_to_ip_network_value(to_ip_network)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert to_ip_network == firewall_page.get_to_ip_network_value()
    firewall_page.click_delete_row_button()
    firewall_page.click_save()
    firewall_page.wait_saved_changes()


@pytest.mark.parametrize("some_text", ["some text"])
def test_comment_fields(login, open_firewall_chapter, browser, some_text):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_comment_text(some_text)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert some_text == firewall_page.get_comment_text()
    firewall_page.click_delete_row_button()
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_comment_text(some_text)
    firewall_page.click_save()
    firewall_page.wait_saved_changes()
    assert some_text == firewall_page.get_comment_text()
    firewall_page.click_delete_row_button()
    firewall_page.click_save()
    firewall_page.wait_saved_changes()


@pytest.mark.parametrize("num_of_rows", [5])
def test_plus_and_delete_row_buttons(login, open_firewall_chapter, browser, num_of_rows):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.get_num_of_last_row() == str(num_of_rows + 1)
    firewall_page.click_delete_row_button(num_of_rows + 1)
    assert firewall_page.get_num_of_last_row() == "0"
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.get_num_of_last_row() == str(num_of_rows + 1)
    firewall_page.click_delete_row_button(num_of_rows + 1)
    assert firewall_page.get_num_of_last_row() == "0"


@pytest.mark.parametrize("num_of_rows", [5])
def test_checkbox_select_all(login, open_firewall_chapter, browser, num_of_rows):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.click_select_all_checkbox() is True
    assert firewall_page.get_num_rows_selected() == (str(num_of_rows + 1) + " rows selected.")
    firewall_page.click_clear_selection_button()
    assert firewall_page.get_num_rows_selected() == "0 rows selected."
    firewall_page.click_select_all_checkbox()
    firewall_page.click_delete_all_rows_button()
    assert firewall_page.get_num_of_last_row() == "0"
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.click_select_all_checkbox() is True
    assert firewall_page.get_num_rows_selected() == (str(num_of_rows + 1) + " rows selected.")
    firewall_page.click_clear_selection_button()
    assert firewall_page.get_num_rows_selected() == "0 rows selected."
    firewall_page.click_select_all_checkbox()
    firewall_page.click_delete_all_rows_button()
    assert firewall_page.get_num_of_last_row() == "0"


@pytest.mark.parametrize("protocol", ["TCP", "UDP", "ICMP", "GRE", "ESP", "All"])
def test_protocol_field(login, open_firewall_chapter, browser, protocol):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_protocol(protocol)
    assert protocol == firewall_page.get_actual_protocol()
    firewall_page.click_delete_row_button()
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_protocol(protocol)
    assert protocol == firewall_page.get_actual_protocol()
    firewall_page.click_delete_row_button()


@pytest.mark.parametrize("protocol", ["TCP", "UDP"])
@pytest.mark.parametrize("port", [1500, 10000, 12000])
def test_to_port_field(login, open_firewall_chapter, browser, port, protocol):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_protocol(protocol)
    firewall_page.set_port_value(port)
    assert str(port) == firewall_page.get_actual_port()
    firewall_page.click_delete_row_button()
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_protocol(protocol)
    firewall_page.set_port_value(port)
    assert str(port) == firewall_page.get_actual_port()
    firewall_page.click_delete_row_button()


@pytest.mark.parametrize("action", ["DROP", "REJECT", "ACCEPT"])
def test_action_field(login, open_firewall_chapter, browser, action):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_action(action)
    assert action == firewall_page.get_actual_action()
    firewall_page.click_delete_row_button()
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_action(action)
    assert action == firewall_page.get_actual_action()
    firewall_page.click_delete_row_button()


def test_visibility_duplicate_entries_message_and_delete_button(login, open_firewall_chapter, browser):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button()
    assert firewall_page.check_visibility_of_duplicate_entries_warning_message_and_button() is True
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button()
    assert firewall_page.check_visibility_of_duplicate_entries_warning_message_and_button() is True


@pytest.mark.parametrize("num_of_rows", [5])
def test_delete_duplicate_button(login, open_firewall_chapter, browser, num_of_rows):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.get_num_of_last_row() == str(num_of_rows + 1)
    firewall_page.click_delete_duplicate_button()
    assert firewall_page.check_invisibility_of_duplicate_entries_warning_message_and_button() is True
    assert firewall_page.get_num_of_last_row() == "1"
    firewall_page.click_on_net_zone2_to_1_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.click_plus_line_button(num_of_rows)
    assert firewall_page.get_num_of_last_row() == str(num_of_rows + 1)
    firewall_page.click_delete_duplicate_button()
    assert firewall_page.check_invisibility_of_duplicate_entries_warning_message_and_button() is True
    assert firewall_page.get_num_of_last_row() == "1"


def test_net_zones_buttons(login, open_firewall_chapter, browser):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    assert firewall_page.get_net_zone_1_to_net_zone_2_is_selected() is True
    firewall_page.click_on_net_zone2_to_1_tab()
    assert firewall_page.get_net_zone_2_to_net_zone_1_is_selected() is True


def test_log_checkbox(login, open_firewall_chapter, browser):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    assert firewall_page.click_log_checkbox() is True

