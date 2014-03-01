from math import sqrt, fabs
import random

import Point as P

EUCLIDEAN = 0
MANHATTAN = 1

def getRandomPoint(low=0, high=10):
   x = random.randint(low, high)
   y = random.randint(low, high)
   return P(x, y)

def getNRandomPoints(n=10, low=0, high=10):
   points = []
   assert(n >= 0)
   for i in range(n):
      points.append(getRandomPoint(low, high))
   return points

def getSquareEnclosingPoint(point, squareSize=5):
   p1 = P(point.x - squareSize, point.y + squareSize)
   p2 = P(point.x + squareSize, point.y - squareSize)
   return (p1, p2)


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
   p = p1.toList() + [1]
   q = p2.toList() + [1]
   r = p3.toList() + [1]

   # Using Sarrus' scheme
   sum1 = q[0]*r[1] + p[0]*q[1] + r[0]*p[1]
   sum2 = q[0]*p[1] + r[0]*q[1] + p[0]*r[1]

   return cmp(sum1 - sum2, 0)

