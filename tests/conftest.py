import allure
import pytest
from selenium import webdriver

from config.pydantic_config import settings


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    if settings.headless:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if not driver and "questions" in item.funcargs:
            pass

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_{report.nodeid}",
                attachment_type=allure.attachment_type.PNG,
            )
