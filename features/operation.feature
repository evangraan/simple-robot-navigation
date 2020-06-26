Feature: Operation
  In order to perform a task
  As a robot
  I want to interpret and operate on instructions
  Using an instruction file

  Scenario Outline: Forward
    Given a robot
    And a valid <instruction> file
    When the robot is instructed to move 'F'
    Then the robot notifies <moves> along its current direction
    And the robot does not change <direction>

    Examples: forward
    | instruction                        | moves | direction |
    | features/data/forward.instructions | 1.000 | n         |

  Scenario Outline: Left
    Given a robot
    And a valid <instruction> file
    When the robot is instructed to move 'L'
    Then the robot does not move <position>
    And the robot changes <direction> by 90 degrees accordingly

    Examples: left
    | instruction                     | position | direction |
    | features/data/left.instructions | 0.000    | w         |

  Scenario Outline: Right
    Given a robot
    And a valid <instruction> file
    When the robot is instructed to move 'R'
    Then the robot does not move <position>
    And the robot changes <direction> by 90 degrees accordingly

    Examples: right
    | instruction                     | position | direction |
    | features/data/right.instructions | 0.000    | e         |

  Scenario: No more operations
    Given a robot
    And a valid instruction file
    When the robot is instructed to operate
    And the robot has executed all valid instructions
    Then the robot does not move
    And the robot does not turn
    And the robot notifies the distance traveled
    And the robot notifies whether a circle was completed