def navigate(instructions):
    x = 0
    y = 0
    d = 3  # 3 - north, 2 - west, 1 - south - 0 - east
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
            if d == 3:
                y += 1
            if d == 2:
                x -= 1
            if d == 1:
                y -= 1
            if d == 0:
                x += 1

    return x, y

