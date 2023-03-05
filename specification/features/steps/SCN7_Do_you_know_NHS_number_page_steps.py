from behave import *

use_step_matcher("re")


from specification.features.proxy.pages.SCN7_Do_you_know_NHS_number_page import DoYouKnowNHSNumberPage

@when("the user knows NHS number")
def step_impl(context):
    context.current_page = DoYouKnowNHSNumberPage(context.browser, context.LOGGER)
    context.current_page.select_NHS_number_option()
