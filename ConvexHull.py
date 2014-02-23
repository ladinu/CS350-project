from Geometry import Point
from Geometry import Line

def computeHull(points):
   polygonEdges = []
   for i in points:
      for j in points:
         edge = Line(i, j)
         determinants = []
         for k in points:
            det = edge.getDeterminant(k)
            determinants.append(det)

         if not containPostiveAndNegativeInts(determinants):
            polygonEdges.append(edge)

   return polygonEdges

def containPostiveAndNegativeInts(array):
   allZerosOrNegatives = True
   for i in array:
      if i > 0:
         allZerosOrNegatives = False
         break
   if allZerosOrNegatives:
      return False

   allZerosOrPositives = True
   for i in array:
      if i < 0:
         allZerosOrPositives = False

   return not allZerosOrPositives
