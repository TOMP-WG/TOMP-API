import sys

file1 = open('C:\sources\TOMP-API\TOMP-API.yaml', 'r')
original_stdout = sys.stdout

file2 = open('output.plantuml', 'w')

classesToPrint = []
endpointsToPrint = []
interfaces = {}
superclassesOf = {}
superclasses = []
directives = {}
directive = ''

depth = 20
argType = ''

supportiveClasses = ['coordinates', 'country', 'assetClass', 'bookingState', 'legState', 'duration', 'distance', 'assetProperties', 'journalCategory', 'bankAccount']

# def parseArgs() :
for i, arg in enumerate(sys.argv):
  if arg == '-c' :
    argType = 'c'
  elif arg == '-e' :
    argType = 'm'
  elif arg == '-d' :
    argType = 'd'
  elif arg == '-s' :
    argType = 's'
  elif arg == '-t' :
    argType = 'directive1'
  elif argType == 'directive1' :
    directives[arg] = ''
    directive = arg
    argType = 'directive2'
  elif argType == 'directive2' :
    directives[directive] = arg
    argType = 'directive1'
  elif argType == 's' :
    supportiveClasses.append(arg)
  elif argType == 'd' :
    depth = int(arg)
  elif argType == 'c' :
    classesToPrint.append(arg)
  elif argType == 'm' :
    endpointsToPrint.append(arg)
    argType = 'p'
  elif argType == 'p' :
    endpointsToPrint[len(endpointsToPrint)-1] += ' ' + arg
    argType = 'm'

Lines = file1.readlines()

class Class:
  attributes = []  
  className = ''
  isEnum = False
  isInterface = False
  requiredAttributes = []
  superClass = ''

  def __init__(self):
    self.attributes = []

class Attribute:
  isRef = False
  isArray = False
  isRequired = False
  isEnum = False
  name = ''
  typeName = ''
  classRef = Class()

class Request:
  method = ''
  path = ''
  className = ''
  response = Attribute()

paths = False
requestBody = False
responses = False
components = False 
properties = False
required = False
allOf = False
oneOf = False
propertyIndex = 0

currentClass = Class()
currentPath = ''
currentRequest = Request()
classes = []
requests = []

def findClass(cname):
  ic = 0
  while ic < len(classes) :
    if classes[ic].className == cname : 
      return classes[ic]
    ic += 1
  print ("no class found " + cname)
  return None

def findRequest(methodAndPath) :
  ie = 0
  while ie < len(requests) :
    if requests[ie].method + ' ' + requests[ie].path == methodAndPath :
      return requests[ie]
    ie += 1
  print ("no endpoint found " + methodAndPath)
  return None

def getClassName(line) :
  return line.replace('$ref: "#/components/schemas/', '').replace('$ref: \'#/components/schemas/','').replace('"', '').replace('\'', '').replace('type:', '').replace('- ','').strip()

def formatClassName(cn) :
  return cn[0:1].capitalize() + cn[1:]

printedClasses = []

def printClass(c, d):
  if c.className in printedClasses :
    return

  if c.className in supportiveClasses:
    return

  printedClasses.append(c.className)
  print("Printing: " + c.className, file = sys.stderr)

  classOrEnum = "class "
  if c.isEnum :
    classOrEnum = "enum "
  elif c.isInterface :
    classOrEnum = "interface "

  toPrint = []
  refs = []

  superText = ''
  if c.superClass != '':
    if c.superClass not in supportiveClasses:
      refs.append ( formatClassName(c.className) + ' -up-|> ' + formatClassName(c.superClass) )
      toPrint.append( c.superClass )
    else  :
      superText = " <<" + c.superClass + ">>"


  print(classOrEnum + formatClassName(c.className) + superText + ' {', file=file2)
  iAttr = 0
  while iAttr < len(c.attributes) :
    currentAttribute = c.attributes[iAttr]

    req = "  "
    if currentAttribute.isRequired :
      req = " +"
    if not currentAttribute.isRef or depth == 1:
      print( req + formatClassName(currentAttribute.typeName) + " " + currentAttribute.name , file=file2)
    else :
      mult = ' -- '
      if currentAttribute.name in directives :
        mult = ' -' + directives[currentAttribute.name] + '- '

      if currentAttribute.isRequired :
        if currentAttribute.isArray :
          mult = mult + ' "1..n" '
        else :
          mult = mult + ' "1..1" '
      else :
        if currentAttribute.isArray :
          mult = mult + ' "0..n" '
        else :
          mult = mult + ' "0..1" '

      if currentAttribute.isArray :
        if currentAttribute.name in directives :
          mult = ' -' + directives[currentAttribute.name] + '-{ '
        else: 
          mult = ' -{ '

      refs.append( formatClassName(c.className) + mult + formatClassName(currentAttribute.typeName) + " : " + currentAttribute.name + " >")
      if d > 0 :
        toPrint.append( currentAttribute.typeName )
    iAttr += 1      

  print("}", file=file2)

  if c.className in interfaces:
    iName = interfaces[c.className]
    refs.append (formatClassName(c.className) + ' .up.> ' + formatClassName(iName) )
    toPrint.append( iName )
    
  for interfacedClass in interfaces :
    if interfaces[interfacedClass] == c.className:
      printClass(findClass(interfacedClass), 1)
      # print(c.className + ": " + interfacedClass)

  iRef = 0
  while iRef < len(refs) :
    print( refs[iRef] , file=file2)
    iRef += 1

  if d > 0 :
    iRef = 0
    while iRef < len(toPrint) :
      printClass(findClass(toPrint[iRef]), d - 1)
      iRef += 1
  
  # print subclasses
  if c.className in superclasses:
    iSub = 0
    for key in superclassesOf :
      if superclassesOf[key] == c.className and not key in classesToPrint:
        #classesToPrint.append(key)
        printClass(findClass(key), 1)
  
# PARSING
for line in Lines:
  spaces = len(line) - len(line.lstrip(' '))
  line = line.strip()

  if line == '' :
    continue

  if (line.startswith('paths:')):
    paths = True

  if paths :
    if (line.startswith('/')):
      currentPath = line.replace(':', '')

    if (spaces == 4 and not line.startswith('parameters:')) :
      currentRequest = Request()
      currentRequest.method = line.replace(':', '')
      currentRequest.path = currentPath
      requests.append(currentRequest)
      requestBody = False
      responses = False

    if (line.startswith('requestBody')) :
      requestBody = True

    if (requestBody and line.startswith('$ref:')) :
      currentRequest.className = getClassName(line)
      requestBody = False

    if (line.startswith('responses')) :
      responses = True

    if (responses and (line.startswith('type:') or line.startswith('$ref:'))) :
      currentRequest.response = Attribute()
      currentRequest.response.isRef = True
      currentRequest.response.typeName = getClassName(line)
      if 'array' in line :
        currentRequest.response.isArray = True

      if line.startswith('$ref:') :
        responses = False

  if (line.startswith('components:')):
    paths = False
    components = True    

  if (line.startswith('parameters:')):
    components = False

  if components:    
    if spaces == 4 :
      currentClass = Class()
      classes.append(currentClass)
      currentClass.className = line.replace(':','')
      properties = False
      allOf = False
      oneOf = False

    if not properties and spaces == 6 :
      if line.startswith('enum:') :
        currentClass.isEnum = True
      elif line.startswith('items:') :
        attr = Attribute()
        attr.isRef = True
        attr.isArray = True
        currentClass.attributes.append (attr)

    if not properties and spaces == 8 and line.startswith('$ref:') :
        attr.typeName = getClassName(line)
    
    if spaces == 6 and line.startswith('allOf:') :
      allOf = True

    if allOf :
      if line.startswith('- $ref'):
        currentClass.superClass = getClassName(line.replace('- ', ''))
        if currentClass.className not in superclassesOf:
          superclassesOf[currentClass.className] = currentClass.superClass
        if currentClass.superClass not in superclasses:
          superclasses.append(currentClass.superClass)
        allOf = False

    if line.startswith('properties:') :
      properties = True
      propertyIndex = spaces + 2

    if required :
      currentClass.requiredAttributes.append( line.replace( '-', '').strip() )

    if line.startswith('required:') :
      required = True

    if properties :
      required = False

      if spaces == propertyIndex: 
        attr = Attribute()
        attr.isRef = False
        attr.name = line.replace(":", '')
        attr.isRequired = attr.name in currentClass.requiredAttributes
        currentClass.attributes.append(attr)

      elif oneOf :
        cn = getClassName(line)
        interfaces[cn] = interfaceName
        if cn not in interfaces:
          classesToPrint.append(cn)

      elif line.startswith('oneOf:') :
        oneOf = True
        interfaceName = 'OneOf' + formatClassName(attr.name)
        interf = Class()
        interf.className = interfaceName
        interf.isInterface = True
        classes.append(interf)

        attr.typeName = interfaceName
        attr.isRef = True

      elif spaces > propertyIndex and not oneOf and (line.startswith('type:') or line.find('$ref:') >= 0) :
        if line.startswith('-') :
          line = line.replace('-', '').strip()
        attr.isRef = line.startswith('$ref:')
        attr.typeName = getClassName(line)
        if 'array' in line :
          attr.isArray = True
        if line.startswith('enum:') :
          attr.isEnum = True
        if attr.typeName in supportiveClasses :
          attr.isRef = False
          if attr.isArray :
            attr.typeName = attr.typeName + '[]'

# iterate classes
iClass = 0
while iClass < len(classes) :
  iAttr = 0
  c = classes[iClass]
  while iAttr < len(c.attributes) :
    if c.attributes[iAttr].isRef :
      c.attributes[iAttr].classRef = findClass(c.attributes[iAttr].typeName.strip())
    iAttr += 1
  iClass += 1

print( '@startuml', file=file2)

# debug
if len(endpointsToPrint) + len(classesToPrint) == 0 :
  classesToPrint.append('leg')

i = 0
while i < len(endpointsToPrint) :
  printClass(findRequest(endpointsToPrint[i]).className, depth)
  printClass(findRequest(endpointsToPrint[i]).response.typeName, depth)
  i += 1

i = 0
while i < len(classesToPrint) :
  printClass(findClass(classesToPrint[i]), depth)
  i += 1

print('@enduml', file=file2)
