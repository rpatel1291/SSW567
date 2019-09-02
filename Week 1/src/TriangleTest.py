import pytest
from Triangle import Triangle

class TestTriangle:
    def test_classify_triangle(self):
        t1 = Triangle(1,2,3)
        t2 = Triangle(3,4,5)
        t3 = Triangle(3,3,3)
        t4 = Triangle(4,4,5)
        assert t1.classify_triangle().lower() == "scalene"
        assert t2.classify_triangle().lower() == "scalene"
        assert t3.classify_triangle().lower() == "equilateral"
        assert t4.classify_triangle().lower() == "isosceles"
    def test_isRightTriangle(self):
        t1 = Triangle(1,2,3)
        t2 = Triangle(3,4,5)
        t3 = Triangle(3,3,3)
        t4 = Triangle(4,4,5)
        assert t1.isRightTriangle() == False
        assert t2.isRightTriangle() == True
        assert t3.isRightTriangle() == False
        assert t4.isRightTriangle() == False

