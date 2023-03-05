"""Sets up the environment for use including browsers and browser config"""
import base64
import logging
import os
import time

import allure
#from axe_selenium_python import Axe
from selenium import webdriver
# from selenium.webdriver.common.devtools.v104 import network
#from uitestcore.utilities.browser_handler import BrowserHandler

from specification.features.browser_setup import get_options
from specification.helpers import config_parser  # pylint: disable=[import-error]


def before_all(context):
    """Executes before the whole test suite"""
    context.config = config_parser.get_config(os.environ["env"])
    context.LOGGER = logging.getLogger("selenium_tests")
    context.LOGGER.info("RUNNING PRE-TEST SUITE SETUP")


def before_scenario(context, scenario):  # pylint: disable=[unused-argument]
    """Executes before each test scenario,
    scenario parameter is required by behave, but currently unused"""
    context.scenario_name = scenario.name
    context.browser = webdriver.Chrome(options=get_options(context))
    # if os.environ["env"] == "stag":
    #     user = context.config.get("USER", "user")
    #     password = context.config.get("USER", "password")
    #     authorization = base64.b64encode(f"{user}:{password}".encode("ascii")).decode(
    #         "ascii"
    #     )
    #     auth_dict = {"Authorization": f"Basic {authorization}"}
    #     params = {"headers": network.Headers(auth_dict)}
    #     context.browser.execute_cdp_cmd("Network.enable", {})
    #     context.browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", params)
    context.browser.get(context.config.get("URLs", "ui_url"))
    # context.browser.maximize_window()
    context.LOGGER.info(f"EXECUTING SCENARIO: {scenario.name}")


def after_step(context, step):  # pylint: disable=[unused-argument]
    """Executes after each individual step"""
    js_zoom_out = "document.body.style.zoom='0.25'"
    context.browser.execute_script(js_zoom_out)
    allure.attach(
        context.browser.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
    js_zoom_back = "document.body.style.zoom='1'"
    context.browser.execute_script(js_zoom_back)
    #time.sleep(1)


def after_scenario(context, scenario):  # pylint: disable=[unused-argument]
    """Executes after each scenario"""
    # if context.config.getboolean("A11Y", "generate_reports", fallback=False):
    #     context.axe = Axe(context.browser)
    #     BrowserHandler.run_axe_accessibility_report(
    #         context,
    #         element_filter={
    #             "exclude": [
    #                 ["#nhsuk-cookie-banner"],
    #                 [".nhsuk-skip-link"],
    #                 ["#nhsuk-skip-link"],
    #             ]
    #         },
    #     )
    # context.browser.quit()
    print("here")
    time.sleep(1)
    context.LOGGER.info(f"SCENARIO ENDED: {scenario.name}")
