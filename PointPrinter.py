from PIL import Image, ImageDraw
from PointUtils import getSquareEnclosingPoint
from Point import Point as P

class PointPrinterException(Exception):
   pass

class PointPrinterPoint(P):
   def __init__(self, point=P(), isMarked = False):
      self.marked = isMarked
      super(P, self).__new__(P, point.x, point.y)


class PointPrinter():
   def __init__(self):
      self._points = []

   def printPoint(self, point):
      self._points.append(self._ppp(point))

   def printPoints(self, pointList):
      points = []
      for p in pointList:
         points.append(self._ppp(p))
      self._points = self._points + points

   def printToFile(self, outFile, outputType='image'):
      if outputType == 'image':
         self._writeImgToFile(outFile)
      else:
         raise PointPrinterException("invalid output type")

   def _composeImage(self):
      size = self._getImageSizeThatWillContainAllPoints()
      img = Image.new('RGB', size, 'white')
      draw = ImageDraw.Draw(img)
      for p in self._points:
         bounds = self._flatten(getSquareEnclosingPoint(p, 1))
         draw.rectangle(bounds, fill='black')
      return img

   def _writeImgToFile(self, outFile):
      img = self._composeImage()
      img.save(outFile + '.bmp')

   def _flatten(self, bounds):
      return (bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1])

   def _getImageSizeThatWillContainAllPoints(self, padding = 100):
      maxPoint = max(self._points)
      return P(maxPoint.x + padding, maxPoint.y + padding)

   def _ppp(self, point):
      return PointPrinterPoint(point)
