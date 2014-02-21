from operator import itemgetter
import Distance

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
      return Distance.calculate(self, other)

   def isLeftOf(self, a, b):
      c = self
      return ((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)) > 0;

class Line(tuple):
   __slots__ = []

   def __new__(cls, start=Point(), end=Point()):
      return tuple.__new__(cls, (start, end))

   startPoint = property(itemgetter(0))
   endPoint = property(itemgetter(1))

   def getDistance(self):
      return Distance.calculate(self.startPoint, self.endPoint)

