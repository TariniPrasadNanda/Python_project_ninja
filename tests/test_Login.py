import pytest
import utilities.logs as logger
import allure
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities.ExcelUtils import *
from utilities.EmailIdGen import *
from datetime import datetime


@allure.epic('Login tests')
class TestSearch:
    # log = logger.get_logger()
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, setup):
        self.driver = setup
        logging.info("Page Object Initialization")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)

    @allure.severity('CRITICAL')
    @pytest.mark.parametrize("email_address,password",
                             get_data_from_excel("ExcelFiles/TutorialsNinja.xlsx", "LoginTest"))
    def test_login_with_valid_credentials(self, email_address, password):
        """
        Running test login with valid credentails
        """
        logger.allure_log('Running test login with valid credentails.')
        self.home_page.navigate_to_login_page()
        self.login_page.login_to_application(email_address, password)
        assert self.account_page.display_status_of_edit_your_account_information_option()

    @allure.severity('CRITICAL')
    def test_login_with_invalid_email_and_valid_password(self):
        """
        Running test login with invalid email and valid password
        """
        logger.allure_log('Running test login with invalid email and valid password')
        self.home_page.navigate_to_login_page()
        self.login_page.login_to_application(self.generate_email_with_time_stamp(), "12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        logging.info(expected_warning_message)
        assert self.login_page.retrieve_warning_message().__contains__(expected_warning_message)

    @allure.severity('CRITICAL')
    def test_login_with_valid_email_and_invalid_password(self):
        """
        Running test login with valid email and invalid password
        """
        logger.allure_log('Running test login with valid email and invalid password')
        self.home_page.navigate_to_login_page()
        self.login_page.login_to_application("amotooricap1@gmail.com", "1234567890")
        expected_warning_message = ("Warning: No match for E-Mail Address and/or Password.")
        logging.info(expected_warning_message)
        assert self.login_page.retrieve_warning_message().__contains__(
            expected_warning_message)

    @allure.severity('CRITICAL')
    def test_login_without_entering_credentials(self):
        """
        Running test login without entering credentials
        """
        try:
            logger.allure_log('Running test login without entering credentials')
            self.home_page.navigate_to_login_page()
            self.login_page.login_to_application("", "")
            expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
            assert self.login_page.retrieve_warning_message().__contains__(
                expected_warning_message)
        except:
            logger.step_fail("failed test:test_login_without_entering_credentials ")

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "tarini" + time_stamp + "@gmail.com"

# report generation
# pytest  --alluredir .\Reports\
# allure serve .\Reports\

##running single test in pytest
#pytest ./tests/test_Login.py -k "test_login_without_entering_credentials"
