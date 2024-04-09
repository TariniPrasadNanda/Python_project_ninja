from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


@allure.epic('Login Page')
class LoginPage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self, driver):
        logger.allure_log('Running constructor of Login page')
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    @allure.severity('CRITICAL')
    def enter_email_address(self,email_address_text):
        logger.allure_log('entering email address in login page')
        self.type_into_element(email_address_text,"email_address_field_id",self.email_address_field_id)

    @allure.severity('CRITICAL')
    def enter_password(self,password_text):
        logger.allure_log('entering password in login page')
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    @allure.severity('CRITICAL')
    def click_on_login_button(self):
        logger.allure_log('clicking on login button in login page')
        self.element_click("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    @allure.severity('CRITICAL')
    def login_to_application(self, email_address_text, password_text):
        logger.allure_log('logging in into application  in login page')
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_login_button()

    @allure.severity('CRITICAL')
    def retrieve_warning_message(self):
        logger.allure_log('retrieving warning message in login page')
        return self.retrieve_element_text("warning_message_xpath", self.warning_message_xpath)





