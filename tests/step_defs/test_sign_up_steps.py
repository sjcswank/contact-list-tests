from tests.step_defs.conftest import SIGN_UP_PAGE_URL
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By

scenarios('../features/sign_up.feature')


@given('a user is on the sign up page', target_fixture='sign_up_page')
def sign_up_page(browser):
    browser.get(SIGN_UP_PAGE_URL)


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(By.ID, 'password1')
    password_input.send_keys(password)


@when(parsers.parse('a user confirms the password: "{confirmation}"'))
def enter_confirmation(browser, confirmation):
    confirmation_input = browser.find_element(By.ID, 'password2')
    confirmation_input.send_keys(confirmation)


@then('the sign up page is displayed')
def sign_up_page_displayed(browser):
    assert browser.title == 'Sign Up'


