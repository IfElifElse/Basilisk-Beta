import sys
from random import randint
try:
  file = sys.argv[1]
except:
  print("Drag and drop a Basilisk file into the terminal!")
  quit()
code = open(file)
program = code.read()
program = list(program)
stdin = []
try:
  for i in range(2,len(sys.argv)):
    stdin.append(sys.argv[i])
except:
  pass

debug = 0

if debug == 1 and stdin != []:
  try:
    print(stdin)
  except:
    "".append(stdin)
    pass

stack = []
variables = {}
codeptr = 0
cmnd = 0
stop = 0
begin = 1
funcvar = 0
stack0 = 0

def forward(var):
  global codeptr, cmnd, stop, begin, variables, funcvar
  if var == 0:
    codeptr += 1
    if begin == 1:
      begin = 0
      codeptr = 0
    if len(program) > codeptr:
      cmnd = program[codeptr]
    else:
      stop = 1
  if var == 1:
    codeptr += 1
    cmnd = variables[funcvar][codeptr]
  if var == 2:
    codeptr += 1
    cmnd = stack0[codeptr]
  if debug == 1:
    print(codeptr, cmnd)

def backward(var):
  global codeptr, cmnd
  if var == 0:
    codeptr -= 1
    cmnd = program[codeptr]
  if var == 1:
    codeptr -= 1
    cmnd = variables[funcvar][codeptr]
  if var == 2:
    codeptr -= 1
    cmnd = stack[0][codeptr]
  if debug == 1:
    print(codeptr, cmnd)

def execute(code, var):
  global stack, variables, codeptr, cmnd, stdin, funcvar, stack0

  #Increment
  if code == ")":
    stack[0] += 1
  #Decrement
  if code == "(":
    stack[0] -= 1
  #Addition
  if code == "+":
    stack[0] = stack[1] + stack[0]
    stack.pop(1)
  #Subtraction
  if code == "-":
    stack[0] = stack[1] - stack[0]
    stack.pop(1)
  #Multiplication
  if code == "*":
    stack[0] = stack[1] * stack[0]
    stack.pop(1)
  #Division
  if code == "/":
    if type(stack[0]) = type(""):
      split = stack[1].split(stack[0])
      stack.pop(1)
      for i in range(len(split) - 1):
        stack.insert(0, split[i])
    else:
      stack[0] = stack[1] / stack[0]
      stack.pop(1)
    
  #Modulus
  if code == "%":
    stack[0] = stack[1] % stack[0]
    stack.pop(1)
  #Exponentiation
  if code == "^":
    forward(var)
    exponent = stack[0]
    stack.pop(0)
    base = stack[0]
    for i in range(exponent-1):
      stack[0] *= base
  #Absolute
  if code == "|":
    stack[0] = abs(stack[0])
  #Random integer
  if code == "@":
    stack[0] = randint(stack[1], stack[0])
    stack.pop(1)
    
  #Input
  if code == "i":
    forward(var)
    if cmnd == "a":
      stack.insert(0, " ".join(stdin))
    elif cmnd == "r":
      try: stdin = sys.argv[2].split(" ")
      except: pass
    else:
      stack.insert(0, stdin[0])
      stdin.pop(0)
      backward(var)
  #Output
  if code == "o":
    sys.stdout.write(str(stack[0]))
    stack.pop(0)
  #Newline
  if code == "n":
    stack.insert(0, "\n")

  #Equal
  if code == "=":
    if stack[1] == stack[0]:
      stack[0] = 1
    else:
      stack[0] = 0
    stack.pop(1)
  #More
  if code == ">":
    if type(stack[0]) == type(1) and type(stack[1]) == type(1):
      if stack[1] > stack[0]:
        stack[0] = 1
      else:
        stack[0] = 0
      stack.pop(1)
    elif type(stack[0]) == type(""):
      stack[0] = stack[0][stack[1]:]
      stack.pop(1)
    elif type(stack[1]) == type(""):
      stack[0] = stack[1][stack[0]:]
      stack.pop(1)
  #Less
  if code == "<":
    if type(stack[0]) == type(1) and type(stack[1]) == type(1):
      if stack[1] < stack[0]:
        stack[0] = 1
      else:
        stack[0] = 0
      stack.pop(1)
    elif type(stack[0]) == type(""):
      stack[0] = stack[0][:stack[1]]
      stack.pop(1)
    elif type(stack[1]) == type(""):
      stack[0] = stack[1][:stack[0]]
      stack.pop(1)
  #Not
  if code == "!":
    if stack[0] == 0:
      stack[0] = 1
    else:
      stack[0] = 0

  #Position
  if code == ":":
    forward(var)
    variables[cmnd] = codeptr
  #Goto
  if code == "g":
    forward(var)
    if stack[0] != 0:
      if code == "s":
        codeptr = 0
      else:
        codeptr = variables[cmnd]
  #Jump
  if code == "j":
    if code[0] != 0:
      for i in range(stack[0]):
        forward(var)
    stack.pop(0)
  #For
  if code == "f":
    forward(var)
    suspend = codeptr
    funcvar = cmnd
    stack0 = stack[0]
    stack.pop(0)
    ctrl = 0
    for i in range(stack0):
      ctrl += 1
      if debug == 1:
        print ctrl
      codeptr = -1
      while codeptr != len(variables[funcvar])-1:
        forward(1)
        execute(cmnd, 1)
    codeptr = suspend
    forward(var)
  #While
  if code == "w":
    forward()
    elif cmnd == "[":
      whilectrl = []
      funcctrl = 1
      while funcctrl != 0:
        whilectrl.append[cmnd]
    def test():
      if cmnd in variables:
        whilectrl = variables[cmnd]
      else:
        suspend = codeptr
        codeptr = -1
        while codeptr != len(whilectrl)-1:
          forward(2)
          execute(cmnd, 2)
        return stack[0]
    codeptr = suspend
    forward()
    beginLoop = codeptr
    while test() != 0:
      codeptr = beginLoop
      while cmnd != "]":
        forward(0)
        execute(cmnd, 0)

  #Duplicate
  if code == "d":
    stack.insert(0, stack[0])
  #Bury
  if code == "&":
    forward(var)
    stack.insert(int(cmnd), stack[0])
    stack.pop(0)
  #Pop
  if code == "p":
    forward(var)
    if cmnd in "0123456789":
      for i in range(int(cmnd)):
        stack.pop(0)
    else:
      stack.pop(0)
      backward(var)
  #Sort
  if code == "$":
    forward(var)
    if cmnd == "a":
      stack = sorted(stack)
    else:
      stack[0] = "".join(sorted(list(stack[0])))
      backward(var)
  #Clear
  if code == "x":
    stack = []

  #Variable
  if code in variables:
    stack.insert(0, variables[code])
  #Store init
  elif code in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    variables[code] = stack[0]
    if type(stack[0]) == type([]):
      stack.pop(0)
  #Store
  if code == "\\":
    forward(var)
    variables[cmnd] = stack[0]
  #Function variable
  if code == "[":
    if debug == 1:
      print"Func begin"
    forward(var)
    function = []
    funcctrl = 1
    while funcctrl != 0:
      function.append(cmnd)
      forward(var)
      if cmnd == "[":
        funcctrl += 1
      if cmnd == "]":
        funcctrl -= 1
    stack.insert(0, function)
    if debug == 1:
      print"Func end"
  #If
  if code == "?":
    forward(var)
    if stack[0] != 0:
      stack.pop(0)
      if cmnd != "[":
        if cmnd in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
          suspend = codeptr
          codeptr = -1
          funcvar = cmnd
          while codeptr != len(variables[funcvar])-1:
            forward(1)
            execute(cmnd, 1)
          codeptr = suspend
        else:
          execute(cmnd, var)
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward(var)
          execute(cmnd, var)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1
      forward(var)
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward(var)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1
    else:
      stack.pop(0)
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward(var)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1
      forward(var)
      if cmnd != "[":
        if cmnd in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
          suspend = codeptr
          codeptr = -1
          funcvar = cmnd
          while codeptr != len(variables[funcvar])-1:
            forward(1)
            execute(cmnd, 1)
          codeptr = suspend
        else:
          execute(cmnd, var)
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward(var)
          execute(cmnd, var)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1

  #String
  if code == "\"":
    string = []
    forward(var)
    while cmnd != "\"":
      string.append(cmnd)
      forward(var)
    stack.insert(0, "".join(string))
  #Convert to integer
  if code == ".":
    stack[0] = int(stack[0])
  #Convert to string
  if code == ",":
    stack[0] = str(stack[0])
  #Character
  if code == "'":
    forward(var)
    stack.insert(0, str(cmnd))
  #Concatenate
  if code == "c":
    forward(var)
    if cmnd == "n":
      short1 = 0
      short0 = 0
      str0 = stack[0].split("\n")
      str1 = stack[1].split("\n")
      if len(str0) >= len(str1):
          shorter = len(str1)
          short1 = 1
      else:
          shorter = len(str0)
          short0 = 1
      conStr = []
      for i in range(0, shorter):
        conStr.append(str1[i] + str0[i])
        if debug == 1:
          print conStr
      stack.pop(0)
      stack.pop(0)
      stack.insert(0, "\n".join(conStr))
    else:
      backward(var)
      stack[0] = str(stack[1]) + str(stack[0])
      stack.pop(1)
  #Vertical
  if code == "v":
    forward(var)
    if cmnd in "0123456789":
      vertstr = []
      for i in range(0, len(stack[0]), int(cmnd)):
        vertstr.append(stack[0][i:i+int(cmnd)])
      vertstr = "\n".join(vertstr)
      stack[0] = vertstr
    else:
      backward(var)
      stack[0] = "\n".join(list(stack[0]))
  #Length
  if code == "l":
    stack.insert(0, len(str(stack[0])))
  #In
  if code == "~":
    stack[0] = stack[1].count(stack[0])
    stack.pop(1)

  #Integer
  if code in "0123456789":
    stack.insert(0, int(code))
      
  #Execute
  if code == "e":
    suspend = codeptr
    codeptr = -1
    stack0 = list(stack[0])
    stack.pop(0)
    while codeptr != len(stack0)-1:
      forward(2)
      execute(cmnd, 2)
    codeptr = suspend

  #String manipulation (s)
  if code == "s":
    forward(var)
    #Insert
    if cmnd == "i":
      modString = list(stack[2])
      modString.insert(stack[0]-1, stack[1])
      stack[0] = "".join(modString)
      stack.pop(1)
      stack.pop(1)
    #Replace
    if cmnd == "r":
      modString = list(stack[2])
      modString[stack[0]] = stack[1]
      stack[0] = "".join(modString)
      stack.pop(1)
      stack.pop(1)
    #Position
    if cmnd == "p":
      stack[0] = stack[1].index(stack[0])
      stack.pop(1)
    #Get
    if cmnd == "g":
      stack[0] = stack[1][stack[0]]
    #Remove
    if cmnd == "x":
      modString = list(stack[1])
      if type(stack[0]) == type(1):
        modString.pop(stack[0]-1)
      elif type(stack[0]) == type(""):
        forward(var)
        if cmnd == "o":
          modString.pop(modString.index(stack[0]))
#        else:
#          backward(var)
#          for i in modString:
#            if modString[i]
    

  #Debug
  if code == "`":
    print(stack)

while 1:
  forward(0)
  if stop != 1:
    try:
      execute(cmnd, 0)
    except:
      print "Error! Something went wrong with the command \"%s\"." % cmnd
      print "The stack looked like",stack,"when the error occured."
      if debug == 1:
        raise
      try:
        raise
      except IndexError:
        print
        print "The stack was probably empty."
      quit()
  else:
    break

stack = list(reversed(stack))
for i in range(0, len(stack)):
  stack[i] = str(stack[i])
print("".join(stack))
print
