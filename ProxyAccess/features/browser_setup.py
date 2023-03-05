"""Sets up all browser options"""
from selenium import webdriver


def get_options(context):
    """Returns the options for Chrome"""

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    if "noJS" in context.scenario.tags:
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.javascript": 2}
        )

    if is_headless(context):
        options.add_argument("--headless")

    options.add_argument(f"--window-size={get_viewport(context)}")
    return options


def is_headless(context) -> bool:
    """Checks whether to run headless browser or not"""
    return context.config.getboolean("BROWSER", "headless")


def get_viewport(context):
    """Gets viewport in which to run tests"""
    return context.config.get("BROWSER", "viewport")
