"""Blood Pressure tool specific custom expected conditions for Selenium"""


class ImageIsReady:  # pylint: disable=too-few-public-methods
    """This condition checks if an image has been loaded"""

    def __init__(self, finder, page_element):
        self.find = finder
        self.page_element = page_element

    def __call__(self, driver):
        element = self.find.element(self.page_element)
        element_tag = element.tag_name
        element_image_src = element.get_attribute("src")
        if element_tag == "svg" and element_image_src is None:
            return element.is_displayed()

        script = (
            "return ("
            "(arguments[0].complete)"
            "||"
            "(arguments[0].naturalWidth !='undefined' && arguments[0].naturalWidth > 0)"
            ")"
        )

        return driver.execute_script(script, element)
