import unittest
from math import sqrt
from Point import Point as P
from Point import Line as L

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

   def testGetDistance(self):
      p = P(1, 1)
      self.assertEqual(sqrt(10), p.getDistanceFrom(P(2, 4)))

   def testEq(self):
      self.assertEqual(P(1, 1), P(-1, -1))
      self.assertEqual(P(1, 1), P(1, 1))

   def testNe(self):
      self.assertNotEqual(P(1, 2), P(-1, -1))

   def testLt(self):
      self.assertLess(P(1, 1), P(1, -2))

   def testLe(self):
      p1 = P(1, 1)
      p2 = P(1, -2)
      self.assertLessEqual(p1, p1)
      self.assertLessEqual(p1, p2)

   def testGt(self):
      self.assertGreater(P(1, -2), P(1, 1))

   def testGe(self):
      p1 = P(1, -2)
      p2 = P(1, 1)
      self.assertGreaterEqual(p1, p2)
      self.assertGreaterEqual(p2, p2)

   @unittest.skip("check later")
   def testIsLeftOf(self):
      self.assertTrue(P(2, 0).isLeftOf(P(1, 1), P(3, 1)))

   def testIsLeftOfSamePoint(self):
      self.assertFalse(P(2, 1).isLeftOf(P(1, 1), P(3, 1)))


class LineTest(unittest.TestCase):
   
   def testLine(self):
      line = L()
      self.assertEqual(P(), line.startPoint)
      self.assertEqual(P(), line.endPoint)

def f(p):
   p.x = 1
   p.y = 2

if __name__ == '__main__':
   unittest.main()
