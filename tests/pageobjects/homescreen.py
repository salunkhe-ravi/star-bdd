import allure

from core.wrappers import WrapperFunctions


class HomeScreen(WrapperFunctions):
    SEARCH_BOX_BY_NAME = 'search'
    SEARCH_BTN_BY_XPATH = "//i[text()='Search']"

    def __init__(self, driver):
        super(HomeScreen, self).__init__(driver)

    @allure.step
    def enter_text_in_searchbox(self, search_text):
        # self.search_box.send_keys(search_text + Keys.RETURN)
        self.enter_text(search_text, self.SEARCH_BOX_BY_NAME, 'name')
        self.click_element(self.SEARCH_BTN_BY_XPATH, 'xpath')
