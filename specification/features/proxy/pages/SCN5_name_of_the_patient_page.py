from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from specification.features.proxy.pages.proxy_base_page import ProxyBasePage


class NameOfThePatientPage(ProxyBasePage):
    first_name = PageElement(By.XPATH, "//input[@id='first-name']")
    last_name = PageElement(By.XPATH, "//input[@id='last-name']")
    continue_element= PageElement(By.XPATH, "//button[@class='nhsuk-button']")

    def enter_first_and_last_name(self):
        self.interact.send_keys(self.first_name, "Serdar")
        self.interact.send_keys(self.last_name, "Yildiz")
        self.interact.click_element(self.continue_element)
