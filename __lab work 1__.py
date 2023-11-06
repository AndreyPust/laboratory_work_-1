from math import sqrt

# using libraries

print("enter the a:")
a = float(input())
print("enter the b:")
b = float(input())
print("enter the c:")
c = float(input())

# enter the variables

D = b*b - 4*a*a
x1 = (-b+sqrt(D))/2*a

# calculation x1

x2 = (-b-sqrt(D))/2*a

# calculation x2

print("x1 = ", x1, "x2 = ", x2)