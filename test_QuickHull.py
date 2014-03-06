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
   #workingSet = [P(20,20), P(40, 20), P(30, 20), P(30, 40), P(30, 1)]
   workingSet = getNRandomPoints(25, 0, 50)
   p1, p2 = _flatten(workingSet)

   plt.plot(p1, p2, 'o')
   plt.axis([-10, 60, -10, 60])

   testSet = QuickHull(workingSet)
   testSet.computeHull()
   vertices = testSet.getVertices()
   polygon = getEdges(sorted(vertices))
   print "Vertices: ", sorted(vertices)
   print "Edges: ", sorted(polygon)

   #plot set of vertices
   i = 0
   while i < len(vertices)-1:
      plt.plot([vertices[i][0], vertices[i+1][0]], [vertices[i][1], vertices[i+1][1]], '-k')
      i = i + 1
   plt.plot([vertices[-1][0], vertices[0][0]], [vertices[-1][1], vertices[0][1]], '-k')
   plt.show()

if __name__=='__main__':
   main()
