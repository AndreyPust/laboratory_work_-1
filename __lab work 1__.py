# the program for solving the quadratic equation
from math import sqrt
print("enter the a:")
a = float(input())
print("enter the b:")
b = float(input())
print("enter the c:")
c = float(input())
D = b*b - 4*a*a
x1 = (-b+sqrt(D))/2*a
x2 = (-b-sqrt(D))/2*a
print("x1 = ", x1, "x2 = ", x2)