import time

from behave import *

use_step_matcher("re")

from ProxyAccess.features.proxy.pages.SCN2_login_page import LoginPage


@then('the user logs in with "(?P<email>.+)"')
def step_impl(context, email):
    context.current_page = LoginPage(context.browser, context.LOGGER)
    context.current_page.enter_email(email)


@then("the user clicks on continue for password")
def step_impl(context):
    context.current_page = LoginPage(context.browser, context.LOGGER)
    context.current_page.click_continue()
