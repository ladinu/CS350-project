from Point import Point as P
from ConvexHull import ConvexHull
from PointUtils import *
class ConvexHullTest(unittest.Testcase):
    def test_ConvexHull(self):
        qhull = ConvexHull()
        
