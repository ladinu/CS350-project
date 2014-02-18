import unittest
from PointUtils import *
from Point import Point

class PointUtilTest(unittest.TestCase):

   def testGetRandomPoint(self):
      p = getRandomPoint()
      self.assertTrue(type(p) == Point)

   def testGetRandomPoint1(self):
      low = 0
      high = 5
      for i in range(100):
         p = getRandomPoint(low, high)
         self.between(p.x, low, high)
         self.between(p.y, low, high)

   def testGetRandomPoints(self):
      points = getNRandomPoints()
      self.assertTrue(len(points) >= 0)

   def testGetRandomPoints1(self):
      points = getNRandomPoints(13)
      self.assertTrue(len(points) == 13)

   def testGetRandomPoints2(self):
      n = 23
      low = 0
      high = 3
      points = getNRandomPoints(n, low, high)
      self.assertTrue(len(points) == n)

      for i in range(n):
         self.between(points[i].x, low, high)
         self.between(points[i].y, low, high)

   def between(self, number, numLow, numHigh):
      self.assertGreaterEqual(number, numLow)
      self.assertLessEqual(number, numHigh)




if __name__ == '__main__':
   unittest.main()

