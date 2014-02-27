import ConvexHull
from Geometry import *
from GeometryUtils import *
from PointUtils import *
import matplotlib.pyplot as plt

P = Point

def flatten(points):
   xList = []
   yList = []
   for p in points:
      xList.append(p.x)
      yList.append(p.y)
   return (xList, yList)

points = [P(25, 25), P(7, 41), P(13, 14), P(0, 49), P(45, 12), P(49, 35), P(24, 42), P(10, 1), P(22, 3), P(32, 12)]

#points = getNRandomPoints(10, 0, 50)
print "Random points: ", points
p1, p2 = flatten(points)

plt.plot(p1, p2, 'o')
plt.axis([-10, 60, -10, 60])

simplices = ConvexHull.computeHull(points)
simplices = [ i for i in simplices if not i.isPoint() ]
print simplices
for s in simplices:
   x1 = s.startPoint.x
   x2 = s.endPoint.x
   y1 = s.startPoint.y
   y2 = s.endPoint.y

   plt.plot([x1, x2], [y1, y2], '-k')

plt.show()

