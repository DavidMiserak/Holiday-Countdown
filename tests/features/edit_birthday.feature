Feature: Edit Birthday
  As a user
  I want to edit an existing birthday
  So that I can update incorrect or outdated birthday information

  Scenario: Successfully edit a birthday
    Given a birthday for "Alice Johnson" exists
    When the user clicks the edit button for "Alice Johnson"
    And changes the name to "Alice Williams"
    And changes the birthday to "1985-09-20"
    And clicks the "Update Birthday" button
    Then the user should see a success message
    And the birthday list should show the updated information
