def turn_left(direction: str) -> str:
    directions = {'n': 'w', 's': 'e', 'w': 's', 'e': 'n'}
    return directions[direction]


def turn_right(direction: str) -> str:
    directions = {'n': 'e', 's': 'w', 'w': 'n', 'e': 's'}
    return directions[direction]


def do_turn(direction: str, instruction) -> str:
    if instruction == 'R':
        return turn_right(direction)
    if instruction == 'L':
        return turn_left(direction)

