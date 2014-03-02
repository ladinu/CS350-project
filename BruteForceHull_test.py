import unittest
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
      vertices = unique(computeHull([point]))
      self.assertEqual(1, len(vertices))
      self.assertTrue(line.isSameLine(vertices[0]))

   def testOneLine(self):
      pointA = getRandomPoint()
      pointB = getRandomPoint()
      line = Line(pointA, pointB)
      vertices = unique(computeHull([pointA, pointB]))

      self.assertEqual(1, len(vertices))
      self.assertTrue(vertices[0] == line)

   @unittest.skip("broken")
   def test_Triangle(self):
      pointA = P(0, 0)
      pointB = P(0, 5)
      pointC = P(5, 0)
      triangle = [pointA, pointB, pointC]
      bruteConvex = [i.toList() for i in computeHull(triangle)]
      pyhullConvex = pyConvexHull(triangle)
      #compare using sets(list) because order might be different
      self.assertTrue(sameList(bruteConvex, pyhullConvex.vertices))

   @unittest.skip("broken")
   def test_randomListPoints(self):
      randomPoints = getNRandomPoints(10)
      bruteConvex = computeHull(randomPoints)
      pyhullConvex = convex_hull.Convexhull(randomPoints)
      #compare using sets(list) because order might be different
      self.assertTrue(set(bruteConvex.getVertices()) == set(pyhullConvex.vertices()))


def unique(vertices):
   retv = []
   print vertices
   for v in vertices:
      add = True
      for i in vertices:
         if v.isSameLine(i):
            add = False
      if add:
         retv.append(v)
   print retv
   return retv

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
