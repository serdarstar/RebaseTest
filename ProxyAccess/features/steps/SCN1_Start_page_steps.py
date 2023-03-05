# pylint: skip-file
"""Step definitions for Service Start Page"""


from behave import *

from ProxyAccess.features.proxy.pages.SCN1_start_page import StartPage
from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


@given("the user opens the start page")
def step_impl(context):
    """Launches the Start page"""
    context.browser.get(context.config.get("URLs", "ui_url"))
    context.current_page = StartPage(context.browser, context.LOGGER)


@when("the user chooses to start the journey")
def step_impl(context):
    """Clicks the Start button to start the user journey"""
    context.browser.click_start_button()


@then("the user logs in")
def step_impl(context):
    context.current_page.enter_credentials()


@then('the user clicks on "Start now"')
def step_impl(context):
    context.current_page.click_start_button()