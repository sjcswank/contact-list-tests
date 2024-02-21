from pytest_bdd import scenarios, when, parsers, then
from selenium.webdriver.common.by import By


scenarios('../features/homepage.feature')


PASSWORD_INPUT_LOCATOR = (By.ID, 'password')


@when(parsers.parse('a user enters a password: "{password}"'))
def enter_password(browser, password):
    password_input = browser.find_element(*PASSWORD_INPUT_LOCATOR)
    password_input.send_keys(password)


@when(parsers.parse('a user clicks the delete button for "{name}"'))
def click_delete(browser, name):
    delete_button = browser.find_element(By.XPATH, '//tr/th[text()="' + name + '"]/following-sibling::td[5]/button')
    delete_button.click()

