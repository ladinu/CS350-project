import unittest
from math import sqrt
from Geometry import Point as P
from GeometryUtils import *

class DistanceTest(unittest.TestCase):
   
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

   def test_getDeterminant(self):
      p1 = P(1, 4)
      p2 = P(4, 2)
      p3 = P(0, 0)
      self.assertTrue(-14, getDeterminant(p1, p2, p3))
      

if __name__ == '__main__':
   unittest.main()
