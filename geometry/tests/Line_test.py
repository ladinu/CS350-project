import unittest
from math import sqrt

from ..Point import Point as P
from ..Line import Line

class LineTest(unittest.TestCase):
   
   def testLine(self):
      line = Line()
      self.assertEqual(P(), line.startPoint)
      self.assertEqual(P(), line.endPoint)

   def testConstruct(self):
      p1 = P(1, 3)
      p2 = P(3, 3)
      line = Line(p1, p2)
      self.assertEqual(line.startPoint, p1)
      self.assertEqual(line.endPoint, p2)

   def testImmutability(self):
      p1 = P(1, 3)
      p2 = P(3, 3)
      line = Line(p1, p2)
      self.assertRaises(AttributeError, lambda: self.f(line))

   def f(self, line):
      line.startPoint = P(1, 2)
      line.endPoint = P(0, 1)

   def testGetDistance(self):
      l = Line()
      self.assertEqual(0, l.getDistance())
      l = Line(P(0, 0), P(0, 1))
      self.assertEqual(1, l.getDistance())

   def testGetDeterminantSign(self):
      l = Line(P(2, 2), P(3, 2))
      self.assertEqual(0, l.getDeterminantSign(P(4, 2)))
      self.assertLess(l.getDeterminantSign(P(3, 1)), 0)
      self.assertGreater(l.getDeterminantSign(P(3, 3)), 0)

   def testIsPoint(self):
      l = Line(P(0, 0), P(0, 0))
      self.assertTrue(l.isPoint())
      l = Line(P(0, 0), P(0, 1))
      self.assertFalse(l.isPoint())

   def testContains(self):
      l = Line(P(1, 3), P(9, 0))
      self.assertTrue((P(1, 3) in l))
      self.assertTrue((P(9, 0) in l))
      self.assertFalse(P(1, 1) in l)

   def testEq(self):
      l1 = Line(P(0, 0), P(-1, -1))
      l2 = Line(P(0, 0), P(-1, -1))
      l3 = Line(P(0, 0), P(1, 1))
      l4 = Line(P(1, 1), P(0, 0))
      l5 = Line(P(0, 0), P(0, 0))

      self.assertTrue(l1 == l2)
      self.assertTrue(l2 == l1)

      self.assertTrue(l3 == l4)
      self.assertTrue(l4 == l3)

   def testNe(self):
      l1 = Line(P(0, 0), P(-1, -1))
      l2 = Line(P(0, 0), P(-1, -1))
      l3 = Line(P(0, 0), P(1, 1))
      l4 = Line(P(1, 1), P(0, 0))
      l5 = Line(P(0, 0), P(0, 0))

      self.assertTrue(l1 != l3)
      self.assertTrue(l3 != l1)

      self.assertTrue(l1 != l5)
      self.assertTrue(l5 != l1)

if __name__ == '__main__':
   unittest.main()
