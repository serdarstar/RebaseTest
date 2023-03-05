from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from ProxyAccess.features.proxy.pages.proxy_base_page import ProxyBasePage


class DoYouKnowNHSNumberPage(ProxyBasePage):
    yes = PageElement(By.XPATH, "//input[@id='know-nhs-number-1']")
    no = PageElement(By.XPATH, "//input[@id='know-nhs-number-2']")
    continue_element = PageElement(By.XPATH, "//button[@type='submit']")

    def select_NHS_number_option(self):
        self.interact.click_element(self.yes)
        self.interact.click_element(self.continue_element)
