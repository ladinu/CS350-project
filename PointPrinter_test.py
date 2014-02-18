import unittest
from PointPrinter import *
from Point import Point

class PointPrinterTest(unittest.TestCase):

   def getMaxPoint(self):
      points = [ Point(1, 0), Point(3, 0) ]
      bound = getBound(points)


if __name__ == '__main__':
   unittest.main()
