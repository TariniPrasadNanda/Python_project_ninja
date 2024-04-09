from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


@allure.epic('Home  Page')
class HomePage(BasePage):
    @allure.severity('CRITICAL')
    def __init__(self,driver):
        logger.allure_log('Running constructor in Home Page')
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    @allure.severity('CRITICAL')
    def enter_product_into_search_box_field(self,product_name):
        logger.allure_log('entering product into search box in home pagde')
        self.type_into_element(product_name,"search_box_field_name",self.search_box_field_name)

    @allure.severity('CRITICAL')
    def click_on_search_button(self):
        logger.allure_log('clicking on search button in home page')
        self.element_click("search_button_xpath",self.search_button_xpath)
        return SearchPage(self.driver)

    @allure.severity('CRITICAL')
    def click_on_my_account_drop_menu(self):
        logger.allure_log('clicking on my account drop menu in home page')
        self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)

    @allure.severity('CRITICAL')
    def select_login_option(self):
        logger.allure_log('selecting login options in home page')
        self.element_click("login_option_link_text",self.login_option_link_text)
        return LoginPage(self.driver)

    @allure.severity('CRITICAL')
    def navigate_to_login_page(self):
        logger.allure_log('navigating to login page in home page')
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    @allure.severity('CRITICAL')
    def select_register_option(self):
        logger.allure_log('selecting register option in home page')
        self.element_click("register_option_link_text",self.register_option_link_text)
        return RegisterPage(self.driver)

    @allure.severity('CRITICAL')
    def navigate_to_register_page(self):
        logger.allure_log('navigating to register page in home page')
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    @allure.severity('CRITICAL')
    def search_for_a_product(self,product_name):
        logger.allure_log('searching for a product in home page')
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()





