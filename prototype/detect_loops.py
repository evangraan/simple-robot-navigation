def detect(instructions):
    loops = 0
    x = 0
    y = 0
    d = 0  # 0 - north, 1 - west, 2 - south - 3 - east
    for instruction in instructions:
        if instruction == 'L':
            d -= 1
            if d < 0:
                d = 3
        if instruction == 'R':
            d += 1
            if d > 3:
                d = 0
        if instruction == 'F':
            if d == 0:
                y += 1
            if d == 1:
                x -= 1
            if d == 2:
                y -= 1
            if d == 3:
                x += 1
            if x == 0 and y == 0:
                loops += 1

    return loops > 0
