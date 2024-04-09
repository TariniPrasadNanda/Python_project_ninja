from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure
from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


@allure.epic('Register Page')
class RegisterPage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self, driver):
        logger.allure_log('running constructor of register page')
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    @allure.severity('CRITICAL')
    def enter_first_name(self,first_name_text):
        logger.allure_log('entering first name in Register page')
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)

    @allure.severity('CRITICAL')
    def enter_last_name(self,last_name_text):
        logger.allure_log('entering last name in Register page')
        self.type_into_element(last_name_text,"last_name_field_id",self.last_name_field_id)

    @allure.severity('CRITICAL')
    def enter_email(self,email_text):
        logger.allure_log('entering email address in Register page')
        self.type_into_element(email_text,"email_field_id",self.email_field_id)

    @allure.severity('CRITICAL')
    def enter_telephone(self,telephone_text):
        logger.allure_log('entering telephone number in Register page')
        self.type_into_element(telephone_text,"telephone_field_id",self.telephone_field_id)

    @allure.severity('CRITICAL')
    def enter_password(self,password_text):
        logger.allure_log('entering password in Register page')
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    @allure.severity('CRITICAL')
    def enter_password_confirm(self,password_text):
        logger.allure_log('entering password again in Register page')
        self.type_into_element(password_text,"confirm_password_field_id",self.confirm_password_field_id)

    @allure.severity('CRITICAL')
    def select_agree_checkbox_field(self):
        logger.allure_log('clicking on agree check box in Register page')
        self.element_click("agree_field_name",self.agree_field_name)

    @allure.severity('CRITICAL')
    def click_on_continue_button(self):
        logger.allure_log('clicking on continue in Register page')
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    @allure.severity('CRITICAL')
    def select_yes_radio_button(self):
        logger.allure_log('clicking on yes radio button in Register page')
        self.element_click("yes_radio_button_xpath",self.yes_radio_button_xpath)

    @allure.severity('CRITICAL')
    def register_an_account(self,first_name_text,last_name_text,email_text,telephone_text,password_text,password_confirm_text,yes_or_no,privacy_policy):
        logger.allure_log('registering for a new account by entering all fields  in Register page')
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_confirm_text)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    @allure.severity('CRITICAL')
    def retrieve_duplicate_email_warning(self):
        logger.allure_log('retrieving duplicate email warning message in Register page')
        return self.retrieve_element_text("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_privacy_policy_warning(self):
        logger.allure_log('Retrieving  privacy policy warning message in Register page')
        return self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_first_name_warning(self):
        logger.allure_log('Retrieving  first name warning message in Register page')
        return self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_last_name_warning(self):
        logger.allure_log('Retrieving  last name warning message in Register page')
        return self.retrieve_element_text("last_name_warning_xpath",self.last_name_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_email_warning(self):
        logger.allure_log('Retrieving  email warning message in Register page')
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_telephone_warning(self):
        logger.allure_log('Retrieving  telephone number warning message in Register page')
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    @allure.severity('CRITICAL')
    def retrieve_password_warning(self):
        logger.allure_log('Retrieving  password warning message in Register page')
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)

    @allure.severity('CRITICAL')
    def verify_all_warnings(self,expected_privacy_policy_warning,expected_first_name_warning_message,expected_last_name_warning_message,expected_email_warning_message,expected_telephone_warning_message,expected_password_warning_message):
        logger.allure_log('Verifying all warning messages in Register page')
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_last_name_warning_message = self.retrieve_last_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_telephone_warning_message = self.retrieve_telephone_warning()
        actual_password_warning_message = self.retrieve_password_warning()

        status = False

        if expected_privacy_policy_warning.__contains__(actual_privacy_policy_warning):
            if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
                if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status






