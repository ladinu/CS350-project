from Point import Point as P
import random

def getRandomPoint(low=0, high=10):
   x = random.randint(low, high)
   y = random.randint(low, high)
   return P(x, y)

def getNRandomPoints(n=10, low=0, high=10):
   points = []
   assert(n >=0)
   for i in range(n):
      points.append(getRandomPoint(low, high))
   return points
