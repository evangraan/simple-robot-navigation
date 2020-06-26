from math import sqrt


def calculate_distance(x, y):
    return "{:.3f} units".format(sqrt(x ** 2 + y ** 2))  # Simple pythagoras as we always measure from origin