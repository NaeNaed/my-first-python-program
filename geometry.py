# This program contains functions that evaluate formulas used in geometry
#
# Alejandro Huavil
# August 30, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r ** 2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(h, b1, b2):
    a = (b1+ b2) / 2 * h
    return a

def volume_rectangular_prism(w, h, l):
    v = w * h * l
    return v

def volume_cone(r, h):
    v = math.pi * r**2 * (h / 3)
    return v

def volume_sphere(r):
    v = (4 / 3) * math.pi * r**3
    return v

def surface_area_rectangular_prism(l, w, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def surface_area_sphere(r):
    a = 4 * math.pi * r ** 2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
