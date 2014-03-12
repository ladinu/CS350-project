import time
from geometry.utils import getNRandomPoints, getCircle
import BruteForceHull, QuickHull
from math import log

def outStr(a, b):
   return "%i,%f" % (a, b)

def getBruteForceExecTime(points):
   t1 = time.time()
   BruteForceHull.computeHull(points)
   t2 = time.time()
   return t2-t1

def getQuickHullExecTime(points, loopCount=1):
   t1 = time.time()
   qh = QuickHull.QuickHull(points)
   qh.computeHull()
   t2 = time.time()
   return t2-t1

def getBruteForceData():
   print "> Generating execution reports for BruteForce hull..."
   f = open("reports/bruteforce.csv", 'w', 1)
   dataPoints = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
   for d in dataPoints:
      etime = getBruteForceExecTime(getNRandomPoints(i))
      f.write("%s\n" % outStr(d, etime))
      print outStr(d, etime)
   f.close()

def getQuickHullWorstCaseData():
   print "> Generating execution reports for QuickHull worst case..."
   dataPoints = [10000, 20000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000,
         400000, 500000, 600000, 700000, 800000, 90000, 1000000, 10000000]
   f = open("reports/quickhull_worst_case.csv", 'w', 1)
   for d in dataPoints:
      etime = getQuickHullExecTime(getCircle(10000, d))
      f.write("%s\n" % outStr(d, etime))
      print outStr(d, etime)
   f.close()

def getQuickHullData():
   print "> Generating execution reports for QuickHull..."
   f = open('reports/quickhull.csv', 'w', 1)
   for j in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]:
      f.write("%s\n" % outStr(j, getQuickHullExecTime(getNRandomPoints(j))))
      print outStr(j, getQuickHullExecTime(getNRandomPoints(j)))
   f.close()

if __name__ == "__main__":
   getQuickHullData()
   getQuickHullWorstCaseData()
   #print getQuickHullExecTime(getNRandomPoints(100), 10000)
   #f = open("reports/quickhull_time.csv", 'w', 1)
   #for i in range(3, 200):
   #   eTime = getBruteForceExecTime(getNRandomPoints(i), 1)
   #   outStr = "%i,%f" % (i, eTime)
   #   print outStr
   #   f.write("%s\n" % outStr)
   #f.close()
