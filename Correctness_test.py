from pyhull.convex_hull import ConvexHull

from geometry.Line import Line
from geometry.Point import Point as P
from geometry.utils import *

import BruteForceHull
from QuickHull import QuickHull

def getStartAndEndPoint(simplex):
   p1x = simplex.coords[0][0]
   p1y = simplex.coords[0][1]
   p2x = simplex.coords[1][0]
   p2y = simplex.coords[1][1]

   p1 = P(p1x, p1y)
   p2 = P(p2x, p2y)
   return (p1, p2)

def convertToPoints(simplices):
   points = []
   for s in simplices:
      p1, p2 = getStartAndEndPoint(s)
      if p1 not in points:
         points.append(p1)
      if p2 not in points:
         points.append(p2)

   return points

def convertSimplicesToLines(simplices):
   lines = []
   for s in simplices:
      p1, p2 = getStartAndEndPoint(s)
      lines.append(Line(p1, p2))
   return lines


def convertEdgesToPoints(edges):
   points = []
   for e in edges:
      if e.startPoint not in points:
         points.append(e.startPoint)
      if e.endPoint not in points:
         points.append(e.endPoint)
   return points


def filterEdges(edges):
   return filterDuplicateEdges(filterSinglePointEdges(edges))

def filterSinglePointEdges(edges):
   return [e for e in edges if not e.isPoint()]

def filterDuplicateEdges(edges):
   filteredEdges = [edges[0]]
   for e in edges:
      inFilteredList = False
      for fe in filteredEdges:
         if e == fe:
            inFilteredList = True
      if not inFilteredList:
         filteredEdges.append(e)
   return filteredEdges


def filterDuplicateLinesOnHull(edges, points):
   filteredPoints = []
   for e1 in edges:
      for p in points:
         if e1.getDeterminantSign(p) == 0 and p in e1:
            if p not in filteredPoints:
               filteredPoints.append(p)
   return filteredPoints

def sameList(listA, listB):
   if len(listA) != len(listB):
      return False

   for a in listA:
      if a not in listB:
         return False

   return True

def testBruteForceHull():
   print "> Running BruteForce tests..."
   high = 50
   for i in range(3, 50):
      print "  Test %i/%i" % (i, high)
      r = getNRandomPoints(i, -10000, 10000)
      simplices = ConvexHull(r).simplices

      points = convertEdgesToPoints(BruteForceHull.computeHull(r))
      points = filterDuplicateLinesOnHull(convertSimplicesToLines(simplices), points)

      if not sameList(points, convertToPoints(simplices)):
         print "[!] INCORRECT RESULT", r
         exit(1)

def testQuickHull():
   print "> Running QuickHull tests..."
   high = 1000
   for i in range(3, high):
      print "  Test %i/%i" % (i, high)
      r = getNRandomPoints(i, -10000, 10000)
      simplices = ConvexHull(r).simplices

      qh = QuickHull(r)
      qh.computeHull()
      points = filterDuplicateLinesOnHull(convertSimplicesToLines(simplices), qh.convexHullSet)

      if not sameList(points, convertToPoints(simplices)):
         print "[!] INCORRECT RESULT", r
         exit(1)

if __name__ == '__main__':
   testBruteForceHull()
   testQuickHull()
