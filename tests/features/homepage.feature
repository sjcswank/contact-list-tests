Feature: Contacts list home page
  as an authenticated user
  I want to access the homepage
  so I can interact with my contacts

  Background:
    Given a user is on the login page
    When a user enters an email: "test@test.com"
    And a user enters a password: "1234567"
    And a user clicks submit

#
#  Scenario: Add Contact
#    When a user enters a contact name: "First Last"
#    And a user enters a contact phone number: "555 123 4567"
#    And a user enters a contact email: "email@email.com"
#    And a user enters a contact address: "123 Test St."
#    And a user clicks submit
#    Then a contact for "First Last" is displayed in the contact list


  Scenario: Delete Contact
    When a user enters a contact name: "First Last"
    And a user enters a contact phone number: "555 123 4567"
    And a user enters a contact email: "email@email.com"
    And a user enters a contact address: "123 Test St."
    And a user clicks submit
    And a user clicks the delete button for "First Last"
    Then a contact for "First Last" will not be displayed in the contact list