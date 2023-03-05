"""Page Object for Enter Reading Page"""
from ProxyAccess.features.proxy.locators.enter_reading_page_locators import (
    EnterReadingPageLocators,
)
from ProxyAccess.features.proxy.pages.proxy_base_page import ProxyBasePage


class EnterReadingPage(ProxyBasePage):
    """Contains all interactions for the Enter Reading Page"""

    def enter_bp_readings(self, bp_readings):
        """Enters both the systolic and diastolic blood pressure readings"""
        self.wait.for_page_to_load()
        self.enter_systolic_bp(bp_readings["systolic"])
        self.enter_diastolic_bp(bp_readings["diastolic"])

    def enter_systolic_bp(self, systolic_bp):
        """Enters the systolic blood pressure reading"""
        self.interact.send_keys(EnterReadingPageLocators.systolic_field, systolic_bp)

    def enter_diastolic_bp(self, diastolic_bp):
        """Enters the diastolic blood pressure reading"""
        self.interact.send_keys(EnterReadingPageLocators.diastolic_field, diastolic_bp)

    def click_continue_button(self):
        """Clicks Continue button"""
        self.interact.click_element(EnterReadingPageLocators.continue_button)
