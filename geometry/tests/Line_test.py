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

   def testisSameLine(self):
      l1 = Line(P(0, 0), P(-1, -1))
      l2 = Line(P(0, 0), P(-1, -1))
      l3 = Line(P(0, 0), P(1, 1))
      l4 = Line(P(1, 1), P(0, 0))
      l5 = Line(P(0, 0), P(0, 0))

      self.assertTrue(l1.isSameLine(l2))
      self.assertTrue(l2.isSameLine(l1))

      self.assertTrue(l3.isSameLine(l4))
      self.assertTrue(l4.isSameLine(l3))

      self.assertFalse(l1.isSameLine(l3))
      self.assertFalse(l3.isSameLine(l1))

      self.assertFalse(l1.isSameLine(l5))
      self.assertFalse(l5.isSameLine(l1))

   def testEq(self):
      l1 = Line(P(0, 0), P(-1, -1))
      l2 = Line(P(0, 0), P(1, 1))
      self.assertEqual(l1, l1)
      self.assertEqual(l1, l2)
      self.assertEqual(l2, l1)

   def testNe(self):
      l1 = Line(P(0, 0), P(-1, -1))
      l2 = Line(P(0, 1), P(1, 1))
      self.assertNotEqual(l1, l2)
      self.assertNotEqual(l2, l1)

   def testLt(self):
      l1 = Line(P(0, 0), P(1, 1))
      l2 = Line(P(0, 0), P(1, -2))
      self.assertLess(l1, l2)

   def testLe(self):
      l1 = Line(P(0, 0), P(1, 1))
      l2 = Line(P(0, 0), P(1, -2))
      self.assertLessEqual(l1, l1)
      self.assertLessEqual(l1, l2)

   def testGt(self):
      l1 = Line(P(0, 0), P(1, -2))
      l2 = Line(P(0, 0), P(1, 1))
      self.assertGreater(l1, l2)

   def testGe(self):
      l1 = Line(P(0, 0), P(1, -2))
      l2 = Line(P(0, 0), P(1, 1))

      self.assertGreaterEqual(l1, l2)
      self.assertGreaterEqual(l2, l2)

if __name__ == '__main__':
   unittest.main()
