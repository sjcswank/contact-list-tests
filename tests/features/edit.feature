Feature: Contacts list edit page
  As an authenticated user
  I want to access the edit page
  so I can update the information on my contacts

  Background:
    Given a user is on the login page
    When a user enters an email: "test@test.com"
    And a user enters a password: "1234567"
    And a user clicks submit
    And a user enters a contact name: "First Last"
    And a user enters a contact phone number: "555 123 4567"
    And a user enters a contact email: "email@email.com"
    And a user enters a contact address: "123 Test St."
    And a user clicks submit
    And a user clicks the edit button for "First Last"


  Scenario: Edit page displays contact info
    Then the edit page for "First Last" will be displayed


  Scenario: Update contact
    When a user clears the contact name input
    And a user enters a contact name: "New Last"
    And a user clicks submit
    Then a contact for "New Last" is displayed in the contact list
    And a contact for "First Last" will not be displayed in the contact list