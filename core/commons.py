import json
import time
from traceback import print_stack

import allure


class CommonFunctions():

    def get_browser_mapping(scenario_name=None):
        # CommonFunctions().get_info()
        try:
            if scenario_name is None:
                print('Scenario name :: ' + scenario_name + ' not defined in star.json, please re-check and confirm!')
            else:
                scenario_name = scenario_name.upper()
                browser_type = CommonFunctions().get_star_json(key_name='WEB', sub_key_name='BROWSER_MAPPING',
                                                               sub_sub_key_name=scenario_name)
                print('browser_type is ' + str(browser_type))
                return browser_type
        except:
            print(print_stack())
            print('Error while getting the browser mapping')

    def get_star_json(self, key_name, sub_key_name=None, sub_sub_key_name=None):
        try:
            print('inside json loads')
            data = json.loads(open('././star.json').read())
            if sub_key_name is None and sub_sub_key_name is None:
                key_name = key_name.upper()
                print('key_name :::' + key_name)
                print(data[key_name])
                return data[key_name]
            elif sub_sub_key_name is None:
                key_name = key_name.upper()
                sub_key_name = sub_key_name.upper()
                print('printing values now :: ' + data[key_name][sub_key_name])
                return data[key_name][sub_key_name]
            else:
                key_name = key_name.upper()
                sub_key_name = sub_key_name.upper()
                sub_sub_key_name = sub_sub_key_name.upper()
                print('printing values now :: ' + data[key_name][sub_key_name][sub_sub_key_name])
                return data[key_name][sub_key_name][sub_sub_key_name]
        except:
            print(print_stack())
            print('Error reading data from star.json')

    def take_screenshot(self, driver, message='test'):
        try:
            file_name = message + '_' + str(round(time.time() * 1000)) + '.png'
            screenshot_path = '././screenshots/' + file_name
            driver.save_screenshot(screenshot_path)
            print('Screenshot saved successfully to ' + screenshot_path)
        except:
            print(print_stack())
            print_stack('Error taking screenshot!')

    @allure.step
    def report_logger(self, step_name, log_details):
        with allure.step(step_name):
            log_details
