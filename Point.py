from operator import itemgetter

class Point(tuple):
   __slots__ = []
   def __new__(cls, x=0, y=0):
      return tuple.__new__(cls, (x, y))
   x = property(itemgetter(0))
   y = property(itemgetter(1))
