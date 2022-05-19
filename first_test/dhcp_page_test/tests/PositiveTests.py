import pytest

from pages.DhcpServerPage import DhcpServerPage, DhcpServerPageLocators


def test_switch_netzone_2(login, open_dhcp_chapter, browser):
    dhcp_server_page = DhcpServerPage(browser)
    assert "OFF" == dhcp_server_page.dhcp_for_netzone2_switch()
    assert "ON" == dhcp_server_page.dhcp_for_netzone2_switch()


@pytest.mark.parametrize("new_start_ip, old_start_ip", [("192.168.1.100", "192.168.1.1")])
def test_change_ip_range_start(login, open_dhcp_chapter, browser, new_start_ip, old_start_ip):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_ip_range_start(new_start_ip)
    dhcp_server_page.click_save()
    assert new_start_ip == dhcp_server_page.get_ip_range_start()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.set_ip_range_start(old_start_ip)
    dhcp_server_page.click_save()
    assert old_start_ip == dhcp_server_page.get_ip_range_start()


@pytest.mark.parametrize("old_end_ip, new_end_ip", [("192.168.1.254", "192.168.1.200")])
def test_change_ip_range_end(login, open_dhcp_chapter, browser, old_end_ip, new_end_ip):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_ip_range_end(new_end_ip)
    dhcp_server_page.click_save()
    assert new_end_ip == dhcp_server_page.get_ip_range_end()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.set_ip_range_end(old_end_ip)
    dhcp_server_page.click_save()
    assert old_end_ip == dhcp_server_page.get_ip_range_end()


@pytest.mark.parametrize("old_local_mask, new_local_mask", [("24", "18")])
def test_change_local_mask(login, open_dhcp_chapter, browser, old_local_mask, new_local_mask):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_local_mask(new_local_mask)
    dhcp_server_page.click_save()
    assert new_local_mask == dhcp_server_page.get_local_mask()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.set_local_mask(old_local_mask)
    dhcp_server_page.click_save()
    assert old_local_mask == dhcp_server_page.get_local_mask()


@pytest.mark.parametrize("old_def_gateway, new_def_gateway", [("192.168.1.1", "192.168.1.3")])
def test_change_def_gateway(login, open_dhcp_chapter, browser, old_def_gateway, new_def_gateway):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_default_gateway(new_def_gateway)
    dhcp_server_page.click_save()
    assert new_def_gateway == dhcp_server_page.get_def_gateway()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.set_default_gateway(old_def_gateway)
    dhcp_server_page.click_save()
    assert old_def_gateway == dhcp_server_page.get_def_gateway()


@pytest.mark.parametrize("old_dns_server, new_dns_server", [("192.168.1.1", "192.168.1.3")])
def test_change_dns_server(login, open_dhcp_chapter, browser, old_dns_server, new_dns_server):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_dns_server(new_dns_server)
    dhcp_server_page.click_save()
    assert new_dns_server == dhcp_server_page.get_dns_server()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.set_dns_server(old_dns_server)
    dhcp_server_page.click_save()
    assert old_dns_server == dhcp_server_page.get_dns_server()


@pytest.mark.parametrize("wins_server", ["192.168.1.10"])
def test_change_wins_server(login, open_dhcp_chapter, browser, wins_server):
    dhcp_server_page = DhcpServerPage(browser)
    dhcp_server_page.set_wins_server(wins_server)
    dhcp_server_page.click_save()
    assert wins_server == dhcp_server_page.get_wins_server()
    dhcp_server_page.wait_saved_changes()
    dhcp_server_page.delete_value(DhcpServerPageLocators.LOCATOR_WINS_SERVER)
    dhcp_server_page.click_save()
    assert str(dhcp_server_page.get_wins_server()) == ""
