import math
from InvalidDim import InvalidDim
class Triangle:

    def __init__(self, a, b, c):
        '''
            Create a triangle with lengths greater than 0.
        '''
        try:
            if a <= 0 or b <= 0 or c <= 0:
                raise InvalidDim
        except InvalidDim:
            print("Invalid length.")
            SystemExit(1)
        self.a = a
        self.b = b
        self.c = c

    def classify_triangle(self):
        result = ""

        if self.a != self.b and self.a != self.c and self.b != self.c:
            result = "Scalene"
        else:
            if self.a == self.b and self.a == self.c and self.b == self.c:
                result = "Equilateral"
            else:
                result = "Isosceles"
        return result

    def isRightTriangle(self):
        return round(((self.a**2) + (self.b**2)),2) == round((self.c**2),2)



