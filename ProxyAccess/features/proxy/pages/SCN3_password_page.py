from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from ProxyAccess.features.proxy.pages.proxy_base_page import ProxyBasePage


class PasswordPage(ProxyBasePage):
    passwordElement = PageElement(By.XPATH, "//input[@id='password']")
    continueElement = PageElement(By.XPATH, "//a[@class='nhsuk-button']")

    def enter_password(self, password):
        self.interact.send_keys(self.passwordElement, password)

    def click_continue(self):
        self.interact.click_element(self.continueElement)