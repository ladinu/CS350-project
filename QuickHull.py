from geometry.Point import Point
from geometry.Line import Line

class QuickHull:
   #initialize fields
   def __init__(self, setOfPoints):
      self.pointsCount = len(setOfPoints)
      self.verticesCount = 0
      self.workingSet = list(setOfPoints)
      self.convexHullSet = []
      self.edges = []

   #this method is used to determine whether a point is outside a line segment
   def _isRightOf(self, a, b, somePoint):
      return (a.x - b.x) * (somePoint.y - b.y) - (somePoint.x - b.x) * (a.y - b.y) > 0

   #this method calculates the distance point p is from points a and b
   def _getDistance(self, a, b, p):
      u = float((p.x - a.x)*(b.x - a.x) + (p.y - a.y)*(b.y - a.y)) / float((b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y))
      x = a.x + u * (b.x - a.x)
      y = a.y + u * (b.y - a.y)
      return (x - p.x)*(x - p.x) + (y - p.y)*(y - p.y)

   #this method calculates the furthest points from the given line segment a b
   def _getFarthestPoint(self, a, b, setOfPoints):
      currentDist = 0.0
      maxDistance = -1.0
      maxPoint = None
      for i in setOfPoints:
         if i is a or i is b:
            continue
         currentDist = self._getDistance(a, b, i)
         if currentDist > maxDistance:
            maxDistance = currentDist
            maxPoint = i
      return maxPoint

   #this method main recursive method to calculate the convex hull set
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
         if (pointInQuestion is p1 or pointInQuestion is p2):
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

   #this is a helper method that calculates the left-most and right-most points
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

   #this is a helper method that generates the upper and lower subset of points
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

   #This method computes the convex hull set
   def computeHull(self):
      if self.pointsCount < 2:
         return
      #get left-most and right-most points:
      extremeties = self._getLeftandRightMost(self.workingSet)
      leftMostPoint = extremeties[0]
      rightMostPoint = extremeties[1]
      temp = self._getUpperAndLowerHalf(self.workingSet, leftMostPoint, rightMostPoint)
      upper = temp[0]
      lower = temp[1]
      #initiate recursive quickHull()
      self.convexHullSet.append(rightMostPoint)
      self.verticesCount += 1
      self._quickHull(rightMostPoint, leftMostPoint, upper)
      self.convexHullSet.append(leftMostPoint)
      self.verticesCount += 1
      self._quickHull(leftMostPoint, rightMostPoint, lower)

   #This method gets the set of vertices of the convex hull
   def getVertices(self):
      if self.verticesCount < 1:
         self.computeHull()
      return list(self.convexHullSet)

   #This method returns the edges that make up the convex hull polygon
   def getEdges(self):
      size = len(self.edges)
      if size < 1:
         vertices = self.getVertices()
         i = 0
         while i < len(vertices)-1:
            self.edges.append(Line(Point(vertices[i][0], vertices[i+1][0]), Point(vertices[i][1], vertices[i+1][1])))
            i = i + 1
         self.edges.append(Line(Point(vertices[-1][0], vertices[0][0]), Point(vertices[-1][1], vertices[0][1])))
      return list(self.edges)
