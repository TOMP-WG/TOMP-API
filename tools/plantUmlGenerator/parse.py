from generator.globals import *
from generator.model import *
import sys

def parseArgs() :
  argType = ''
  for i, arg in enumerate(sys.argv):
    # set argument type
    # class to print
    if arg == '-c' :
      argType = 'c'
    # endpoint to print
    elif arg == '-e' :
      argType = 'm'
    # tree depth
    
    elif arg == '-d' :
      argType = 'd'
    # hidden of supportive
    elif arg == '-s':
      argType = 's'
    elif arg == '-h':
      argType = 's'
    # direction
    elif arg == '-t' :
      argType = 'directive1'
    # explicit enum
    elif arg == '-n' :
      argType = 'enums'

    # argument values
    elif argType == 'directive1' :
      directives[arg] = ''
      directive = arg
      argType = 'directive2'
    elif argType == 'directive2' :
      directives[directive] = arg
      argType = 'directive1'
    elif argType == 'enums' :
      enumsToPrint.append(arg)
      classesToPrint.append(arg)
      supportiveClasses.remove(arg)
    elif argType == 's' :
      if arg == '-' :
        supportiveClasses.clear()
      else:
        supportiveClasses.append(arg)
    elif argType == 'd' :
      globals.class_depth = int(arg)
    elif argType == 'c' :
      classesToPrint.append(arg)
    elif argType == 'm' :
      endpointsToPrint.append(arg)
      argType = 'p'
    elif argType == 'p' :
      endpointsToPrint[len(endpointsToPrint)-1] += ' ' + arg
      argType = 'm'

def getClassName(line) :
  return line.replace('$ref: "#/components/schemas/', '').replace('$ref: \'#/components/schemas/','').replace('"', '').replace('\'', '').replace('type:', '').replace('- ','').strip()

class singleClassParser: 
  active = False
  inProperties = False
  inRequired = False
  inEnum = False
  allOf = False
  oneOf = False
  propertyIndex = 0
  currentAttribute = Attribute()

  c = Class()

  def parseLine(self, line, spaces) :
    if line == '' : 
      return -1
    
    if line.startswith('#'):
      return 0

    if spaces == 4 :
      if self.active: return -1
    
      self.c = Class()
      self.c.className = line.replace(':','')
      self.active = True

    if 'enum:' in line:
      self.inEnum = True
      if self.inProperties:
        self.currentAttribute.isEnum = True
      else:
        self.c.isEnum = True

    if self.inEnum:
      enumV = line.replace('enum:','').replace(',','').replace('[','').replace(']','').strip()
      for value in enumV.split(' '):
        if value != '':
          if self.inProperties:
            self.currentAttribute.enumValues.append(value)
          else:
            self.c.enumValues.append(value)
      if ']' in line: self.inEnum = False
    elif self.inProperties:
      if spaces == self.propertyIndex :
        self.currentAttribute = Attribute()
        self.currentAttribute.name = line.replace(':','').strip()
        self.c.attributes.append(self.currentAttribute)
        if self.currentAttribute.name in self.c.requiredAttributes:
          self.currentAttribute.isRequired = True
        self.inEnum = False
      elif 'type:' in line:
        self.currentAttribute.typeName = line.replace('type:','').strip()
        if self.currentAttribute.typeName == 'array':
          self.currentAttribute.isArray = True
      elif 'ref:' in line:
        self.currentAttribute.isRef = True
        self.currentAttribute.typeName = getClassName(line)

    elif self.allOf:
      self.c.superClass = getClassName(line)
      if self.c.superClass not in superclasses:
        superclasses.append(self.c.superClass)
      self.allOf = False
    
    elif self.oneOf:
      self.c.isInterface = True
      if self.c.className not in interfaces:
        interfaces[getClassName(line)] = self.c.className

    elif self.inRequired and 'properties:' not in line:
      self.c.requiredAttributes.append(line.replace('-','').strip())

    if 'type:' in line:
      self.c.typeName = line.replace('type: ', '')
    elif 'properties:' in line:
      self.inProperties = True
      self.inRequired = False
      self.propertyIndex = spaces + 2
    elif 'required:' in line:
      self.inRequired = True
    elif 'allOf:' in line:
      self.allOf = True
    elif 'oneOf:' in line:
      self.oneOf = True
    elif 'discriminator:' in line:
      self.oneOf = False

    return 0

  def get(self):
    return self.c

class classParser :
  classes = []
  p = singleClassParser()

  def parseLine(self, line, spaces) :
    out = self.p.parseLine(line, spaces)
    if out == -1:
      self.classes.append(self.p.get())
      self.p = singleClassParser()
    return 0

  def get(self):
    return self.classes

class singleEndpointParser :
  request = Request()
  active = False
  inBody = False
  inResponses = False

  def __init__(self):
    self.request = Request()
    self.active = False
    self.inBody = False
    self.inResponses = False

  def parseLine(self, line : str, spaces):
    if self.active and (line.startswith('/') or line == ''): 
      self.active = False
      return -1

    if line.startswith('/'):
      self.request.path = line
      self.active = True

    if spaces == 4:
      self.request.method = line.replace(':','')
    elif spaces > 4 :
      if 'requestBody' in line:
        self.inBody = True
      elif 'responses' in line:
        self.inResponses = True
      elif '$ref' in line:
        #if self.request.requestBody != None:
        #  self.request.responses.append(getClassName(line))
        if self.inBody:
          self.request.requestBody = getClassName(line)
        elif self.inResponses and self.request.response == None:
          self.request.response == getClassName(line)        

    return 0
  def get(self):
    return self.request

class endpointParser : 
  activated = False
  active = False
  requests = []
  p = singleEndpointParser()

  def __init__(self):
    self.requests = []

  def parseLine(self, line, spaces) :
    if line.startswith('paths:') and not self.activated:
      self.activated = True
      self.active = True
    if line.startswith('components:'):
      self.active = False

    if self.active :
      out = self.p.parseLine(line, spaces)
      if out == -1:
        self.requests.append(self.p.get())
        self.p = singleEndpointParser()
      return 0
    elif not self.activated: 
      return 0

    return -1

  def get(self):
    return self.requests

class fileParser():
  parser = endpointParser()

  def parse(self) :
    self.parser = endpointParser()

    for line in Lines: 
      spaces = len(line) - len(line.lstrip(' '))
      line = line.strip()
      out = self.parser.parseLine(line, spaces)
      if out == -1 and globals.requests == [] :
        globals.requests = self.parser.get()
        self.parser = classParser()
    globals.classes = self.parser.get()

    iClass = 0
    while iClass < len(globals.classes) :
      iAttr = 0
      c = globals.classes[iClass]
      while iAttr < len(c.attributes) :
        if c.attributes[iAttr].isRef :
          c.attributes[iAttr].classRef = findClass(c.attributes[iAttr].typeName.strip())
          if c.attributes[iAttr].classRef != None and c.attributes[iAttr].classRef.isEnum:
            c.attributes[iAttr].isEnum = True
            c.attributes[iAttr].enumValues = c.attributes[iAttr].classRef.enumValues
        iAttr += 1
      iClass += 1

    return 0

def parse():
  f = fileParser()
  f.parse()
  return f

# PARSING
def parseOld() : 
  paths = False
  requestBody = False
  responses = False
  components = False 
  properties = False
  required = False
  allOf = False
  oneOf = False
  enum = False
  propertyIndex = 0

  currentClass = Class()
  currentPath = ''
  currentRequest = Request()

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
        print("parsing class " + currentClass.className)
        properties = False
        allOf = False
        oneOf = False
        enum = False

      if not properties and spaces == 6 :
        if line.startswith('enum:') :
          currentClass.isEnum = True
          #print( 'Enum ' + currentClass.className)
        elif line.startswith('items:') :
          attr = Attribute()
          attr.isRef = True
          attr.isArray = True
          currentClass.attributes.append (attr)

      if not properties and spaces == 8 and line.startswith('$ref:') :
          attr.typeName = getClassName(line)

      if line.startswith('enum:') :
        enum = True
      if enum :
        if line.strip() != '[' and line.strip() != ']':
          enumV = line.replace('[','').replace(']','').replace(',','').replace( 'enum:' , '')
          if enumV.strip() != '' :
            if properties :
              #print('property ' + attr.name + ' enum ' + enumV)
              attr.enumValues.append(enumV)
            else :
              currentClass.enumValues.append(enumV)
            #print('Enum: ' + enumV)

        if ']' in line :
          enum = False

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
          enum = False

        elif oneOf :
          cn = getClassName(line)
          interfaces[cn] = interfaceName
          if cn not in interfaces:
            print("adding oneof: " + cn)
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
