import pytest as pytest
from selenium import webdriver
from pytest_bdd import then, when, parsers
from selenium.webdriver.common.by import By


# Constants


HOME_PAGE_URL = 'http://127.0.0.1:5000'
SIGN_UP_PAGE_URL = HOME_PAGE_URL + '/sign-up'
LOGIN_PAGE_URL = HOME_PAGE_URL + '/login'


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


# Shared When Steps


@when(parsers.parse('a user enters an email: "{email}"'))
@when(parsers.parse('a user enters an email already in use: "{email}"'))
def enter_email(browser, email):
    email_input = browser.find_element(By.ID, 'email')
    email_input.send_keys(email)


@when('a user clicks submit')
def click_submit(browser):
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()


# Shared Then Steps


@then('an error alert is displayed')
def error_alert(browser):
    assert browser.find_elements(By.CLASS_NAME, 'alert-danger')


@then('a success alert is displayed')
def success_alert(browser):
    assert browser.find_elements(By.CLASS_NAME, 'alert-success')


@then('the home page is displayed')
def home_page_displayed(browser):
    assert browser.title == 'Contacts'

