from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure

from pages.BasePage import BasePage


@allure.epic('Account success Page')
class AccountSuccessPage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self,driver):
        logger.allure_log('Running constructor of account success page')
        super().__init__(driver)

    account_creation_message_xpath = "//div[@id='content']/h1"

    @allure.severity('CRITICAL')
    def retrieve_account_creation_message(self):
        logger.allure_log('retrieving account creation message in account success page ')
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)




