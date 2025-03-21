from globals import *
from parse import *
from model import *
from print import *

print( '@startuml generated', file=file2)
print( 'scale 2000 width', file=file2)

parseArgs()

# debug
if len(endpointsToPrint) + len(classesToPrint) == 0 :
  classesToPrint.append('fare')
  classesToPrint.append('farePart')
  supportiveClasses.clear()

parser = parse()

i = 0
while i < len(endpointsToPrint) :
  printClass(findRequest(endpointsToPrint[i]).className, globals.class_depth)
  printClass(findRequest(endpointsToPrint[i]).response.typeName, globals.class_depth)
  i += 1

i = 0
while i < len(classesToPrint) :
  printClass(findClass(classesToPrint[i]), globals.class_depth)
  i += 1

print('@enduml', file=file2)
