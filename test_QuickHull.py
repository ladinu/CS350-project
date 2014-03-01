from Geometry import *
from QuickHull import QuickHull
import matplotlib.pyplot as plt
from PointUtils import *

def _flatten(points):
   xList = []
   yList = []
   for p in points:
      xList.append(p.x)
      yList.append(p.y)
   return (xList, yList)

def getEdges(vertices):
   size = len(vertices)
   if size < 1:
      return None
   elif size == 1:
      return list(Line(vertices[0]))
   temp = sorted(vertices)
   startingPoint = temp[0]
   listOfEdges = []
   for i in range(1, size):
      if i+1 < size and temp[i+1] == startingPoint:
         listOfEdges.append(Line(temp[i], startingPoint))
      else:
         listOfEdges.append(Line(temp[i-1], temp[i]))
   return listOfEdges

def main():
   workingSet = getNRandomPoints(10, 0, 50)
   print("Size of workingSet = " 'len(workingSet)')
   p1, p2 = _flatten(workingSet)

   plt.plot(p1, p2, 'o')
   plt.axis([-10, 60, -10, 60])

   testSet = QuickHull(workingSet)
   testSet.computeHull()
   vertices = testSet.getVertices()
   polygon = getEdges(vertices)
   print "Edges: ", sorted(polygon)
   for s in polygon:
      x1 = s.startPoint.x
      x2 = s.endPoint.x
      y1 = s.startPoint.y
      y2 = s.endPoint.y
      plt.plot([x1, x2], [y1, y2], '-k')

   plt.show()

if __name__=='__main__':
   main()
