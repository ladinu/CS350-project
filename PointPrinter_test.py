import unittest
from PointPrinter import *
from Point import Point as P
from PointUtils import *


class PointPrinterPointTest(unittest.TestCase):
   pass

class PointPrinterTest(unittest.TestCase):

   def testPrintPoint(self):
      pp = PointPrinter()
      self.assertTrue(len(pp._points) == 0)
      pp.printPoint(P(0, 0))
      self.assertTrue(len(pp._points) == 1)

   def testPrintPoints(self):
      pp = PointPrinter()
      points = getNRandomPoints(20)
      pp.printPoints(points)
      self.assertEqual(len(pp._points), 20)

   def testPrintToFile(self):
      pp = PointPrinter()
      points = getNRandomPoints(20, 100, 512)
      pp.printPoints(points)
      pp.printToFile('asd', 'image')

#img = Image.new('RGB', (255, 255), 'white')
#draw = ImageDraw.Draw(img)
#draw.ellipse((10, 10, 128, 128), fill='black')
#img.show()

if __name__ == '__main__':
   unittest.main()
