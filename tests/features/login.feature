@Login-Page
Feature: Contact list login page
  As a user
  I want to sign in
  so I can access the homepage

  Background:
    Given a user is on the login page


  @Smoke
  Scenario: Basic Login
    When a user enters an email: "test@test.com"
    And a user enters a password: "1234567"
    And a user clicks submit
    Then the home page is displayed
    And a success alert is displayed


  Scenario: Invalid email address
    When a user enters an email: "test1@test.com"
    And a user clicks submit
    Then the login page is displayed
    And an error alert is displayed


  Scenario: Invalid password
    When a user enters an email: "test@test.com"
    And a user enters a password: "password"
    And a user clicks submit
    Then the login page is displayed
    And an error alert is displayed