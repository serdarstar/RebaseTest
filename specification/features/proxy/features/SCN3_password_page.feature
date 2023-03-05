Feature: Password page feature
  Background:
    Given the user opens the start page
    Then the user clicks on "Start now"
    Then the user logs in with "serdar.yildiz1@nhs.net"
    Then the user clicks on continue for password

  Scenario: Login
    Then the user enters password as "12345"
    Then the user clicks on continue on password page
