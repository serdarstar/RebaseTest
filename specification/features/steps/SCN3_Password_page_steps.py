from behave import *

use_step_matcher("re")
from specification.features.proxy.pages.SCN3_password_page import PasswordPage

@then('the user enters password as "(?P<password>.+)"')
def step_impl(context, password):
    context.current_page = PasswordPage(context.browser, context.LOGGER)
    context.current_page.enter_password(password)


@then("the user clicks on continue on password page")
def step_impl(context):
    context.current_page.click_continue()
