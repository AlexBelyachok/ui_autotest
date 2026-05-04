import allure
import pytest

from data.data import ManagerPageData
from utils.page_fixture import bank_manager_page,bank_customer_page

@pytest.fixture
def auth_customer_with_account(bank_manager_page, customer_data, bank_customer_page):
    with allure.step("Предусловие 2: Открыть счет"):
        data = customer_data.copy()
        bank_manager_page.setup_account(data)
    with allure.step("Предусловие 3: Зайти в аккаунт"):
        bank_customer_page.open()
        bank_customer_page.find_element(bank_customer_page.LBL_LOGIN_ANCHOR)
        bank_customer_page.select_your_name(data)
        bank_customer_page.click(bank_customer_page.BTN_SUBMIT)

    yield data


@pytest.fixture(scope="function")
def customer_data(bank_manager_page):
    with allure.step("Предусловие 1: Создать профиль пользователя"):
        bank_manager_page.open()
        bank_manager_page.click_add_customer()
        data = ManagerPageData.VALID
        bank_manager_page.enter_data_and_send(data)
        bank_manager_page.grab_alert()

    yield data

    with allure.step("Очистка: Удалить созданного клиента"):
        bank_manager_page.open()
        bank_manager_page.click(bank_manager_page.TAB_CUSTOMERS)

        bank_manager_page.search_customer(data["first_name"])

        if bank_manager_page.is_customer_in_table(data["first_name"], timeout=1):
            bank_manager_page.click_delete_customer(data["first_name"])
        else:
            allure.attach(
                "Клиент уже удален",
                name="Status",
                attachment_type=allure.attachment_type.TEXT,
            )
