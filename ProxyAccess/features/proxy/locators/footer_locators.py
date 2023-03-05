"""Page element locators for Page Footers"""
from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


class FooterLocators:  # pylint: disable=too-few-public-methods
    """Contains all elements for the Page footer"""

    footer = PageElement(By.CLASS_NAME, "nhsuk-footer")
    standard_footer_list = PageElement(By.CLASS_NAME, "nhsuk-footer__list")
    terms_and_conditions = PageElement(By.LINK_TEXT, "Terms and Conditions")
    privacy_policy = PageElement(By.LINK_TEXT, "Privacy policy")
