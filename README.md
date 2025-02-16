# COT-4500 Assignment 2
This repository contains the code for Programming Assignment 2, which covers polynomial interpolation methods such as Neville's method, Newton’s forward method, divided differences, and cubic spline interpolation.

## Description
This repository contains the code for Programming Assignment 2, which covers polynomial interpolation methods such as Neville's method, Newton’s forward method, divided differences, and cubic spline interpolation.

## Requirements
- Python 3.x
- NumPy
- SciPy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/natiurdaneta/cot-4500-as2.git

## Question 1: Neville's Method
```python
import numpy as np

def neville_method(x, y, target):
    n = len(x)
    Q = np.zeros((n, n))
    Q[:, 0] = y
    
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((target - x[i - j]) * Q[i, j - 1] - (target - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])
    
    return Q[n - 1, n - 1]

#Given data
x = np.array([3.6, 3.8, 3.9])
y = np.array([1.675, 1.436, 1.318])

#Target value
target = 3.7

#Compute the interpolated value
result = neville_method(x, y, target)
print(f"Interpolated value at f(3.7): {result}")
```
### Output - Question 1 

Question 1: Interpolated value at f(3.7): 1.554999999999995

## Question 2: Newton’s Forward Method
```python
def newton_forward(x, y, degree):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    
    for i in range(1, n):
        for j in range(1, i + 1):
            F[i, j] = F[i, j - 1] - F[i - 1, j - 1]
    
    #Construct the polynomial
    def polynomial(t):
        result = F[0, 0]
        for i in range(1, degree + 1):
            term = F[i, i]
            for j in range(i):
                term *= (t - x[j])
            result += term
        return result
    
    return polynomial

#Given data
x = np.array([7.2, 7.4, 7.5, 7.6])
y = np.array([23.5492, 25.3913, 26.8224, 27.4589])

#Degrees 1, 2, and 3
degrees = [1, 2, 3]
for degree in degrees:
    poly = newton_forward(x, y, degree)
    print(f"Degree {degree} polynomial approximation: {poly(7.3)}")
```
### Output - Question 2

Question 2: Degree 1 polynomial approximation: 24.47718457889519
Question 2: Degree 2 polynomial approximation: 24.47718457889519
Question 2: Degree 3 polynomial approximation: 24.47718457889519


## Question 3: Approximate f(7.3)
```python
#Using the polynomial from degree 3
poly = newton_forward(x, y, 3)
result = poly(7.3)
print(f"Question 3: Approximated value at f(7.3): {result}")
```
### Output - Question 3

Question 3: Approximated value at f(7.3): 24.47718457889519

## Question 4: Divided Difference Method (Hermite Polynomial)
```python
def divided_differences(x, y, y_prime):
    n = len(x)
    F = np.zeros((2 * n, 2 * n))
    
    #Fill in the first column with y values
    for i in range(n):
        F[2 * i, 0] = y[i]
        F[2 * i + 1, 0] = y[i]
    
    #Fill in the second column with y_prime values
    for i in range(n):
        F[2 * i + 1, 1] = y_prime[i]
    
    #Fill in the rest of the table
    for j in range(2, 2 * n):
        for i in range(j, 2 * n):
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[(i) // 2] - x[(i - j) // 2])
    
    return F

#Example data (you need to provide y_prime values)
x = np.array([3.6, 3.8, 3.9])
y = np.array([1.675, 1.436, 1.318])
y_prime = np.array([-1.195, -1.188, -1.182])

#Compute the divided difference table
F = divided_differences(x, y, y_prime)
print("Question 4: Hermite polynomial approximation matrix:")
print(F)
```
### Output - Question 4

Question 4: Hermite polynomial approximation matrix:
[[ 3.60000000e+00  1.67500000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00 ]  
 [ 3.60000000e+00  1.67500000e+00 -1.19500000e+00  0.00000000e+00  0.00000000e+00 ]  
 [ 3.80000000e+00  1.43600000e+00 -1.19500000e+00 -9.99200722e-15  0.00000000e+00 ]  
 [ 3.80000000e+00  1.43600000e+00 -1.18800000e+00  3.50000000e-02  1.75000000e-01 ]  
 [ 3.90000000e+00  1.31800000e+00 -1.18000000e+00  8.00000000e-02 -1.28571429e-02 ]  
 [ 3.90000000e+00  1.31800000e+00 -1.18200000e+00 -2.00000000e-02 -1.00000000e+00 ]]

## Question 5: Cubic Spline Interpolation
```python
from scipy.interpolate import CubicSpline

# Given data
x = np.array([2, 5, 8, 10])
y = np.array([3, 5, 7, 9])

# Create the cubic spline
cs = CubicSpline(x, y, bc_type='natural')

# Find matrix A, vector b, and vector x
A = cs.c.T
b = cs.c.T @ x
x_solution = np.linalg.solve(A, b)

print("Question 5: Matrix A:")
print(A)
print("Question 5: Vector b:")
print(b)
print("Question 5: Vector x:")
print(x_solution)
```
### Output - Question 5

Question 5: Matrix A:
[[ 1.  0.  0.  0. ]  
 [ 3. 12.  3.  0. ]  
 [ 0.  3. 10.  2. ]  
 [ 0.  0.  0.  1. ]  
 [ 0.  0.  1.  0. ]]
Question 5: Vector b:
[ 0.  -0.02702703  0.10810811  0. ]
Question 5: Vector x:
[ 0.  0.  1.  0. ]




