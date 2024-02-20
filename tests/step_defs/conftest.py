import pytest as pytest
from selenium import webdriver


# Constants

HOME_PAGE_URL = 'http://127.0.0.1:5000'
SIGN_UP_PAGE_URL = HOME_PAGE_URL + '/sign-up'


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
