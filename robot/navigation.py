from math import sqrt
from . import directions


class Navigation:
    __x = 0
    __y = 0
    distance: float = 0
    direction: str = 'n'
    loops: int = 0

    def reset(self):
        self.__x = 0
        self.__y = 0
        self.direction = 'n'
        self.distance = 0
        self.loops = 0

    def navigate(self, instruction: str):
        if instruction == 'F':
            self.__forward()
        else:
            self.__turn(instruction)

    def calculate_distance(self) -> float:
        self.distance = sqrt(self.__x ** 2 + self.__y ** 2)

    def report(self) -> str:
        return "x: " + str(self.__x) + " y: " + str(self.__y) + \
               " direction: " + self.direction + " distance: " + str(self.distance) + " loops: " + str(self.loops)

    def __move(self):
        cartesian = {'n' : (0, 1), 's': (0,-1), 'w': (-1, 0), 'e': (1, 0)}
        self.__x += cartesian[self.direction][0]
        self.__y += cartesian[self.direction][1]

    def __forward(self):
        self.__move()
        self.__detect_loops()

    def __turn(self, instruction: str):
        self.direction = directions.do_turn(self.direction, instruction)

    def __detect_loops(self):
        if self.__x == 0 and self.__y == 0:
            self.loops += 1
