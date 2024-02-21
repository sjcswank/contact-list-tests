from pytest_bdd import scenarios, when, parsers, then
from selenium.webdriver.common.by import By
import time


scenarios('../features/homepage.feature')


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(By.ID, 'password')
    password_input.send_keys(password)


@when(parsers.parse('a user enters a contact name: "{name}"'))
def enter_name(browser, name):
    name_input = browser.find_element(By.ID, 'name')
    name_input.send_keys(name)


@when(parsers.parse('a user enters a contact phone number: "{number}"'))
def enter_number(browser, number):
    number_input = browser.find_element(By.ID, 'phone')
    number_input.send_keys(number)


@when(parsers.parse('a user enters a contact email: "{email}"'))
def enter_email(browser, email):
    email_input = browser.find_element(By.ID, 'email')
    email_input.send_keys(email)


@when(parsers.parse('a user enters a contact address: "{address}"'))
def enter_address(browser, address):
    address_input = browser.find_element(By.ID, 'address')
    address_input.send_keys(address)


@then(parsers.parse('a contact for "{name}" is displayed in the contact list'))
def contact_displayed(browser, name):
    assert browser.find_element(By.XPATH, '//th[text()="' + name + '"]')


@when(parsers.parse('a user clicks the delete button for "{name}"'))
def click_delete(browser, name):
    delete_button = browser.find_element(By.XPATH, '//tr/th[text()="' + name + '"]/following-sibling::td[5]/button')
    delete_button.click()


@then(parsers.parse('a contact for "{name}" will not be displayed in the contact list'))
def no_contact(browser, name):
    time.sleep(1)
    assert not browser.find_elements(By.XPATH, '//th[text()="' + name + '"]')
