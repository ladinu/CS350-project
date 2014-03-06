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

def getCirclePoints(centerX, centerY, radius):
   x = radius
   y = 0
   radiusError = 1 - x
   circle = []
   while(x >= y):
      circle.append(Point(x + centerX, y + centerY))
      circle.append(Point(y + centerX, x + centerY))
      circle.append(Point(-x + centerX, y + centerY))
      circle.append(Point(-y + centerX, x + centerY))
      circle.append(Point(-x + centerX, -y + centerY))
      circle.append(Point(-y + centerX, -x + centerY))
      circle.append(Point(x + centerX, -y + centerY))
      circle.append(Point(y + centerX, -x + centerY))
      y += 1
      if (radiusError<0):
         radiusError += 2 * y + 1
      else:
         x -= 1
         radiusError += 2 * (y - x + 1)
   return circle

def main():
   #workingSet = [P(20,20), P(40, 20), P(30, 20), P(30, 40), P(30, 1)]
   workingSet = getNRandomPoints(35, 0, 50)
   #workingSet = getCirclePoints(25, 25, 20)
   print "Points Set: ", workingSet
   p1, p2 = _flatten(workingSet)

   plt.plot(p1, p2, 'o')
   plt.axis([-10, 60, -10, 60])

   testSet = QuickHull(workingSet)
   testSet.computeHull()
   vertices = testSet.getVertices()
   print "Vertices: ", sorted(vertices)
   edges = testSet.getEdges()
   print "Edges: ", sorted(edges)

   #plot set of vertices as edges
   for e in edges:
      plt.plot(e.startPoint, e.endPoint, '-k')
   plt.show()

if __name__=='__main__':
   main()
