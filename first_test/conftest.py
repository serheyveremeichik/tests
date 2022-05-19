import pytest
from selenium import webdriver

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-insecure-localhost')
    caps = options.to_capabilities()
    caps["acceptInsecureCerts"] = True
    driver = webdriver.Chrome(executable_path="C:/UI_tests/first_test/chromedriver", desired_capabilities=caps)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(browser):
    login_page = LoginPage(browser)
    login_page.go_to_ui()
    login_page.enter_username("admin")
    login_page.enter_password("private")
    login_page.click_on_the_login_button()


@pytest.fixture(scope="session")
def open_firewall_chapter(browser):
    home_page = HomePage(browser)
    home_page.go_to_firewall_tab()


@pytest.fixture(scope="session")
def open_dhcp_chapter(browser):
    home_page = HomePage(browser)
    home_page.go_to_dhcp_server_tab()
