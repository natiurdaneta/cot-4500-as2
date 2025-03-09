import numpy as np

# Neville's Method
def neville_method(x, y, target):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((target - x[i - j]) * Q[i, j - 1] - (target - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])
    return Q[n - 1, n - 1]

# Newton's Forward Method
def newton_forward_method(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for i in range(1, n):
        for j in range(1, i + 1):
            F[i, j] = F[i, j - 1] - F[i - 1, j - 1]
    return F

# Divided Difference Method for Hermite Polynomial
def divided_difference_method(x, y, y_prime):
    n = len(x)
    Q = np.zeros((2 * n, 2 * n))
    for i in range(n):
        Q[2 * i, 0] = y[i]
        Q[2 * i + 1, 0] = y[i]
        if i != 0:
            Q[2 * i, 1] = (Q[2 * i, 0] - Q[2 * i - 1, 0]) / (x[i] - x[i - 1])
        Q[2 * i + 1, 1] = y_prime[i]
    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i, j] = (Q[i, j - 1] - Q[i - 1, j - 1]) / (x[i // 2] - x[(i - j) // 2])
    return Q

# Cubic Spline Interpolation
def cubic_spline_interpolation(x, y):
    n = len(x)
    h = np.diff(x)
    A = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
    A[0, 0] = 1
    A[-1, -1] = 1
    c = np.linalg.solve(A, b)
    return A, b, c

# Question 1: Neville's Method
x1 = [3.6, 3.8, 3.9]
y1 = [1.675, 1.436, 1.318]
target1 = 3.7
result1 = neville_method(x1, y1, target1)
print(f"Question 1: Neville's Method Result for f(3.7): {result1}")

# Question 2: Newton's Forward Method
x2 = [7.2, 7.4, 7.5, 7.6]
y2 = [23.5492, 25.3913, 26.8224, 27.4589]
F = newton_forward_method(x2, y2)
print("Question 2: Newton's Forward Method Table:")
print(F)

# Question 3: Approximate f(7.3) using Newton's Forward Method
target2 = 7.3
result2 = neville_method(x2, y2, target2)
print(f"Question 3: Approximation for f(7.3): {result2}")

# Question 4: Divided Difference Method for Hermite Polynomial
x4 = [3.6, 3.8, 3.9]
y4 = [1.675, 1.436, 1.318]
y_prime4 = [-1.195, -1.188, -1.182]
Q = divided_difference_method(x4, y4, y_prime4)
print("Question 4: Hermite Polynomial Approximation Matrix:")
print(Q)

# Question 5: Cubic Spline Interpolation
x5 = [2, 5, 8, 10]
y5 = [3, 5, 7, 9]
A, b, c = cubic_spline_interpolation(x5, y5)
print("Question 5: Cubic Spline Interpolation Results:")
print("Matrix A:")
print(A)
print("Vector b:")
print(b)
print("Vector c:")
print(c)
