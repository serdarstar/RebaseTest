Feature: End-to-End Happy Path

  Scenario: Happy path
    Given the user opens the start page
    Then the "start" page url is correct
    Then the user clicks on "Start now"
    Then the user logs in with "serdar.yildiz1@nhs.net"
    Then the user clicks on continue for password
    Then the user enters password as "12345"
    Then the user clicks on continue on password page
    When the user confirm details
    Then the user enter the name of the patient
    Then the user enters date of birth of the patient
    When the user knows NHS number