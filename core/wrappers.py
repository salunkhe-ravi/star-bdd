#####################################################
####
# Description : Wrapper methods for selenium library
# Developer : Ravi Salunkhe(ravi.salunkhe@mastek.com)
# Modified Date : 3rd Oct 2019
####
######################################################
import logging
from traceback import print_stack

import allure
import pytest
from selenium.webdriver.common.by import By

from core.star_logger import star_log


class WrapperFunctions():
    __author__ = 'Ravi Salunkhe'

    log = star_log(log_level=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        # self.name = name

    def get_by_type(self, locator_type):
        """
        Returns the By type object for a given locator_type
        :param locator_type:
        :return:
        """
        try:
            locator_type = locator_type.lower()
            if locator_type == "id":
                return By.ID
            elif locator_type == "name":
                return By.NAME
            elif locator_type == "xpath":
                return By.XPATH
            elif locator_type == "css":
                return By.CSS_SELECTOR
            elif locator_type == "class_name":
                return By.CLASS_NAME
            elif locator_type == "link_text":
                return By.LINK_TEXT
            elif locator_type == "partial_link_text":
                return By.PARTIAL_LINK_TEXT
            elif locator_type == "tag_name":
                return By.TAG_NAME
            else:
                self.log.info("Locator type ==> " + locator_type + " not correct or supported")
                # print("Locator type : " + locator_type + " not correct or supported")
                return False
        except:
            self.log.info('Issue with locator type ==> ' + locator_type)

    def get_element(self, locator, locator_type="id"):
        """
        Get you the reference to the desired web element
        :param locator:
        :param locator_type:
        :return:
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator ==> " + locator + " and locator_type ==> " + locator_type)
        except:
            self.log.info("Element NOT found with locator ==> " + locator + " and locator_type ==> " + locator_type)
        return element

    def enter_text(self, data, locator, locator_type="id"):
        """
        Enter the required data in a web element
        :param data:
        :param locator:
        :param locator_type:
        :return:
        """
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info(
                "Entered " + data + " on element with locator ==> " + locator + " and locator_type ==> " + locator_type)
        except:
            self.log.info(
                "Unable to enter " + data + " in element with locator ==> " + locator + " and locator_type ==> " + locator_type)
            print_stack()

    def get_element_text(self, locator, locator_type="id"):
        """
        Gets you the text of an element
        :param locator:
        :param locator_type:
        :return: element text
        """
        text = None
        try:
            element = self.get_element(locator, locator_type)
            text = element.text
            self.log.info(
                "Element text captured as " + text + " on element with locator ==> " + locator + " and locator_type ==> " + locator_type)
        except:
            self.log.info(
                "Unable to capture text from  element with locator ==> " + locator + " and locator_type ==> " + locator_type)
            print_stack()
        return text

    def get_browser_title(self):
        """
        Retrieves your the browser title
        :return: browser or driver title
        """
        return self.driver.title

    def get_element_list(self, locator, locator_type="id"):
        """
        Gets us the list of web elements
        :param locator:
        :param locator_type:
        :return:
        """
        element = None
        try:
            by_type = self.getByType(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator ==> " + locator +
                          " and locator_type ==> " + locator_type)
        except:
            self.log.info("Element list not found with locator ==> " + locator +
                          " and locator_type ==> " + locator_type)
        return element

    def click_element(self, locator="", locator_type="id", element=None):
        """
        Click on the required element
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator ==> " + locator +
                          " locator_type ==> " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator ==> " + locator +
                          " locator_type ==> " + locator_type)
            print_stack()

    def clear_field(self, locator="", locator_type="id"):
        """
        Clears an element field
        :param locator:
        :param locator_type:
        :return:
        """
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info("Clear field with locator ==> " + locator +
                          " locator_type ==> " + locator_type)
        except:
            self.log.info('Unable to clear field with locator as ==> ' + locator + ' locator_type ==> ' + locator_type)

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator ==> " + locator +
                              " locator_type ==> " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator ==> " + locator +
                              " locator_type ==> " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locator_type: id/name/xpath/class_name
        :param element:
        :return:
        """

        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed | locator ==> " + locator + " locator_type ==> " + locator_type)
            else:
                self.log.info("Element not displayed | locator ==> " + locator + " locator_type ==> " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    @allure.step
    def verify_text_equals(self, actual_text, expected_text):
        """
        Function to compare, verify and log element text value
        :param actual_text:
        :param expected_text:
        :return:
        """
        pytest.assume(actual_text == expected_text)
        self.log.info("ASSERTION :: Actual Value = " + actual_text + " with Expected Value as = " + expected_text)
