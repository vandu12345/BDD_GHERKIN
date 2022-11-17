Feature: Login in with Valid credentials

    # Feature Description
    # Can have multiple scenarios in a single feature file
Scenario: User login successfully

    # Steps - One or multiple lines starting with keywords : Given,When,Then,And,But

    Given I create a new User
    When I type email
    When I execute using handler 'Node1' the SSH command 'mkdir -p hello'
    # When I type password
    # When I click on 'Login'
    # Then I should see the next Welcome