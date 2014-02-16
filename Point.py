from operator import itemgetter
import Distance

class Point(tuple):
   __slots__ = []

   def __new__(cls, x=0, y=0):
      return tuple.__new__(cls, (x, y))

   def getDistanceFrom(self, other):
      return Distance.calculate(self, other)

   def __eq__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf == distanceOfOther

   def __ne__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf != distanceOfOther

   def __lt__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf < distanceOfOther

   def __le__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf <= distanceOfOther

   def __gt__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf > distanceOfOther

   def __ge__(self, other):
      distanceOfSelf = self.getDistanceFrom(Point(0, 0))
      distanceOfOther = other.getDistanceFrom(Point(0, 0))
      return distanceOfSelf >= distanceOfOther


   x = property(itemgetter(0))
   y = property(itemgetter(1))

