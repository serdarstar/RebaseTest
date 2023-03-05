from behave import *

use_step_matcher("re")
from specification.features.proxy.pages.SCN5_name_of_the_patient_page import NameOfThePatientPage


@then(u'the user enter the name of the patient')
def step_impl(context):
    context.current_page = NameOfThePatientPage(context.browser, context.LOGGER)
    context.current_page.enter_first_and_last_name()
