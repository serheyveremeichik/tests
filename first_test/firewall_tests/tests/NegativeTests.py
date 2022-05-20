import pytest

from pages.FireWallPage import FirewallRulesPage


@pytest.mark.parametrize("from_ip_network", ["192.168.1.0/33", "192.168.1./33", "any"])
@pytest.mark.parametrize("to_ip_network", ["192.168.2.0/33", "192.168.1./33", "any"])
def test_net_zones_from_ip_to_ip_fields_negative(login, open_firewall_chapter, browser, from_ip_network, to_ip_network):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_from_ip_network_value(from_ip_network)
    firewall_page.set_to_ip_network_value(to_ip_network)
    assert firewall_page.get_from_ip_network_error_message() is True
    assert firewall_page.get_to_ip_network_error_message() is True
    firewall_page.click_delete_row_button()


@pytest.mark.parametrize("protocol", ["TCP", "UDP"])
@pytest.mark.parametrize("port", ["FFF", 0, 65536])
def test_to_port_field(login, open_firewall_chapter, browser, port, protocol):
    firewall_page = FirewallRulesPage(browser)
    firewall_page.click_on_rules_tab()
    firewall_page.click_on_net_zone1_to_2_tab()
    firewall_page.click_on_add_row_button()
    firewall_page.set_protocol(protocol)
    firewall_page.set_port_value(port)
    assert firewall_page.get_protocol_error_message() is True
    firewall_page.click_delete_row_button()
