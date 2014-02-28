import unittest
import ConvexHull
from PointUtils import *
from Geometry import Point as P, Line
import pyhull

#Test convex hull results against pyhull's ConvexHull
class ConvexHullTest(unittest.TestCase):

   def test_oneLine(self):
      pointA = getRandomPoint()
      pointB = getRandomPoint()
      line = Line(pointA, pointB)
      vertices = ConvexHull.computeHull(line)
      self.assertEqual(1, len(vertices))
      self.assertTrue(vertices[0] == line)

   @unittest.skip("broken")
   def test_Triangle(self):
      pointA = P(0, 0)
      pointB = P(0, 5)
      pointC = P(5, 0)
      triangle = [pointA, pointB, pointC]
      bruteConvex = ConvexHull.computeHull(triangle)
      pyhullConvex = convex_hull.Convexhull(triangle)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))

   @unittest.skip("broken")
   def test_randomListPoints(self):
      randomPoints = getNRandomPoints(10)
      bruteConvex = ConvexHull.computeHull(randomPoints)
      pyhullConvex = convex_hull.Convexhull(randomPoints)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))

if __name__ == '__main__':
   unittest.main()
