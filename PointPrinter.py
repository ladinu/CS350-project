from PIL import Image, ImageDraw
from PointUtils import getSquareEnclosingPoint
from Point import Point as P

class PointPrinterException(Exception):
   pass

class PointPrinter():
   def __init__(self):
      self._points = []

   def printPoint(self, point):
      self._points.append(point)

   def printPoints(self, pointList):
      self._points = self._points + pointList

   def printToFile(self, outFile, outputType='image'):
      if outputType == 'image':
         self._printImage(outFile)
      else:
         raise PointPrinterException("invalid output type")

   def _printImage(self, outFile):
      size = self._getImageSizeThatWillContainAllPoints()
      img = Image.new('RGB', size, 'white')
      draw = ImageDraw.Draw(img)
      for p in self._points:
         bounds = self._flatten(getSquareEnclosingPoint(p))
         print bounds
         draw.rectangle(bounds, fill='black')
      img.show()

   def _flatten(self, bounds):
      return (bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1])

   def _getImageSizeThatWillContainAllPoints(self, padding = 100):
      maxPoint = max(self._points)
      return P(maxPoint.x + padding, maxPoint.y + padding)

