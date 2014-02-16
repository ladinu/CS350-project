import unittest
from Point import *

class PointTest(unittest.TestCase):

   def testDefaultPoint(self):
      p = Point()
      self.assertEqual(p.x, 0)
      self.assertEqual(p.y, 0)

   def testConstruct(self):
      p = Point(1, 3)
      self.assertEqual(p.x, 1)
      self.assertEqual(p.y, 3)

   def testImutability(self):
      p = Point(4, 3)
      self.assertRaises(AttributeError, lambda: f(p))
      self.assertEqual(4, p.x)
      self.assertEqual(3, p.y)

   def testEquality(self):
      self.assertEqual(Point(1, 3), Point(1, 3))
      self.assertEqual(Point(3, 3), Point(2, 2))
      self.assertNotEqual(Point(1, 2), Point(1, 3))

   def testLessThan(self):
      self.assertTrue(Point(0, 3) < Point(0, 4))
      self.assertTrue(Point(0, 1) < Point(0, 4))
      self.assertFalse(Point(0, 4) < Point(0, 2))

   def testGreaterThan(self):
      self.assertTrue(Point(0, 2) > Point(0, 1))
      self.assertFalse(Point(0, 1) > Point(0, 2))

def f(p):
   p.x = 1
   p.y = 2

if __name__ == '__main__':
   unittest.main()
