from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure
from pages.BasePage import BasePage


@allure.epic('Search Page')
class SearchPage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self,driver):
        logger.allure_log('Running constructor in search page')
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    @allure.severity('CRITICAL')
    def display_status_of_valid_product(self):
        logger.allure_log('displaying status of valid product in search page')
        return self.check_display_status_of_element("valid_hp_product_link_text",self.valid_hp_product_link_text)

    @allure.severity('CRITICAL')
    def retrieve_no_product_message(self):
        logger.allure_log('Retrieving no product message  in search page')
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)




