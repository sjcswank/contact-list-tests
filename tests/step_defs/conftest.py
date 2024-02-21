import pytest as pytest
from selenium import webdriver
from pytest_bdd import given, then, when, parsers
from selenium.webdriver.common.by import By
import time

# Constants


HOME_PAGE_URL = 'http://127.0.0.1:5000'
SIGN_UP_PAGE_URL = HOME_PAGE_URL + '/sign-up'
LOGIN_PAGE_URL = HOME_PAGE_URL + '/login'

EMAIL_INPUT_LOCATOR = (By.ID, 'email')
SUBMIT_BUTTON_LOCATOR = (By.ID, 'submit')
ALERT_DANGER_LOCATOR = (By.CLASS_NAME, 'alert-danger')
ALERT_SUCCESS_LOCATOR = (By.CLASS_NAME, 'alert-success')

CONTACT_NAME_INPUT_LOCATOR = (By.ID, 'name')
CONTACT_PHONE_INPUT_LOCATOR = (By.ID, 'phone')
CONTACT_EMAIL_INPUT_LOCATOR = (By.ID, 'email')
CONTACT_ADDRESS_INPUT_LOCATOR = (By.ID, 'address')


# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"step failed: {step}")


# Fixtures


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Shared Given Steps


@given('a user is on the login page', target_fixture='login_page')
def login_page(browser):
    browser.get(LOGIN_PAGE_URL)


# Shared When Steps


@when(parsers.parse('a user enters an email: "{email}"'))
@when(parsers.parse('a user enters an email already in use: "{email}"'))
def enter_email(browser, email):
    email_input = browser.find_element(*EMAIL_INPUT_LOCATOR)
    email_input.send_keys(email)


@when('a user clicks submit')
def click_submit(browser):
    submit_button = browser.find_element(*SUBMIT_BUTTON_LOCATOR)
    submit_button.click()


@when(parsers.parse('a user enters a contact name: "{name}"'))
def enter_name(browser, name):
    name_input = browser.find_element(*CONTACT_NAME_INPUT_LOCATOR)
    name_input.send_keys(name)


@when(parsers.parse('a user enters a contact phone number: "{number}"'))
def enter_number(browser, number):
    number_input = browser.find_element(*CONTACT_PHONE_INPUT_LOCATOR)
    number_input.send_keys(number)


@when(parsers.parse('a user enters a contact email: "{email}"'))
def enter_email(browser, email):
    email_input = browser.find_element(*CONTACT_EMAIL_INPUT_LOCATOR)
    email_input.send_keys(email)


@when(parsers.parse('a user enters a contact address: "{address}"'))
def enter_address(browser, address):
    address_input = browser.find_element(*CONTACT_ADDRESS_INPUT_LOCATOR)
    address_input.send_keys(address)


@when(parsers.parse('a user clicks the edit button for "{name}"'))
def click_delete(browser, name):
    edit_button = browser.find_element(By.XPATH, '//tr/th[text()="' + name + '"]/following-sibling::td[4]/a')
    edit_button.click()


# Shared Then Steps


@then('an error alert is displayed')
def error_alert(browser):
    assert browser.find_elements(*ALERT_DANGER_LOCATOR)


@then('a success alert is displayed')
def success_alert(browser):
    assert browser.find_elements(*ALERT_SUCCESS_LOCATOR)


@then('the home page is displayed')
def home_page_displayed(browser):
    assert browser.title == 'Contacts'


@then(parsers.parse('the edit page is displayed'))
def edit_page(browser):
    assert browser.title == 'Edit'


@then(parsers.parse('a contact for "{name}" is displayed in the contact list'))
def contact_displayed(browser, name):
    assert browser.find_element(By.XPATH, '//th[text()="' + name + '"]')


@then(parsers.parse('a contact for "{name}" will not be displayed in the contact list'))
def no_contact(browser, name):
    time.sleep(1)
    assert not browser.find_elements(By.XPATH, '//th[text()="' + name + '"]')
