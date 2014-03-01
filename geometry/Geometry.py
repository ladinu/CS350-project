from operator import itemgetter
import GeometryUtils as utils

class Point(tuple):
   __slots__ = []

   def __new__(cls, x=0, y=0):
      return tuple.__new__(cls, (x, y))

   def __eq__(self, other):
      return (self.x == other.x and self.y == other.y)

   def __ne__(self, other):
      return not (self == other)

   x = property(itemgetter(0))
   y = property(itemgetter(1))

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

   def isSameLine(self, other):
      a, b = (self.startPoint, self.endPoint)
      c, d = (other.startPoint, other.endPoint)
      return (a == c and b == d) or (a == d and b == c)

   def __contains__(self, key):
      return (key == self.startPoint or key == self.endPoint)

   def __eq__(self, other):
      return self.getDistance() == other.getDistance()

   def __ne__(self, other):
      return not self == other
   
   def __lt__(self, other):
      return self.getDistance() < other.getDistance()

   def __le__(self, other):
      return self.getDistance() <= other.getDistance()

   def __gt__(self, other):
      return self.getDistance() > other.getDistance()

   def __ge__(self, other):
      return self.getDistance() >= other.getDistance()



