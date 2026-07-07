import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.ConfigReader import ConfigReader
from Utilities.Logger import LogGenerator
from Utilities.Screenshot import Screenshot
from Utilities.WordReport import WordReport


# -----------------------------
# Global Objects
# -----------------------------

config = ConfigReader()
logger = LogGenerator.loggen()
report = WordReport()


# -----------------------------
# Browser Setup Fixture
# -----------------------------

@pytest.fixture(scope="function")
def setup():

    browser = config.get("Application", "browser").lower()

    logger.info("=========================================")
    logger.info("Starting Test Execution")
    logger.info(f"Selected Browser : {browser}")

    if browser == "chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            ),
            options=options
        )

    elif browser == "edge":

        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            ),
            options=options
        )

    else:

        raise Exception(f"Browser '{browser}' is not supported.")

    driver.implicitly_wait(
        int(config.get("Application", "implicit_wait"))
    )

    url = config.get("Application", "base_url")

    logger.info(f"Opening URL : {url}")

    driver.get(url)

    yield driver

    logger.info("Closing Browser")

    driver.quit()

    logger.info("Browser Closed")
    logger.info("=========================================")


# ---------------------------------------------------
# Capture Screenshot Automatically on Test Failure
# ---------------------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    result = outcome.get_result()

    if result.when == "call":

        if result.failed:

            driver = item.funcargs["setup"]

            screenshot_path = Screenshot.capture(
                driver,
                item.name
            )

            logger.error(f"Test Failed : {item.name}")
            logger.error(f"Screenshot : {screenshot_path}")

            failure_reason = ""

            if call.excinfo:
                failure_reason = str(call.excinfo.value)

            report.add_failure(

                testcase=item.name,

                expected="Refer Test Case",

                actual="Assertion Failed",

                reason=failure_reason,

                screenshot=screenshot_path

            )

        elif result.passed:

            logger.info(f"Test Passed : {item.name}")

        elif result.skipped:

            logger.warning(f"Test Skipped : {item.name}")


# -----------------------------------------
# Save Word Report after Execution
# -----------------------------------------

def pytest_sessionfinish(session, exitstatus):

    logger.info("Saving Word Report")

    report.save()

    logger.info("Execution Completed")