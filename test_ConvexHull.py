import unittest
from ConvexHull import ConvexHull
from PointUtils import *
import pyhull

#Test convex hull results against pyhull's ConvexHull
class ConvexHullTest(unittest.Testcase):

   def test_oneLine(self):
      pointA = getRandomPoint()
      pointB = getRandomPoint()
      line = [pointA, pointB]
      bruteConvex = ConvexHull.computeHull(line)
      self.assertTrue(bruteConvex.getVertices() == line)

   def test_Triangle(self):
      pointA = P(0, 0)
      pointB = P(0, 5)
      pointC = P(5, 0)
      triangle = [pointA, pointB, pointC]
      bruteConvex = ConvexHull.computeHull(triangle)
      pyhullConvex = convex_hull.Convexhull(triangle)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))

   def test_randomListPoints(self):
      randomPoints = getNRandomPoints(10)
      bruteConvex = ConvexHull.computeHull(randomPoints)
      pyhullConvex = convex_hull.Convexhull(randomPoints)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))

if __name__ == '__main__':
   unittest.main()
