import unittest
from PointUtils import *
from Point import Point

class PointUtilTest(unittest.TestCase):

   def testGetRandomPoint(self):
      p = getRandomPoint()
      self.assertTrue(type(p) == Point)

if __name__ == '__main__':
   unittest.main()

