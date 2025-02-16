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

