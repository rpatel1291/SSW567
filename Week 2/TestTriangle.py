# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6,8,10),'Right','3,4,5 is a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(8,6,10),'Right','5,3,4 is a Right triangle')
    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(10,6,8),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,2,4),'Scalene','2,2,4 should be a scalene')
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(2,3,4),'Isoceles','2,2,4 should be a scalene')

    def testValidInputs(self):
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput', '-1,2,3 should be invalidinputs')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

