import unittest
from math import sqrt
from Point import Point as P

class PointTest(unittest.TestCase):

   def testDefaultPoint(self):
      p = P()
      self.assertEqual(p.x, 0)
      self.assertEqual(p.y, 0)

   def testConstruct(self):
      p = P(1, 3)
      self.assertEqual(p.x, 1)
      self.assertEqual(p.y, 3)

   def testImmutability(self):
      p = P(4, 3)
      self.assertRaises(AttributeError, lambda: f(p))
      self.assertEqual(4, p.x)
      self.assertEqual(3, p.y)

   def test_getDistance(self):
      p = P(1, 1)
      self.assertEqual(sqrt(10), p.getDistanceFrom(P(2, 4)))

   def testEq(self):
      self.assertEqual(P(1, 1), P(-1, -1))

def f(p):
   p.x = 1
   p.y = 2

if __name__ == '__main__':
   unittest.main()
