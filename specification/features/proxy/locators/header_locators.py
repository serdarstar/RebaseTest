"""Page element locators for Page Headers"""
from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


class HeaderLocators:  # pylint: disable=too-few-public-methods
    """Contains all elements for the Page header"""

    transactional_header = PageElement(By.CLASS_NAME, "nhsuk-header--transactional")
    standard_header = PageElement(By.CLASS_NAME, "nhsuk-header")
    nhs_logo = PageElement(By.CLASS_NAME, "nhsuk-logo")
    nhs_logo_link = PageElement(By.CLASS_NAME, "nhsuk-header__link")
    service_name_link = PageElement(
        By.CLASS_NAME, "nhsuk-header__transactional-service-name--link"
    )
    my_account_link = PageElement(By.CLASS_NAME, "nhsuk-account__login--link")
    search_form = PageElement(By.CLASS_NAME, "nhsuk-header__search-form")
    search_input_field = PageElement(By.CLASS_NAME, "nhsuk-search__input")
    search_submit_button = PageElement(By.CLASS_NAME, "nhsuk-search__submit")
