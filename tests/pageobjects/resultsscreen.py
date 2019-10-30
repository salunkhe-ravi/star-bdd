from core.commons import CommonFunctions
from core.wrappers import WrapperFunctions


class ResultsScreen(WrapperFunctions):
    # Page Element Locators
    HEADING_BY_ID = 'firstHeading'
    FULL_NAME_BY_XPATH = "(//th[@scope='row']//following::td[@class='nickname'])[1]"

    def __init__(self, driver):
        super(ResultsScreen, self).__init__(driver)

    def verify_header_text(self, text):
        header_text = self.get_element_text(self.HEADING_BY_ID, 'id')
        self.verify_text_equals(actual_text=header_text, expected_text=text)
        CommonFunctions().report_logger(step_name='verify_header_text',
                                        log_details='verify_header_text log details')

    def verify_full_name_text(self, text):
        text = 'Sachin'
        full_name_text = self.get_element_text(self.FULL_NAME_BY_XPATH, 'xpath')
        self.verify_text_equals(actual_text=full_name_text, expected_text=text)
        CommonFunctions().report_logger(step_name='verify_full_name_text',
                                        log_details='verify_full_name_text log details')
