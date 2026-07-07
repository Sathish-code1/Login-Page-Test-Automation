import pytest
import re

from Pages.LoginPage import LoginPage
from TestData.LoginData import LoginData
from Utilities.Logger import LogGenerator


logger = LogGenerator.loggen()


class TestLogin:

    # -------------------------------------------------------
    # TC_001 - Verify Login Page Opens
    # -------------------------------------------------------

    def test_login_page_load(self, setup):

        logger.info("TC_001 : Verify Login Page")

        driver = setup

        assert "login" in driver.current_url.lower()

        logger.info("Login Page Loaded Successfully")

    # -------------------------------------------------------
    # TC_002 - Empty Email
    # -------------------------------------------------------

    def test_empty_email(self, setup):

        logger.info("TC_002 : Empty Email")

        login = LoginPage(setup)

        login.login(
            LoginData.EMPTY,
            LoginData.VALID_PASSWORD
        )

        actual = login.get_error_message_email_empty()

        expected = LoginData.MSG_EMPTY_EMAIL

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_003 - Empty Password
    # -------------------------------------------------------

    def test_empty_password(self, setup):

        logger.info("TC_003 : Empty Password")

        login = LoginPage(setup)

        login.login(
            LoginData.VALID_EMAIL,
            LoginData.EMPTY
        )

        actual = login.get_error_message_pass_empty()

        expected = LoginData.MSG_EMPTY_PASSWORD

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_004 - Both Empty
    # -------------------------------------------------------

    def test_empty_email_password(self, setup):

        logger.info("TC_004 : Both Fields Empty")

        login = LoginPage(setup)

        login.login(
            LoginData.EMPTY,
            LoginData.EMPTY
        )

        actual = login.get_error_message_email_pass_empty()

        expected = LoginData.MSG_EMPTY_EMAIL

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_005 - Invalid Email Format
    # -------------------------------------------------------

    @pytest.mark.parametrize(
        "email",
        LoginData.INVALID_EMAIL_FORMATS
    )
    def test_invalid_email_format(self, setup, email):

        logger.info("TC_005 : Invalid Email Format")

        login = LoginPage(setup)

        # Python format validation
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        assert re.match(pattern, email) is None

        login.login(
            email,
            LoginData.VALID_PASSWORD
        )

        actual = login.get_error_message_email_invalid()

        expected = LoginData.MSG_INVALID_EMAIL

        logger.info(f"Testing Email : {email}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_006 - Invalid Credentials
    # -------------------------------------------------------

    def test_invalid_credentials(self, setup):

        logger.info("TC_006 : Invalid Credentials")

        login = LoginPage(setup)

        login.login(
            LoginData.INVALID_EMAIL,
            LoginData.INVALID_PASSWORD
        )

        actual = login.get_error_message_invalid_credential()

        expected = LoginData.MSG_INVALID_CREDENTIALS

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_007 - Wrong Password
    # -------------------------------------------------------

    def test_wrong_password(self, setup):

        logger.info("TC_007 : Wrong Password")

        login = LoginPage(setup)

        login.login(
            LoginData.VALID_EMAIL,
            LoginData.INVALID_PASSWORD
        )

        actual = login.get_error_message_invalid_credential()

        expected = LoginData.MSG_WRONG_PASSWORD

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected

    # -------------------------------------------------------
    # TC_008 - Password Hidden
    # -------------------------------------------------------

    def test_password_hidden(self, setup):

        logger.info("TC_008 : Password Hidden")

        login = LoginPage(setup)

        assert login.is_password_hidden()

        logger.info("Password is masked")

    # -------------------------------------------------------
    # TC_009 - Successful Login
    # -------------------------------------------------------

    def test_valid_login(self, setup):

        logger.info("TC_009 : Valid Login")

        login = LoginPage(setup)

        login.login(
            LoginData.VALID_EMAIL,
            LoginData.VALID_PASSWORD
        )

        actual = login.get_success_message()

        expected = LoginData.MSG_LOGIN_SUCCESS

        logger.info(f"Expected : {expected}")
        logger.info(f"Actual   : {actual}")

        assert actual == expected