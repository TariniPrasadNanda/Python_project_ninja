from selenium.webdriver.common.by import By
import utilities.logs as logger
import allure


@allure.epic('Base Page')
class BasePage:
    @allure.severity('CRITICAL')
    def __init__(self, driver):
        logger.allure_log('Running Constructor of Base page')
        self.driver = driver

    @allure.severity('CRITICAL')
    def type_into_element(self,text,locator_name,locator_value):
        logger.allure_log('entering value for locators name and value in base page')
        element = self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    @allure.severity('CRITICAL')
    def element_click(self,locator_name,locator_value):
        logger.allure_log('clicking on elements in base page')
        element = self.get_element(locator_name,locator_value)
        element.click()

    @allure.severity('CRITICAL')
    def check_display_status_of_element(self,locator_name,locator_value):
        logger.allure_log('checking display status of element in base page')
        element = self.get_element(locator_name,locator_value)
        return element.is_displayed()

    @allure.severity('CRITICAL')
    def retrieve_element_text(self,locator_name,locator_value):
        logger.allure_log('retrieving element text in base page')
        element = self.get_element(locator_name,locator_value)
        return element.text

    @allure.severity('CRITICAL')
    def get_element(self,locator_name,locator_value):
        logger.allure_log('getting elements in base page')
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

