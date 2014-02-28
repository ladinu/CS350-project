from Geometry import Point
from Geometry import Line

def computeHull(points):
   polygonEdges = []
   for p1 in points:
      for p2 in points:
         if p1 == p2:
            break
         edge = Line(p1, p2)
         determinantSigns = []
         for p in points:
            if p not in edge:
               detSign = edge.getDeterminantSign(p)
               determinantSigns.append(detSign)
         if not allPositivesAndNegatives(determinantSigns):
            polygonEdges.append(edge)
   return polygonEdges

def allPositivesAndNegatives(array):
   return (-1 in array and 1 in array)

