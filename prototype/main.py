import os
import sys

sys.path.insert(0, os.getcwd())

from prototype.navigate import navigate
from prototype.calculate_distance import calculate_distance
from prototype.detect_loops import detect

if __name__ == "__main__":
    instruction_file = sys.argv[1]

    file = open(instruction_file)
    instructions = [instruction.rstrip('\r\n').lstrip().rstrip() for instruction in file.readlines() if
                    instruction.rstrip('\r\n').lstrip().rstrip()]
    file.close()

    x, y = navigate(instructions)
    distance = calculate_distance(x, y)
    looped = detect(instructions)

    print(distance)
    print(looped)
