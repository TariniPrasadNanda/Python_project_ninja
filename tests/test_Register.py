import logging
import pytest
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.AccountSuccessPage import AccountSuccessPage
from utilities import ExcelUtils
from utilities.EmailIdGen import *
from datetime import datetime
import utilities.logs as logger
import allure

@allure.epic('Register tests')
class TestRegister:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, setup):
        self.driver = setup
        logging.info("Page Object Initialization")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.account_success_page = AccountSuccessPage(self.driver)

    @allure.severity('CRITICAL')
    def test_register_with_mandatory_fields(self):
        """
                Running test Register with mandatory fields
        """
        logger.allure_log('Running test Register with mandatory fields')
        self.home_page.navigate_to_register_page()
        self.register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx","RegisterTest",2,1),
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx","RegisterTest",2,2),
            generate_email_with_time_stamp(),
            "1234567890",
            "12345","12345","no","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert self.account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    @allure.severity('CRITICAL')
    def test_register_with_all_fields(self):
        """
                Running test Register with all fields
        """
        logger.allure_log('Running test Register with all fields')
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Arun","Motoori",self.generate_email_with_time_stamp(),"1234567890","12345","12345","yes","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    @allure.severity('CRITICAL')
    def test_register_with_duplicate_email(self):
        """
                Running test Register with duplicate email
        """
        logger.allure_log('Running test Register with duplicate email')
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Arun","Motoori","amotooricap3@gmail.com","1234567890","12345","12345","yes","select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    @allure.severity('CRITICAL')
    def test_register_without_entering_any_fields(self):
        """
                Running test Register without entering any data
        """
        logger.allure_log('Running test Register without entering any data')
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("","","","","","","no","no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!","First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!","E-Mail Address does not appear to be valid!","Telephone must be between 3 and 32 characters!","Password must be between 4 and 20 characters!")
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "tarini" + time_stamp + "@gmail.com"


