import sys
from robot.robot import Robot

if __name__ == "__main__":
    robot = Robot()

    instruction_file = None
    if len(sys.argv) > 1:
        instruction_file = sys.argv[1]

    result = robot.operate(instruction_file, debug=False)
    distance = robot.nav.distance
