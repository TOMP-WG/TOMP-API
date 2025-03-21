class Class:
  attributes = []  
  className = ''
  isEnum = False
  isSuperClass = False
  isInterface = False
  requiredAttributes = []
  superClass = ''
  enumValues = []

  def __init__(self):
    self.attributes = []
    self.requiredAttributes = []
    self.enumValues = []

class Attribute:
  isRef = False
  isArray = False
  isRequired = False
  isEnum = False
  name = ''
  typeName = ''
  classRef = Class()
  enumValues = []

  def __init__(self):
    self.enumValues = []

class Parameter:
  ref = ''

class Request:
  method = ''
  path = ''
  className = ''
  response = Attribute()
  responses = {}
  requestBody = ''
  parameters = []

  def __init__(self):
    self.method = ''
    self.path = ''
    self.className = ''
    self.response = Attribute()
    self.requestBody = ''
    self.parameters = []
    self.responses = {}
