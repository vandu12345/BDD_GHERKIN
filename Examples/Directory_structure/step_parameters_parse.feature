# Example

Feature: Passing parameters to steps

Scenario: method 1 of passing step parameters


    Given I have a new 'DVD' in my cart
    And I have a new "BOOK" in my cart
    When I click on "Next"
    And I click on "FINISH"
    Then I should see "error"

Scenario: Add 10 participants in the call

    Given I start a call with "10" participants