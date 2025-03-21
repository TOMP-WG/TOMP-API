import sys

file1 = open('C:\sources\TOMP-API\TOMP-API.yaml', 'r')
file2 = open('output.plantuml', 'w')

Lines = file1.readlines()

class globals :
  classes = []
  requests = []
  class_depth = 20

original_stdout = sys.stdout
classesToPrint = []
endpointsToPrint = []
enumsToPrint = []
interfaces = {}
superclassesOf = {}
superclasses = []
directives = {}
directive = ''


supportiveClasses = [ 'amountOfMoney', 'coordinates', 'country'
                     , 'currencyCode', 'customProperties', 'externalReference'
                     , 'date', 'dateTime', 'day', 'error', 'float', 'httpDate', 'longInt', 'longString', 'normalString', 'normalInt'
                     , 'shortInt', 'shortString', 'time', 'timeWindow', 'tinyInt', 'tinyString', 'url', 'uuid'
                     , 'mode', 'tripState', 'legState', 'requirement'
                     , 'duration', 'distance', 'assetProperties', 'journalCategory', 'bankAccount'
                     , 'LineString', 'Point', 'MultiPolygon', 'geojsonGeometry'
                     , 
                    ]


def formatClassName(cn) :
  return cn[0:1].capitalize() + cn[1:]

def findClass(cname):
  # print ("findClass " + cname)
  ic = 0
  while ic < len(globals.classes) :
    if globals.classes[ic].className == cname : 
      return globals.classes[ic]
    ic += 1
  print ("no class found " + cname)
  return None

def findRequest(methodAndPath) :
  ie = 0
  while ie < len(globals.requests) :
    if globals.requests[ie].method + ' ' + globals.requests[ie].path == methodAndPath :
      return globals.requests[ie]
    ie += 1
  print ("no endpoint found " + methodAndPath)
  return None

