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

   def testImmutability(self):
      p = Point(4, 3)
      self.assertRaises(AttributeError, lambda: f(p))
      self.assertEqual(4, p.x)
      self.assertEqual(3, p.y)

def f(p):
   p.x = 1
   p.y = 2

if __name__ == '__main__':
   unittest.main()
