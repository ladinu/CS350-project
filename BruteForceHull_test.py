import unittest
import itertools
import numpy as np
from BruteForceHull import computeHull
from geometry.utils import *
from geometry.Point import Point as P
from geometry.Line import Line
from pyhull.convex_hull import ConvexHull as pyConvexHull

#Test convex hull results against pyhull's ConvexHull
class BruteForceHullTest(unittest.TestCase):

   def testSinglePoint(self):
      point = getRandomPoint()
      vertices = computeHull([point])
      line = Line(point, point)
      vertices = computeHull([point])
      self.assertEqual(1, len(vertices))
      self.assertTrue(line == vertices[0])

   def testOneLine(self):
      pointA = getRandomPoint()
      pointB = getRandomPoint()
      line = Line(pointA, pointB)
      vertices = unique(computeHull([pointA, pointB]))

      self.assertEqual(1, len(vertices))
      self.assertTrue(vertices[0] == line)

   def testTriangle(self):
      triangle = [P(0, 0),  P(0, 5), P(5, 0)]
      vertices = unique(computeHull(triangle))
      self.assertTrue(len(vertices), 3)

   def testTriangleWithPointsInside(self):
      triangle = [P(0, 0),  P(0, 5), P(5, 0), P(1, 1)]
      vertices = unique(computeHull(triangle))
      self.assertTrue(len(vertices), 3)
      for v in vertices:
         self.assertTrue(v.startPoint != P(1, 1))
         self.assertTrue(v.endPoint != P(1, 1))

def unique(vertices):
   retv = []
   for v in vertices:
      if not v.isPoint() and v not in retv:
         retv.append(v)
   return retv


if __name__ == '__main__':
   unittest.main()
