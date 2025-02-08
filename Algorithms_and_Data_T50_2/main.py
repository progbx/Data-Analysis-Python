import math
import cmath 

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        x1 = x2 = -b / (2*a)
    else:
        x1 = (-b - cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    
    if isinstance(x1, complex) and isinstance(x2, complex):
        if x1.real > x2.real:
            x1, x2 = x2, x1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
    
    return x1, x2