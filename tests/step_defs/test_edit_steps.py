from pytest_bdd import when, parsers, then, scenarios
from selenium.webdriver.common.by import By
import time


scenarios('../features/edit.feature')


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(By.ID, 'password')
    password_input.send_keys(password)


@then(parsers.parse('the edit page for "{name}" will be displayed'))
def edit_page_for_contact(browser, name):
    name_input = browser.find_element(By.ID, 'name')
    assert name_input.get_attribute("value") == name

@when('a user clears the contact name input')
def clear_name(browser):
    name_input = browser.find_element(By.ID, 'name')
    name_input.clear()
