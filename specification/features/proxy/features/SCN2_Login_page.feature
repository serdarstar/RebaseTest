# Created by Serdar.Yildiz at 01/03/2023
Feature: Login page features
  Background:
    Given the user opens the start page
    Then the user clicks on "Start now"

  Scenario Outline: Enter your email
    Then the user logs in with "<email>"
    Examples:
      | email                  |
      | serdar.yildiz1@nhs.net |
