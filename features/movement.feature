Feature: Mapping movement
  In order to use distance from starting point in a useful application
  As a controller
  I want the robot to complete the distance from its starting point

  Scenario Outline: Detect circles or no
    Given a robot
    And a valid <instruction> file
    When the robot is instructed to operate
    Then the robot notifies '<distance>' units
    And the robot returns <circle>

    Examples: turns only no circle
    | instruction                                                   | distance | circle  |
    | features/data/turnsonlynocircle.instructions                  | 0.000    | False   |
    | features/data/fourturns.instructions                          | 0.000    | False    |
    | features/data/eightturns.instructions                         | 2.000    | True    |
    | features/data/movementonly.instructions                       | 5.000    | False   |
    | features/data/movementincludingturnsnocircle.instructions     | 2.828    | False   |
    | features/data/movementincludingturnsonecircle.instructions    | 4.000    | True    |
    | features/data/movementincludingturnsmanycircles.instructions  | 2.236    | True    |
    | features/data/movementincludinglargecircle.instructions       | 3.000    | True    |
    | features/data/movementincludingretracementcircle.instructions | 0.000    | True    |
