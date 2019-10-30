from pytest_bdd import (scenarios, given, when, then, parsers)

from core.commons import CommonFunctions
from tests.pageobjects.homescreen import HomeScreen
from tests.pageobjects.resultsscreen import ResultsScreen

scenarios('../features/web.feature')


# Given Steps
@given(parsers.parse('the wikipedia home page is displayed'))
def navigate_to_app_homepage(driver):
    driver.get(CommonFunctions().get_star_json(key_name='WEB', sub_key_name='URLS', sub_sub_key_name='QA'))


# When Steps
@when(parsers.parse('the user searches for "<name>"'))
def enter_name_in_searchbox(driver, name):
    search = HomeScreen(driver)
    search.enter_text_in_searchbox(name)


# Then Steps
@then(parsers.parse('results are shown for "<name>"'))
def validate_header_value(driver, name):
    header = ResultsScreen(driver)
    header.verify_header_text(name)
    header.verify_full_name_text(name)
    print('this is a print statement in the test_web file')
