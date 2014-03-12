from QuickHull import QuickHull
import BruteForceHull
from geometry.utils import *
import matplotlib.pyplot as plt

def flatten(points):
   xList = []
   yList = []
   for p in points:
      xList.append(p.x)
      yList.append(p.y)
   return (xList, yList)

def plotBruteForceHull():
   points = getNRandomPoints(100, 0, 50)
   p1, p2 = flatten(points)

   plt.plot(p1, p2, 'o')
   plt.axis([-10, 60, -10, 60])

   simplices = BruteForceHull.computeHull(points)
   for s in simplices:
      x1 = s.startPoint.x
      x2 = s.endPoint.x
      y1 = s.startPoint.y
      y2 = s.endPoint.y

      plt.plot([x1, x2], [y1, y2], '-k')

   plt.show()

def plotQuickHull():
   points = getNRandomPoints(100, 0, 50)
   p1, p2 = flatten(points)

   plt.plot(p1, p2, 'o')
   plt.axis([-10, 60, -10, 60])

   qh = QuickHull(points)
   qh.computeHull()

   for e in qh.getEdges():
      plt.plot(e.startPoint, e.endPoint, '--k')
   plt.show()

if __name__ == '__main__':
  #plotQuickHull()
  plotBruteForceHull()
