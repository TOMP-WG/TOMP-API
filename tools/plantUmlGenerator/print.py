from generator.globals import *
from generator.model import *

printedClasses = []

def printClass(c, d):

  if d < 0:
    # print("Skip " + c.className + ", too far away: " + str(d))
    return

  if c == None:
    return

  if c.className in printedClasses :
    # print("Skip " + c.className + ", already printed")
    return

  if c.className in supportiveClasses:
    # print("Skip " + c.className + ", supportive")
    return

  printedClasses.append(c.className)
  print("Printing: " + c.className, file = sys.stderr)

  toPrint = []
  
  classOrEnum = "class "
  if c.isEnum :
    classOrEnum = "enum "
  elif c.isInterface :
    classOrEnum = "interface "

  for subclass in globals.classes:
    if subclass.superClass == c.className \
      and d >= 1  \
      and subclass.className not in toPrint:
      toPrint.append(subclass.className)

  refs = []

  superText = ''
  if c.superClass != '':
    if c.superClass not in supportiveClasses:
      refs.append ( formatClassName(c.className) + ' -up-|> ' + formatClassName(c.superClass) )
      print( 'Superclass ' + c.superClass )
      toPrint.append( c.superClass )
    else  :
      superText = " <<" + c.superClass + ">>"

  print(classOrEnum + formatClassName(c.className) + superText + ' {', file=file2)
  iAttr = 0
  notes = []
  while iAttr < len(c.attributes) :
    currentAttribute = c.attributes[iAttr]

    req = "  "
    if currentAttribute.isRequired :
      req = " +"
    if not currentAttribute.isRef or d == 0:
      arrayText = ''
      if currentAttribute.isArray:
        arrayText = '[]'
      print( req + formatClassName(currentAttribute.typeName) + arrayText + " " + currentAttribute.name , file=file2)
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

      if not currentAttribute.typeName in supportiveClasses:
        refs.append( formatClassName(c.className) + mult + formatClassName(currentAttribute.typeName) + " : " + currentAttribute.name + " >")
        toPrint.append( currentAttribute.typeName )
      else:
        if currentAttribute.isArray:
          print( req + formatClassName(currentAttribute.typeName) + "[] " + currentAttribute.name , file=file2)
        else:
          print( req + formatClassName(currentAttribute.typeName) + " " + currentAttribute.name , file=file2)

    noteKey = formatClassName(c.className) + "::" + currentAttribute.name
    if currentAttribute.isEnum and noteKey in enumsToPrint:
      note ='note right of ' + noteKey + '\n'
      for enumValue in currentAttribute.enumValues :
        note += enumValue + '\n'
      note += "end note"
      notes.append(note)

    iAttr += 1      

  if c.isEnum and c.className in enumsToPrint :
    for enumValue in c.enumValues :
      print(enumValue, file=file2)

  print("}", file=file2)

  if c.className in interfaces:
    iName = interfaces[c.className]
    refs.append (formatClassName(c.className) + ' .up.> ' + formatClassName(iName) )
    # print('Interface reference: ' + iName)
    toPrint.append( iName )
    
  for interfacedClass in interfaces :
    if interfaces[interfacedClass] == c.className:
      printClass(findClass(interfacedClass), d - 1)

  for note in notes:
    print(note, file=file2)

  iRef = 0
  while iRef < len(refs) :
    print( refs[iRef] , file=file2)
    iRef += 1

  iRef = 0
  if d >= 0:
    while iRef < len(toPrint) :
      # print('Reference found: ' + toPrint[iRef])
      printClass(findClass(toPrint[iRef]), d - 1)
      iRef += 1
  
    # print subclasses
    if c.className in superclasses:
      for key in superclassesOf :
        if superclassesOf[key] == c.className and not key in classesToPrint:
          print( 'Is superclass, printing subclasses')
          printClass(findClass(key), d - 1)
  
