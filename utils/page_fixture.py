import pytest

from pages.banking_app.bank_customer_page import BankCustomerPage
from pages.banking_app.bank_manager_page import BankManagerPage
from pages.website_app.reg_page import RegPage


@pytest.fixture
def reg_page(driver):
    return RegPage(driver)


@pytest.fixture
def bank_customer_page(driver):
    return BankCustomerPage(driver)


@pytest.fixture(scope="function")
def bank_manager_page(driver):
    return BankManagerPage(driver)
