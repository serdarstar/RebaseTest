"""Page element locators for Enter Your Reading Page"""
from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


class EnterReadingPageLocators:  # pylint: disable=too-few-public-methods
    """Contains all elements for the Enter Your Reading page"""

    systolic_field = PageElement(By.ID, "nhsuk-bp_your-details_reading_sys")
    diastolic_field = PageElement(By.ID, "nhsuk-bp_your-details_reading_dia")
    continue_button = PageElement(By.ID, "nhsuk-bpt_reading_continue")
