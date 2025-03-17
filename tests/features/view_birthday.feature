Feature: View Birthdays
  As a user
  I want to view my list of birthdays
  So that I can see upcoming birthdays and their countdowns

  Scenario: View birthday list when birthdays exist
    Given some birthdays have been added
    When the user navigates to the home page
    Then the user should see a list of birthdays
    And each birthday should display a countdown timer

  Scenario: View empty birthday list
    Given no birthdays have been added
    When the user navigates to the home page
    Then the user should see a message suggesting to add a birthday
