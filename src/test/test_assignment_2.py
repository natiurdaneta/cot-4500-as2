import unittest
from src.main.assignment_2 import neville_method, newton_forward_method, divided_difference_method, cubic_spline_interpolation

class TestAssignment2(unittest.TestCase):
    def test_neville_method(self):
        x = [3.6, 3.8, 3.9]
        y = [1.675, 1.436, 1.318]
        target = 3.7
        result = neville_method(x, y, target)
        self.assertAlmostEqual(result, 1.528, places=3)

    def test_newton_forward_method(self):
        x = [7.2, 7.4, 7.5, 7.6]
        y = [23.5492, 25.3913, 26.8224, 27.4589]
        F = newton_forward_method(x, y)
        self.assertAlmostEqual(F[3, 3], 0.0, places=4)

    def test_divided_difference_method(self):
        x = [3.6, 3.8, 3.9]
        y = [1.675, 1.436, 1.318]
        y_prime = [-1.195, -1.188, -1.182]
        Q = divided_difference_method(x, y, y_prime)
        self.assertAlmostEqual(Q[2, 2], -0.05, places=2)

    def test_cubic_spline_interpolation(self):
        x = [2, 5, 8, 10]
        y = [3, 5, 7, 9]
        A, b, c = cubic_spline_interpolation(x, y)
        self.assertAlmostEqual(A[1, 1], 6.0, places=1)

if __name__ == "__main__":
    unittest.main()
