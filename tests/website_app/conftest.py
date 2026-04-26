import pytest

from utils.page_fixture import reg_page
from data.data import RegPageData


@pytest.fixture(scope="function")
def logged_in_session(reg_page):

    reg_page.open()
    reg_page.enter_reg_data(RegPageData.VALID)
    reg_page.click(reg_page.BTN_LOGIN, "кнопка Login")
    reg_page.wait_until_invisible(reg_page.IMG_LOADING)

    yield reg_page

    if reg_page.driver.find_elements(*reg_page.LNK_LOGOUT):
        reg_page.click(reg_page.LNK_LOGOUT)
