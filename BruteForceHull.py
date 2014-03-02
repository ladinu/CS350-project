import ..geometry

def computeHull(points):
   polygonEdges = []
   for p1 in points:
      for p2 in points:
         edge = Line(p1, p2)
         determinantSigns = []
         for p in points:
            detSign = edge.getDeterminantSign(p)
            determinantSigns.append(detSign)
         if not allPositivesAndNegatives(determinantSigns):
            polygonEdges.append(edge)
   return polygonEdges

def allPositivesAndNegatives(array):
   return (-1 in array and 1 in array)

