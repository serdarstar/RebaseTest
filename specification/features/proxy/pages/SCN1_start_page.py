"""Page Object for Service Start Page"""
from selenium.webdriver.common.alert import Alert

from specification.features.proxy.pages.proxy_base_page import ProxyBasePage
from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement


class StartPage(ProxyBasePage):
    """Contains all interactions for the Service Start Page"""
    start_button = PageElement(By.CSS_SELECTOR, ".nhsuk-button")

    def click_start_button(self):
        """Clicks start button"""
        self.wait.for_page_to_load()
        self.wait.for_element_to_be_present(self.start_button)
        self.interact.click_element(self.start_button)
