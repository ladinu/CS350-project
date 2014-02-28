from operator import itemgetter
import GeometryUtils as utils

class Point(tuple):
   __slots__ = []

   def __new__(cls, x=0, y=0):
      return tuple.__new__(cls, (x, y))

   def __eq__(self, other):
      return self._dist(self) == self._dist(other)

   def __ne__(self, other):
      return self._dist(self) != self._dist(other)

   def __lt__(self, other):
      return self._dist(self) < self._dist(other)

   def __le__(self, other):
      return self._dist(self) <= self._dist(other)

   def __gt__(self, other):
      return self._dist(self) > self._dist(other)

   def __ge__(self, other):
      return self._dist(self) >= self._dist(other)


   def _dist(self, point):
      return point.getDistanceFrom(Point(0, 0))

   x = property(itemgetter(0))
   y = property(itemgetter(1))

   def getDistanceFrom(self, other):
      return Line(self, other).getDistance()

   def toList(self):
      return [self.x, self.y]

class Line(tuple):
   __slots__ = []

   def __new__(cls, start=Point(), end=Point()):
      return tuple.__new__(cls, (start, end))

   startPoint = property(itemgetter(0))
   endPoint = property(itemgetter(1))

   def getDistance(self):
      return utils.calculateDistance(self.startPoint, self.endPoint)

   def getDeterminantSign(self, point):
      return utils.getDeterminantSign(self.startPoint, self.endPoint, point)

   def isPoint(self):
      return self.getDistance() == 0

   def __eq__(self, other):
      a = [self.startPoint, self.endPoint]
      b = [other.startPoint, other.endPoint]

      lineEqual = True
      for i in a:
         if i not in b:
            lineEqual = False
      return lineEqual

   def __contains__(self, key):
      return (key == self.startPoint or key == self.endPoint)


