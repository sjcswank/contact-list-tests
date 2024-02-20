Feature: Contacts List Sign Up
  As a user
  I want to be able to sign in
  so I can access the home page

  Background:
    Given the sign up page is displayed

#  Scenario: Basic Sign Up
#    When a user enters an email: "test@test.com"
#    And a user enters a password: "1234567"
#    And a user confirms the password: "1234567"
#    And a user clicks submit
#    Then the home page is displayed
#    And a success alert is displayed

  Scenario: Invalid email
    When a user enters an email: "x@y"
    And a user clicks submit
    Then the sign up page is displayed
    And an error alert is displayed


  Scenario: Invalid password
    When a user enters an email: "test@test.com"
    And a user enters a password: "123"
    And a user clicks submit
    Then the sign up page is displayed
    And an error alert is displayed


  Scenario: Mismatched passwords
    When a user enters an email: "test@test.com"
    And a user enters a password: "1234567"
    And a user confirms the password: "4567890"
    And a user clicks submit
    Then the sign up page is displayed
    And an error alert is displayed