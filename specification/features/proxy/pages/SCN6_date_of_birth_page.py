from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from specification.features.proxy.pages.proxy_base_page import ProxyBasePage


class DateOfBrithPage(ProxyBasePage):
    day = PageElement(By.XPATH, "//input[@id='day']")
    month = PageElement(By.XPATH, "//input[@id='month']")
    year = PageElement(By.XPATH, "//input[@id='year']")
    continue_element = PageElement(By.XPATH, "//a[@class='nhsuk-button']")

    def enter_date_of_bith(self):
        self.interact.send_keys(self.day, "21")
        self.interact.send_keys(self.month, "01")
        self.interact.send_keys(self.year, "2001")
        self.interact.click_element(self.continue_element)
