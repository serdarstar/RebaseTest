# pylint: skip-file
"""Step definitions shared amongst features"""

from behave import *

from ProxyAccess.helpers.user_data_helper import get_user_data


@given("that a user exists with a {user_type} blood pressure level")
def step_impl(context, user_type):
    """Ensures a user exists and sets their details in context"""
    context.user = get_user_data(user_type)
    # for i in context.user['blood_pressure']:
    #     print(i["systolic"])


@then('the "{page_name}" page is displayed')
def step_impl(context, page_name):
    """Ensures page title is displayed and set correctly"""
    context.current_page.verify_title_for_page_by_id(page_name)


@then('the "{page_url}" page url is correct')
def step_impl(context, page_url):
    """Ensures page title is displayed and set correctly"""
    context.current_page.verify_url_for_page_by_id(page_url)


@when("the browser is blocking ads")
def step_impl(context):
    pass


@when('the user clicks on "{action}"')
def step_impl(context, action):
    """Click the Go back link or browser back button"""
    actions = {
        "browser_back": click_browser_back_button,
        "Go_back_link": click_go_back_link,
    }
    return actions[action](context)


@step("the user clicks on browser back then forward button")
def step_impl(context):
    """Click the browser back button then forward button"""
    context.browser.back()
    context.browser.forward()


def click_browser_back_button(context):
    """Click the browser back button"""
    context.browser.back()


def click_go_back_link(context):
    """Click the Go back link"""
    context.current_page.click_go_back_link()


@then('the page has a "{header_type}" header and a "{footer_type}" footer')
def step_impl(context, header_type, footer_type):
    """Checks the required header is present and correct"""
    if header_type == "standard":
        context.current_page.assert_standard_header_visible_and_correct()
    else:
        context.current_page.assert_transactional_header_visible_and_correct()

    """Checks the required footer is present and correct"""
    if footer_type == "standard":
        context.current_page.assert_standard_footer_visible_and_correct()
    else:
        context.current_page.assert_transactional_footer_visible_and_correct()


@when("the user clicks the service name link")
def step_impl(context):
    """Clicks the service name header link"""
    context.current_page.click_header_service_name_link()


@when("the user selects to view the terms and conditions")
def step_impl(context):
    """Clicks the terms and conditions footer link"""
    context.current_page.click_footer_terms_and_conditions_link()


@when("the user selects to view the privacy policy")
def step_impl(context):
    """Clicks the privacy policy footer link"""
    context.current_page.click_footer_privacy_policy_link()
