"""Page element locators for All Pages"""

from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


class SharedLocators:  # pylint: disable=too-few-public-methods
    """Contains shared elements for All Pages"""

    go_back_link = PageElement(By.CLASS_NAME, "nhsuk-back-link__link")
    error_summary = PageElement(By.ID, "nhsuk-hat_error-summary")
