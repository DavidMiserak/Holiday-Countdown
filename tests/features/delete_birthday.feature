Feature: Delete Birthday
  As a user
  I want to delete a birthday
  So that I can remove outdated or incorrect birthday entries

  Scenario: Successfully delete a birthday
    Given a birthday for "Jane Smith" exists
    When the user clicks the delete button for "Jane Smith"
    And confirms the deletion
    Then the birthday for "Jane Smith" should be removed from the list
