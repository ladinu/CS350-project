from Geometry import Point
from Geometry import Line

class QuickHull:
   def __init__(self, setOfPoints):
      self.pointsCount = len(setOfPoints)
      self.verticesCount = 0
      self.workingSet = list(setOfPoints)
      self.convexHullSet = []
      self.edges = []

   def _isRightOf(self, a, b, somePoint):
      return (a.x - b.x) * (somePoint.y - b.y) - (somePoint.x - b.x) * (a.y - b.y)


#   def _getDistance(int a, int b, int p)
#      x, y, u
#      u = ((p.x - a.x)*(b.x - (float)xPoints[a]) + ((float)yPoints[p] - (float)yPoints[a])*((float)yPoints[b] - (float)yPoints[a]))
#          / (((float)xPoints[b] - (float)xPoints[a])*((float)xPoints[b] - (float)xPoints[a]) + ((float)yPoints[b] - (float)yPoints[a])*((float)yPoints[b] - (float)yPoints[a]));
#      x = (float)xPoints[a] + u * ((float)xPoints[b] - (float)xPoints[a]);
#      y = (float)yPoints[a] + u * ((float)yPoints[b] - (float)yPoints[a]);
#      return ((x - (float)xPoints[p])*(x - (float)xPoints[p]) + (y - (float)yPoints[p])*(y - (float)yPoints[p]));

   def _getFarthestPoint(self, a, b, setOfPoints):
      currentDist = 0.0
      maxDistance = -1.0
      maxPoint = None
      for i in setOfPoints:
         if i is a or i is b:
            continue
         currentDist = max(Line(a, i).getDistance(), Line(b, i).getDistance())
         if currentDist > maxDistance:
            maxDistance = currentDist
            maxPoint = i
      return maxPoint

   def _quickHull(self, p1, p2, subset):
      numPoints = len(subset)
      if numPoints < 1:
         return
      farthestPoint = self._getFarthestPoint(p1, p2, subset)
      print "farthestPoint: ", farthestPoint
      firstHalf = []
      otherHalf = []
      pointInQuestion = None
      for i in range(0, numPoints):
         pointInQuestion = subset[i]
         #might need to use ==
         if (pointInQuestion is p1 or pointInQuestion is p2):
            continue
         if self._isRightOf(p1, farthestPoint, pointInQuestion) > 0:
            firstHalf.append(pointInQuestion)
         elif self._isRightOf(farthestPoint, p2, pointInQuestion) > 0:
            otherHalf.append(pointInQuestion)
      #solve firstHalf set
      self._quickHull(p1, farthestPoint, firstHalf)
      #add farthestPoint to the ConvexHull set
      self.convexHullSet.append(farthestPoint)
      self.verticesCount += 1
      #solve for otherHalf
      self._quickHull(farthestPoint, p2, otherHalf)

   def _getLeftandRightMost(self, setOfPoints):
      itrtr = lIndex = rIndex = 0
      points = setOfPoints
      for i in points:
         pointL = points[lIndex]
         pointR = points[rIndex]
         if((pointR.x < i.x)):
            rIndex = itrtr
         if((pointL.x > i.x)):
            lIndex = itrtr
         itrtr += 1
      return [setOfPoints[lIndex], setOfPoints[rIndex]]

   def _getUpperAndLowerHalf(self, setOfPoints, leftMost, rightMost):
      if len(setOfPoints) < 2:
         return None
      upper = []
      lower = []
      for i in setOfPoints:
         if (i is leftMost or i is rightMost):
            continue
         if self._isRightOf(rightMost, leftMost, i) > 0:
            upper.append(i)
         else:
            lower.append(i)
      return [upper, lower]

   def computeHull(self):
      if self.pointsCount < 2:
         return
      #start with left-most and right-most points of the set
      print "workingSet: ", self.workingSet

      #get left-most and right-most points:
      extremeties = self._getLeftandRightMost(self.workingSet)
      leftMostPoint = extremeties[0]
      rightMostPoint = extremeties[1]
      print "leftMost: ", leftMostPoint, ", rightMost: ", rightMostPoint

      temp = self._getUpperAndLowerHalf(self.workingSet, leftMostPoint, rightMostPoint)
      upper = temp[0]
      lower = temp[1]
      print "upper-half: ", upper
      print "lower-half: ", lower
      #initiate recursive quickHull()
      self.convexHullSet.append(rightMostPoint)
      self.verticesCount += 1
      self._quickHull(rightMostPoint, leftMostPoint, upper)
      self.convexHullSet.append(leftMostPoint)
      self.verticesCount += 1
      self._quickHull(leftMostPoint, rightMostPoint, lower)

   def getVertices(self):
      if self.verticesCount < 1:
         self.computeHull()
      return self.convexHullSet

   def getEdges(self):
      return list(self.edges)
