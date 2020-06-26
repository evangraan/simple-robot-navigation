import os
import sys

sys.path.insert(0, os.getcwd())

import unittest
from prototype.navigate import navigate
from prototype.calculate_distance import calculate_distance
from prototype.detect_loops import detect


class TestAlgorithms(unittest.TestCase):

    def test_navigation(self):
        x, y = navigate(['L', 'F', 'F'])
        assert (x == -2)
        assert (y == 0)

        x, y = navigate(['F', 'F', 'F', 'L', 'F', 'R', 'R', 'F', 'F'])
        assert (x == 1)
        assert (y == 3)

    def test_distance(self):
        assert (calculate_distance(1, 1) == "1.414 units")
        assert (calculate_distance(99, 21) == "101.203 units")

    def test_loop_detection(self):
        assert (detect(['L', 'F', 'F']) == False)
        assert (detect(['L', 'L', 'L', 'L']) == False)
        assert (detect(['F', 'R', 'F', 'R', 'F', 'R', 'F', 'L', 'L', 'L', 'L']) == True)


if __name__ == '__main__':
    unittest.main()
