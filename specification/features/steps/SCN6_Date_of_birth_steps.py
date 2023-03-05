from behave import *

use_step_matcher("re")


from specification.features.proxy.pages.SCN6_date_of_birth_page import DateOfBrithPage
@then("the user enters date of birth of the patient")
def step_impl(context):
    context.current_page = DateOfBrithPage(context.browser, context.LOGGER)
    context.current_page.enter_date_of_bith()
