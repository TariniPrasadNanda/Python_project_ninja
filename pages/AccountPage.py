from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure

from pages.BasePage import BasePage


@allure.epic('Account Page')
class AccountPage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self, driver):
        logger.allure_log('Running Account Page Constructor')
        super().__init__(driver)

    edit_your_account_information_option_link_text = "Edit your account information"

    @allure.severity('CRITICAL')
    def display_status_of_edit_your_account_information_option(self):
        logger.allure_log('displaying status for edit account information')
        return self.check_display_status_of_element("edit_your_account_information_option_link_text",
                                                    self.edit_your_account_information_option_link_text)
