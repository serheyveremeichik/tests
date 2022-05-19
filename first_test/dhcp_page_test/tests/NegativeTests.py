import pytest

from pages.DhcpServerPage import DhcpServerPage


@pytest.mark.parametrize("not_correct_start_ip", ["192.168.1.1000"])
def test_not_correct_ip_range_start(login, open_dhcp_chapter, browser, not_correct_start_ip):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_ip_range_start(not_correct_start_ip)
    assert dhcp_server_page.get_invalid_ipv4_address_message() is True


@pytest.mark.parametrize("not_correct_end_ip", ["192.168.1.256"])
def test_not_correct_ip_range_end(login, open_dhcp_chapter, browser, not_correct_end_ip):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_ip_range_end(not_correct_end_ip)
    assert dhcp_server_page.get_invalid_ipv4_address_message() is True


@pytest.mark.parametrize("not_correct_local_mask", ["33"])
def test_not_correct_local_mask(login, open_dhcp_chapter, browser, not_correct_local_mask):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_local_mask(not_correct_local_mask)
    assert dhcp_server_page.get_invalid_ipv4_netmask_message() is True


@pytest.mark.parametrize("not_correct_def_gateway", ["192.168.1.10000"])
def test_not_correct_def_gateway(login, open_dhcp_chapter, browser, not_correct_def_gateway):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_default_gateway(not_correct_def_gateway)
    assert dhcp_server_page.get_invalid_ipv4_address_message() is True


@pytest.mark.parametrize("not_correct_dns_server", ["192.168.1.10000"])
def test_not_correct_dns_server(login, open_dhcp_chapter, browser, not_correct_dns_server):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_dns_server(not_correct_dns_server)
    assert dhcp_server_page.get_invalid_ipv4_address_message() is True


@pytest.mark.parametrize("not_correct_wins_server", ["192.168.1.10000"])
def test_change_wins_server(login, open_dhcp_chapter, browser, not_correct_wins_server):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_wins_server(not_correct_wins_server)
    assert dhcp_server_page.get_invalid_ipv4_address_message() is True
