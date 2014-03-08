import time
from geometry.utils import getNRandomPoints
import BruteForceHull

def getBruteForceExecTimeForPoints(points):
   t1 = time.time()
   BruteForceHull.computeHull(points)
   t2 = time.time()
   return t2-t1


if __name__ == "__main__":
   print getBruteForceExecTimeForPoints(getNRandomPoints(100))
