import time
import utilities.logs as logger
import allure
import pytest
from selenium import webdriver
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage
from pages.BasePage import BasePage
import logging
from utilities.ExcelUtils import *


@allure.epic('Search tests')
class TestSearch:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, setup):
        self.driver = setup
        logging.info("Page Object Initialization")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.base_page = BasePage(self.driver)

    @allure.severity('CRITICAL')
    def test_search_for_a_valid_product(self):
        """
                Running test Search for a valid product
        """
        logger.allure_log('Running test Search for a valid product')
        self.home_page.search_for_a_product("HP")
        assert self.search_page.display_status_of_valid_product()

    @allure.severity('CRITICAL')
    def test_search_for_an_invalid_product(self):
        """
                Running test Search for an invalid product
        """
        logger.allure_log('Running test Search for an invalid product')
        self.home_page.search_for_a_product("Honda")
        expected_text = "There is no product that matches the search criteria."
        assert self.search_page.retrieve_no_product_message().__eq__(expected_text)

    @allure.severity('CRITICAL')
    def test_search_without_entering_any_product(self):
        """
                Running test Search without entering any product
        """
        logger.allure_log('Running test Search without entering any product')
        self.home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert self.search_page.retrieve_no_product_message().__eq__(expected_text)

    @allure.severity('CRITICAL')
    def test_search_for_imac(self):
        """
                running test by searching for imac and adding to cart comparing price and checking out by
                          validating message  in search page
        """
        logger.allure_log('running test by searching for imac and adding to cart comparing price and checking out by '
                          'validating message  in search page')
        self.home_page.navigate_to_login_page()
        self.login_page.login_to_application("jayjagannath@gmail.com", "jayjagannath")
        self.home_page.search_for_a_product("imac")
        time.sleep(2)
        x = self.base_page.get_element("xpath", "(//button[@type='button'])[10]")
        print(x.text)
        time.sleep(10)

# report generation
# pytest  --alluredir .\Reports\
# allure serve .\Reports\

##running single test in pytest
# pytest ./tests/test_Search.py -k "test_search_for_imac"
