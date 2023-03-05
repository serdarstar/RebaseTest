Feature: Proxy access common features

   Background:
    Given that a user exists with a healthy blood pressure level

  Scenario Outline: The page MUST use the correct page template
    When the user navigates to the "<tool_page>" page
    Then the page has a "<header_type>" header and a "<footer_type>" footer
    Examples:
      | tool_page     | header_type   | footer_type   |
      | start         | standard      | standard      |
      | enter_reading | transactional | transactional |

  Scenario Outline: A user MAY return to the start page by clicking the service name link in the header
    When the user navigates to the "<tool_page>" page
    And the user clicks the service name link
    Then the "start" page is displayed
    Examples:
      | tool_page     |
      | enter_reading |

  Scenario Outline: A user MAY view the service terms and conditions of use
    When the user navigates to the "<tool_page>" page
    And the user selects to view the terms and conditions
    Then the "terms_and_conditions" page is displayed
    Examples:
      | tool_page     |
      | enter_reading |

  Scenario Outline: A user MAY view the service privacy policy
    When the user navigates to the "<tool_page>" page
    And the user selects to view the privacy policy
    Then the "privacy_policy" page is displayed
    Examples:
      | tool_page     |
      | enter_reading |
