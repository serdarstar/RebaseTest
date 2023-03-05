from behave import *

use_step_matcher("re")
from ProxyAccess.features.proxy.pages.SCN4_check_your_details_page import CheckYourDetailsPage


@when("the user confirm details")
def step_impl(context):
    context.current_page = CheckYourDetailsPage(context.browser, context.LOGGER)
    context.current_page.click_yes()
