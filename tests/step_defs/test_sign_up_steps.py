from tests.step_defs.conftest import SIGN_UP_PAGE_URL
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scenarios('../features/sign_up.feature')


@given('the sign up page is displayed', target_fixture='sign_up_page')
def sign_up_page(browser):
    browser.get(SIGN_UP_PAGE_URL)


@when(parsers.parse('a user enters an email: "{email}"'))
def enter_email(browser, email):
    email_input = browser.find_element(By.ID, 'email')
    email_input.send_keys(email)


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(By.ID, 'password1')
    password_input.send_keys(password)


@when(parsers.parse('a user confirms the password: "{confirmation}"'))
def enter_confirmation(browser, confirmation):
    confirmation_input = browser.find_element(By.ID, 'password2')
    confirmation_input.send_keys(confirmation)


@when('a user clicks submit')
def click_submit(browser):
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()


@then('the home page is displayed')
def home_page_displayed(browser):
    assert browser.title == 'Contacts'


@then('a success alert is displayed')
def success_alert(browser):
    assert browser.find_elements(By.CLASS_NAME, 'alert-success')


@then('the sign up page is displayed')
def sign_up_page_displayed(browser):
    assert browser.title == 'Sign Up'


@then('an error alert is displayed')
def error_alert(browser):
    assert browser.find_elements(By.CLASS_NAME, 'alert-danger')