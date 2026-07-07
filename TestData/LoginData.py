class LoginData:

    # ==========================================================
    # VALID LOGIN
    # ==========================================================

    VALID_EMAIL = "Test@gmail.com"

    VALID_PASSWORD = "test123"

    # ==========================================================
    # INVALID LOGIN
    # ==========================================================

    INVALID_EMAIL = "invalid@gmail.com"

    INVALID_PASSWORD = "WrongPassword"

    # ==========================================================
    # EMAIL FORMAT VALIDATION
    # ==========================================================

    INVALID_EMAIL_FORMAT_1 = "admin"

    INVALID_EMAIL_FORMAT_2 = "admin@"

    INVALID_EMAIL_FORMAT_3 = "@gmail.com"

    INVALID_EMAIL_FORMAT_4 = "admin@gmail"

    INVALID_EMAIL_FORMAT_5 = "admin.com"

    INVALID_EMAIL_FORMAT_6 = "admin@@gmail.com"

    INVALID_EMAIL_FORMAT_7 = "admin gmail.com"

    # ==========================================================
    # EMPTY VALUES
    # ==========================================================

    EMPTY = ""

    SPACE = " "

    # ==========================================================
    # EXPECTED ERROR MESSAGES
    # (Modify according to your application)
    # ==========================================================

    MSG_EMPTY_EMAIL = "Please enter an email address or phone number."

    MSG_EMPTY_PASSWORD = "Please enter a password."

    MSG_INVALID_EMAIL = "Please enter a valid email address."

    MSG_INVALID_CREDENTIALS = "Wrong email or password."

    MSG_WRONG_PASSWORD = "Wrong email or password."

    MSG_LOGIN_SUCCESS = "Logged in"

    INVALID_EMAIL_FORMATS = [
    "admin",
    "admin@",
    "@gmail.com",
    "admin@gmail",
    "admin.com",
    "admin@@gmail.com",
    "admin gmail.com"
    ]