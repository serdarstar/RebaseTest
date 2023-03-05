# pylint: skip-file
"""Step definitions for page navigation"""

from behave import when

from specification.features.proxy.pages.enter_reading_page import EnterReadingPage
from specification.features.proxy.pages.SCN1_start_page import StartPage


@when('the user navigates to the "{page}" page')
def step_impl(context, page):
    """Sets the start page as current page"""
    context.current_page = navigate_to(context, page)


@when("the user submits their data")
def step_impl(context):
    """Navigates to the last page in the standard user journey (ie Results page)"""
    context.current_page = navigate_to(context, "results")


def navigate_to(context, page):
    """Navigates to the required tool page"""
    pages = {
        "start": navigate_to_start_page,
        "enter_reading": navigate_to_enter_reading_page,
    }
    return pages[page](context)


def navigate_to_start_page(context):
    """Navigates to the Start page"""
    context.browser.get(context.config.get("URLs", "ui_url"))
    context.current_page = StartPage(context.browser, context.LOGGER)
    return context.current_page


def navigate_to_enter_reading_page(context):
    """Navigates to the Enter Your Reading page"""
    context.current_page = navigate_to_start_page(context)
    context.current_page.click_start_button()
    context.current_page = EnterReadingPage(context.browser, context.LOGGER)
    return context.current_page
