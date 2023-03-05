"""Page Object for general Blood Pressure tool interactions"""
import json

from hamcrest import assert_that, equal_to
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait
from uitestcore.page import BasePage

from ProxyAccess.features.proxy.helpers import bp_custom_expected_conditions
from ProxyAccess.features.proxy.locators.footer_locators import FooterLocators
from ProxyAccess.features.proxy.locators.header_locators import HeaderLocators
from ProxyAccess.features.proxy.locators.shared_locators import SharedLocators

FIELD_VALIDATION_FILEPATH = "ProxyAccess/features/data/errors/field_validation.json"

EXPECTED_NHS_FOOTER_LINKS = (
    "NHS sites\nNHS App\nAbout us\nContact us\nProfile editor login"
    "\nSite map\nAccessibility statement\nOur policies\nCookies"
)


class ProxyBasePage(BasePage):
    """Members of this class may be useful across the whole journey"""

    def __init__(self, driver, logger):
        super().__init__(driver, existing_logger=logger)
        self.webdriver_wait = WebDriverWait(self.driver, self.wait.wait_time)

    def verify_title_for_page_by_id(self, page_name):
        """Verifies the title of a page based on the title stored in the page_titles.json file"""
        file_path = "ProxyAccess/features/data/content/page_titles.json"
        expected_title = self.get_content_dict(file_path)[page_name]
        try:
            self.webdriver_wait.until(title_is(expected_title))
        except TimeoutException as exception:
            raise AssertionError(
                f"\nExpected title: {expected_title}"
                f"\nGot title: {self.driver.title}"
            ) from exception

    def verify_url_for_page_by_id(self, page_url):
        """Verifies the title of a page based on the title stored in the page_titles.json file"""
        file_path = "ProxyAccess/features/data/content/page_urls.json"
        expected_url = self.get_content_dict(file_path)[page_url]
        actual_url = self.interrogate.get_current_url()

        print(expected_url)
        print(actual_url)

        try:
            assert actual_url == expected_url
        except TimeoutException as exception:
            raise AssertionError(
                f"\nExpected title: {expected_url}"
                f"\nGot title: {self.driver.title}"
            ) from exception

    def assert_standard_header_visible_and_correct(self):
        """Verifies the standard header is visible"""
        self.wait.for_element_to_be_present(HeaderLocators.standard_header)
        assert_that(
            self.interrogate.is_element_visible(HeaderLocators.nhs_logo),
            equal_to(True),
            "NHS Logo",
        )
        assert_that(
            self.interrogate.is_element_visible(HeaderLocators.search_form),
            equal_to(True),
            "NHS Search form",
        )

    def assert_standard_footer_visible_and_correct(self):
        """Verifies the standard footer is visible"""
        self.wait.for_element_to_be_present(FooterLocators.footer)
        assert_that(
            self.interrogate.is_element_visible(FooterLocators.standard_footer_list),
            equal_to(True),
            "NHS footer list",
        )
        assert_that(
            self.interrogate.get_text(FooterLocators.standard_footer_list),
            equal_to(EXPECTED_NHS_FOOTER_LINKS),
        )

    def assert_transactional_header_visible_and_correct(self):
        """Verifies the transactional header is visible"""
        self.wait.for_element_to_be_present(HeaderLocators.transactional_header)
        assert_that(
            self.interrogate.is_element_visible(HeaderLocators.service_name_link),
            equal_to(True),
            "Service name link",
        )
        assert_that(
            self.interrogate.is_element_visible(HeaderLocators.nhs_logo),
            equal_to(True),
            "NHS Logo",
        )

    def assert_transactional_footer_visible_and_correct(self):
        """Verifies the transactional footer is visible"""
        self.wait.for_element_to_be_present(FooterLocators.footer)
        assert_that(
            self.interrogate.is_element_visible(FooterLocators.terms_and_conditions),
            equal_to(True),
            "Terms and conditions link",
        )
        assert_that(
            self.interrogate.is_element_visible(FooterLocators.privacy_policy),
            equal_to(True),
            "Privacy policy link",
        )

    def user_presses_tab_key(self):
        """Activates the Skip To Main Content link"""
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.perform()

    def user_skips_to_main_content(self):
        """Verifies and click the Skip To Main Content link"""
        elem = self.driver.switch_to.active_element
        assert_that(elem.get_property("text"), equal_to("Skip to main content"))
        elem.click()

    def verify_main_content_is_active(self):
        """Verifies active element is the main content"""
        elem = self.driver.switch_to.active_element
        assert_that(elem.get_property("id"), equal_to("maincontent"))

    def scroll_to_element(self, element):
        """Scrolls page to specified page element"""
        self.interact.scroll_into_view(element)

    def wait_for_image_to_be_visible(self, page_element):
        """
        Wait for element to be visible, using a selenium expected condition
        :param page_element: PageElement instance representing the element
        :return:
        """
        WebDriverWait(self.driver, self.wait.wait_time).until(
            bp_custom_expected_conditions.ImageIsReady(self.find, page_element)
        )

    @staticmethod
    def get_content_dict(file_path):
        """Takes a json file path and returns that file as a dict object"""
        with open(file_path, encoding="utf-8") as content:
            return json.load(content)

    def click_go_back_link(self):
        """Clicks Go back link"""
        self.wait.for_page_to_load()
        self.interact.click_element(SharedLocators.go_back_link)

    def click_header_service_name_link(self):
        """Clicks header service name link"""
        self.wait.for_page_to_load()
        self.interact.click_element(HeaderLocators.service_name_link)

    def click_footer_terms_and_conditions_link(self):
        """Clicks footer terms and conditions link"""
        self.wait.for_page_to_load()
        self.interact.click_element(FooterLocators.terms_and_conditions)

    def click_footer_privacy_policy_link(self):
        """Clicks footer privacy policy link"""
        self.wait.for_page_to_load()
        self.interact.click_element(FooterLocators.privacy_policy)

    def assert_error_summary_displayed(self):
        """Verifies error summary is displayed"""
        self.wait.for_page_to_load()
        assert_that(
            self.interrogate.is_element_visible(SharedLocators.error_summary),
            equal_to(True),
            "Error summary",
        )
