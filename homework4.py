"""
Written by :
Name: Amit Ovadia, 207634791
Name: Rona Nazarov, 207134446
"""
import math
import sympy as sp
import numpy

def func(x):
    return pow(x, 4) + pow(x, 3) - 3 * pow(x, 2)


def derivative(x_par):
    x = sp.symbols('x')
    my_f = pow(x, 4) + pow(x, 3) - 3 * pow(x, 2)
    der = sp.diff(my_f, x)
    return der.evalf(subs={x: x_par})


def bisection(a, b, epsilon, error, function):
    if (function(a) * function(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    if a > b:
        temp = a
        a = b
        b = temp

    max_iters = math.ceil(-(math.log(error / (b - a), math.e)) / (math.log(2, math.e)))

    c = a
    for i in range(0, max_iters):
        if (b - a) < epsilon:
            break

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    if (b - a) < epsilon:
        return c
    return None


def bisection_method(a, b, diff, epsilon, error, function):
    roots = []
    x = a
    next_x = x + diff
    y_perv = function(x)
    y_curr = function(next_x)

    num_itrs = int((abs(a) + abs(b)) / diff)
    for i in range(0, num_itrs + 1):
        if y_perv * y_curr < 0:
            point_x = bisection(x, next_x, epsilon, error, function)
            if point_x is not None:
                roots.append(point_x)
        x = next_x
        next_x += diff
        y_perv = y_curr
        y_curr = function(next_x)
    return roots




def find_roots(a, b, diff, epsilon, error):
    #find roots with the function
    roots = bisection_method(a, b, diff, epsilon, error, func)
    # find roots with the derivative
    roots_der = bisection_method(a, b, diff, epsilon, error, derivative)
    for i in roots_der:
        if func(i) == 0:
            roots.append(i)
    # Check x = 0
    if func(0) == 0:
        roots.append(0)
    print(roots)


print("Please enter a:")
a = float(input())
print("Please enter b:")
b = float(input())
print("Please enter the epsilon:")
epsilon = float(input())
print("Please enter the error:")
error = float(input())
print("Please enter the difference:")
diff = float(input())
find_roots(a, b, diff, epsilon, error)