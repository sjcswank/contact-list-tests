from tests.step_defs.conftest import SIGN_UP_PAGE_URL
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

scenarios('../features/sign_up.feature')


PASSWORD_INPUT_LOCATOR = (By.ID, 'password1')
CONFIRM_PASSWORD_LOCATOR = (By.ID, 'password2')


@given('a user is on the sign up page', target_fixture='sign_up_page')
def sign_up_page(browser):
    browser.get(SIGN_UP_PAGE_URL)


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(*PASSWORD_INPUT_LOCATOR)
    password_input.send_keys(password)


@when(parsers.parse('a user confirms the password: "{confirmation}"'))
def enter_confirmation(browser, confirmation):
    confirmation_input = browser.find_element(*CONFIRM_PASSWORD_LOCATOR)
    confirmation_input.send_keys(confirmation)


@then('the sign up page is displayed')
def sign_up_page_displayed(browser):
    assert browser.title == 'Sign Up'


