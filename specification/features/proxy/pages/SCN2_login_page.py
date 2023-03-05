from selenium.webdriver.common.by import By
from uitestcore.page_element import PageElement
from specification.features.proxy.pages.proxy_base_page import ProxyBasePage


class LoginPage(ProxyBasePage):
    email = PageElement(By.XPATH, "//input[@id='email']")
    continueElement = PageElement(By.XPATH, "//button[@type='submit']")

    def enter_email(self, email):
        self.interact.send_keys(self.email, email)

    def click_continue(self):
        self.interact.click_element(self.continueElement)
