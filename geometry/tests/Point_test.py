import unittest
from math import sqrt
from ..Point import Point as P
from ..Line import Line

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
      self.assertRaises(AttributeError, lambda: self.f(p))
      self.assertEqual(4, p.x)
      self.assertEqual(3, p.y)

   def f(self, p):
      p.x = 1
      p.y = 2

   def testEq(self):
      self.assertEqual(P(1, 1), P(1, 1))

   def testNe(self):
      self.assertNotEqual(P(1, 2), P(-1, -1))
      self.assertNotEqual(P(1, 1), P(-1, -1))

   def testToList(self):
      p1 = P(4, 5)
      self.assertEqual([4, 5], p1.toList())


if __name__ == '__main__':
   unittest.main()
