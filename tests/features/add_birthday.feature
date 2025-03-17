Feature: Add Birthday
  As a user
  I want to add a new birthday
  So that I can track upcoming birthdays

  Scenario: Successfully add a new birthday
    Given the user is on the add birthday page
    When the user enters name "John Doe"
    And the user enters birthday "1990-05-15"
    And the user clicks the "Add Birthday" button
    Then the user should see a success message
    And the birthday for "John Doe" should be in the birthday list
