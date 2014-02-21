import unittest
from math import sqrt
from Point import Point as P
from Distance import *

class Distance(unittest.TestCase):
   
   def test_SamePoint(self):
      d = calculate(P(4, 2), P(4, 2))
      self.assertEqual(0.0, d)


   def test_SimplePoint(self):
      d = calculate(P(1, 3), P(4, 2))
      self.assertEqual(sqrt(10), d)

   def test_InvalidDistanceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      self.assertRaises(
            DistanceException, lambda: calculate(p1, p2, "NONE"))

   def test_EuclideanDistanceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      d = calculate(p1, p2, EUCLIDEAN)
      self.assertEqual(sqrt(5), d)

   def test_ManhattanDistnaceType(self):
      p1 = P(3, 4)
      p2 = P(1, 3)
      d = calculate(p1, p2, MANHATTAN)
      self.assertEqual(3, d)
      

if __name__ == '__main__':
   unittest.main()
