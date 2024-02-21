from pytest_bdd import scenarios, given, when, then, parsers
from tests.step_defs.conftest import LOGIN_PAGE_URL
from selenium.webdriver.common.by import By

scenarios('../features/login.feature')


PASSWORD_INPUT_LOCATOR = (By.ID, 'password')


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(*PASSWORD_INPUT_LOCATOR)
    password_input.send_keys(password)


@then('the login page is displayed')
def login_page_displayed(browser):
    assert browser.title == "Login"
