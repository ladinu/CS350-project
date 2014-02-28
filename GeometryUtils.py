from math import sqrt, fabs
from numpy import linalg

EUCLIDEAN = 0
MANHATTAN = 1

class DistanceException(Exception):
   pass

def calculateDistance(p1, p2, distanceType=EUCLIDEAN):
   if distanceType == EUCLIDEAN:
      return calculateEuclideanDistance(p1, p2)
   elif distanceType == MANHATTAN:
      return calculateManhattanDistance(p1, p2)
   else:
      raise DistanceException("invalid distance type")

def calculateEuclideanDistance(p1, p2):
   x_diff = p2.x - p1.x
   y_diff = p2.y - p1.y
   return sqrt(pow(x_diff, 2) + pow(y_diff, 2))

def calculateManhattanDistance(p1, p2):
   x_diff = fabs(p1.x - p2.x)
   y_diff = fabs(p1.y - p2.y)
   return x_diff + y_diff

def getDeterminantSign(p1, p2, p3):
   matrix = [ p1.toList() + [1],
              p2.toList() + [1],
              p3.toList() + [1] ]

   return linalg.slogdet(matrix)[0]

