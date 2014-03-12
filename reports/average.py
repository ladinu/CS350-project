#!/usr/bin/env python


def getPoints(inFile):
   c = open(inFile, 'r').readlines()
   return [i.split(',')[0] for i in c]

def getTime(inputFile):
   c = open(inputFile, 'r').readlines()
   c = [i.rstrip('\n') for i in c]
   c = [i.split(',')[1] for i in c]
   return [float(i) for i in c]


def getAvg(lists):
   n = len(lists[0])
   ret = lists[0]
   for i in range(n):
      ret[i] += lists[1][i]
      ret[i] += lists[2][i]
   for i in range(n):
      ret[i] = ret[i] / 3.0
   return ret

def printCSV(column1, column2):
   print "Points,Time (seconds)"
   for i in range(len(column1)):
      print "%s,%s" % (column1[i], column2[i])

files = ['quickhull_worst_case_0.csv', 'quickhull_worst_case_1.csv', 'quickhull_worst_case_2.csv']
points = getPoints(files[0])
files = [getTime(i) for i in files]
files = getAvg(files)

printCSV(points, files)
