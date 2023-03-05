import time

from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from ProxyAccess.features.proxy.pages.proxy_base_page import ProxyBasePage


class CheckYourDetailsPage(ProxyBasePage):
    yes_option = PageElement(By.XPATH, "//input[@id='contact-details-1']")
    continue_element = PageElement(By.XPATH, "//button[@type='submit']")

    def click_yes(self):
        self.interact.click_element(self.yes_option)
        self.interact.click_element(self.continue_element)
