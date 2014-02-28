import unittest
from math import sqrt
from Geometry import Point as P
from Geometry import Line

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

   def testToList(self):
      p1 = P(4, 5)
      self.assertEqual([4, 5], p1.toList())


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

   def testEq(self):
      l1 = Line(P(1, 3), P(3, 4))
      l2 = Line(P(4, 3), P(0, 0))
      l3 = Line(P(0, 0), P(4, 3))

      self.assertTrue(l1 == l1)
      self.assertTrue(l1 != l2)
      self.assertTrue(l2 == l3)



if __name__ == '__main__':
   unittest.main()
