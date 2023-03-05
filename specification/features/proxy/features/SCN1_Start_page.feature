Feature: Proxy Access Start Page

  Background:
    Given the user opens the start page

  Scenario: Common validations
    Then the "start" page is displayed
    Then the "start" page url is correct

  Scenario: Ensure that start page loads and works as expected
    Then the user clicks on "Start now"

