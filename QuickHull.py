from Geometry import Point
from Geometry import Line

class QuickHull:
   def __init__(self, setOfPoints):
      self.pointsCount = 0
      self.verticesCount = 0
      self.workingSet = setOfPoints
      self.convexHullSet = []

   def _isRightOf(self, a, b, somePoint):
      return (a.x - b.x) * (somePoint.y - b.y) - (somePoint.x - b.x) * (a.y - b.y) > 0

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
      firstHalf = []
      otherHalf = []
      pointInQuestion = None
      for i in range(0, numPoints):
         pointInQuestion = subset[i]
         #might need to use ==
         if pointInQuestion is p1 or pointInQuestion is p2:
            continue
         if self._isRightOf(p1, farthestPoint, pointInQuestion):
            firstHalf.append(pointInQuestion)
         elif self._isRightOf(farthestPoint, p2, pointInQuestion):
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

   def computeHull(self):
      #start with left-most and right-most points of the set
      temp = list(self.workingSet)
      self.workingSet.sort()

      assert set(temp) == set(self.workingSet)
      print "original set: ", temp
      print "workingSet: ", self.workingSet

      #get left-most and right-most points:
      extremeties = self._getLeftandRightMost(self.workingSet)
      leftMostPoint = extremeties[0]
      rightMostPoint = extremeties[1]
      print "leftMost: ", leftMostPoint, ", rightMost: ", rightMostPoint

      #initiate recursive quickHull()
      self._quickHull(leftMostPoint, rightMostPoint, self.workingSet)

   def getVertices(self):
      if self.verticesCount < 1:
         self.computeHull()
      return self.convexHullSet

