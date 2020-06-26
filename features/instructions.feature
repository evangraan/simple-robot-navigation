Feature: Loading instructions
  In order to direct the robot's movement
  As a robot controller
  I want to provide movement instructions
  Using an instruction file

  Scenario: No instruction file
    Given a robot
    And no instruction file
    When the robot is instructed to operate
    Then the robot notifies 'missing instructions file'

  Scenario: Problem with instruction file
    Given a robot
    And an instruction file that does not exist or cannot be opened
    When the robot is instructed to operate
    Then the robot notifies 'could not open instructions file'

  Scenario: Empty instruction file
    Given a robot
    And an empty instruction file
    When the robot is instructed to operate
    Then the robot notifies 'no instructions in instruction file'

  Scenario: Valid instruction file
    Given a robot
    And a valid instruction file
    When the robot is instructed to operate
    Then the robot performs the instructions
    And the robot notifies the distance traveled
    And the robot notifies whether a circle was completed

  Scenario: Instruction file containing unknown instructions
    Given a robot
    And an instruction file containing some valid and some unknown instructions
    When the robot is instructed to operate
    Then the robot performs the instructions that it understands
    And the robot ignores the instructions it does not understand
    And the robot notifies the distance traveled using valid steps
    And the robot notifies whether a circle was completed
    And the robot notifies 'Warning: some instructions were invalid'

  Scenario: Invalid instruction file
    Given a robot
    And an instruction file with only unknown instructions
    When the robot is instructed to operate
    Then the robot notifies 'no valid instructions in instruction file'
