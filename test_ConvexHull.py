import unittest
import ConvexHull
from PointUtils import *
from Geometry import Point as P, Line
from pyhull.convex_hull import ConvexHull as pyConvexHull

#Test convex hull results against pyhull's ConvexHull
class ConvexHullTest(unittest.TestCase):

   def test_oneLine(self):
      pointA = getRandomPoint()
      pointB = getRandomPoint()
      line = Line(pointA, pointB)
      vertices = ConvexHull.computeHull(line)
      self.assertEqual(1, len(vertices))
      self.assertTrue(vertices[0] == line)

   def test_Triangle(self):
      pointA = P(0, 0)
      pointB = P(0, 5)
      pointC = P(5, 0)
      triangle = [pointA, pointB, pointC]
      bruteConvex = [i.toList() for i in ConvexHull.computeHull(triangle)]
      pyhullConvex = pyConvexHull(triangle)
      #compare using sets(list) because order might be different
      self.assertTrue(sameList(bruteConvex, pyhullConvex.vertices))

   @unittest.skip("broken")
   def test_randomListPoints(self):
      randomPoints = getNRandomPoints(10)
      bruteConvex = ConvexHull.computeHull(randomPoints)
      pyhullConvex = convex_hull.Convexhull(randomPoints)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))


def sameList(listA, listB):
   for a in listA:
      if a not in listB:
         return False
   for b in listB:
      if b not in listA:
         return False
   return True


if __name__ == '__main__':
   unittest.main()
