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
