import unittest
from math import sqrt
from Geometry import Point as P
from GeometryUtils import *

class UtilsTest(unittest.TestCase):

   def testGetRandomPoint(self):
      p = getRandomPoint()
      self.assertTrue(type(p) == P)

   def testGetRandomPoint1(self):
      low = 0
      high = 5
      for i in range(100):
         p = getRandomPoint(low, high)
         self.between(p.x, low, high)
         self.between(p.y, low, high)

   def testGetRandomPoints(self):
      points = getNRandomPoints(0)
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

   def testGetSquareEnclosingPoint(self):
      bounds = getSquareEnclosingPoint(P(0, 0))
      topLeft = bounds[0]
      bottomRight = bounds[1]
      self.assertTrue(P(-5, 5) == topLeft)
      self.assertTrue(P(5, -5))

   def testGetSquareEnclosingPoint(self):
      size = 10
      bounds = getSquareEnclosingPoint(P(0, 0), size)
      topLeft = bounds[0]
      bottomRight = bounds[1]
      self.assertTrue(P(-size, size) == topLeft)
      self.assertTrue(P(size, -size))

   def test_SamePoint(self):
      d = calculateDistance(P(4, 2), P(4, 2))
      self.assertEqual(0.0, d)

   def test_SimplePoint(self):
      d = calculateDistance(P(1, 3), P(4, 2))
      self.assertEqual(sqrt(10), d)

   def test_InvalidDistanceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      self.assertRaises(
            DistanceException, lambda: calculateDistance(p1, p2, "NONE"))

   def test_EuclideanDistanceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      d = calculateDistance(p1, p2, EUCLIDEAN)
      self.assertEqual(sqrt(5), d)

   def test_ManhattanDistnaceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      d = calculateDistance(p1, p2, MANHATTAN)
      self.assertEqual(3, d)

   def test_getDeterminantSign0(self):
      p1 = P(4, 2)
      p2 = P(4, 2)
      p3 = P(4, 2)
      self.assertEqual(0, getDeterminantSign(p1, p2, p3))

   def test_getDeterminantSign1(self):
      p1 = P(0, 49)
      p2 = P(10, 1)
      p3 = P(0, 49)
      self.assertEqual(0, getDeterminantSign(p1, p2, p3))

   def test_getDeterminantSign2(self):
      p1 = P(0, 49)
      p2 = P(10, 1)
      p3 = P(0, 45)
      self.assertEqual(-1, getDeterminantSign(p1, p2, p3))


if __name__ == '__main__':
   unittest.main()
