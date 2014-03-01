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

points = getNRandomPoints(50, 0, 50)
#points = [P(45, 9), P(13, 49), P(42, 1), P(49, 13)]
p1, p2 = flatten(points)

plt.plot(p1, p2, 'o')
plt.axis([-10, 60, -10, 60])

print points
simplices = ConvexHull.computeHull(points)
print simplices
for s in simplices:
   x1 = s.startPoint.x
   x2 = s.endPoint.x
   y1 = s.startPoint.y
   y2 = s.endPoint.y

   plt.plot([x1, x2], [y1, y2], '-k')

plt.show()
