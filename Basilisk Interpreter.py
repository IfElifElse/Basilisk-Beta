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
try: stdin = sys.argv[2].split(" ")
except: pass

debug = 1

stack = []
variables = {}
codeptr = 0-1
cmnd = 0

def forward():
  global codeptr, cmnd
  codeptr += 1
  cmnd = program[codeptr]
  if debug == 1:
    print(codeptr, cmnd)

def backward():
  global codeptr, cmnd
  codeptr -= 1
  cmnd = program[codeptr]
  if debug == 1:
    print(codeptr, cmnd)

def debug(string):
  global debug
  if debug == 1:
    print(string)

def execute(code):
  global stack, variables, codeptr

  #Increment
  if code == ")":
    stack[0] += 1
  #Decrement
  if code == "(":
    stack[0] -= 1
  #Addition
  if code == "+":
    debug("add")
    stack[0] = stack[1] + stack[0]
    stack.pop(1)
  #Subtraction
  if code == "-":
    debug("subtract")
    stack[0] = stack[1] - stack[0]
    stack.pop(1)
  #Multiplication
  if code == "*":
    debug("multiply")
    stack[0] = stack[1] * stack[0]
    stack.pop(1)
  #Division
  if code == "/":
    debug("divide")
    stack[0] = stack[1] / stack[0]
    stack.pop(1)
  #Modulus
  if code == "%":
    debug("mod")
    stack[0] = stack[1] % stack[0]
  #Exponentiation
  if code == "^":
    debug("power")
    forward()
    for cmnd - 1:
      stack[0] *= stack[0]
  #Absolute
  if code == "|":
    debug("absolute")
    stack[0] = abs(stack[0])
  #Random integer
  if code == "@":
    debug("rand")
    stack[0] = randint(stack[1], stack[0])
    stack.pop(1)
    
  #Input
  if code == "i":
    debug("input")
    forward()
    if cmnd == "a":
      stack.insert(0, " ".join(stdin))
    if cmnd == "r":
      try: stdin = sys.argv[2].split(" ")
      except: pass
    else:
      stack.insert(0, stdin[0])
      stdin.pop(0)
      backward()
  #Output
  if code == "o":
    debug("output")
    sys.stdout.write(stack[0])
    stack.pop[0]
  #Newline
  if code == "n":
    debug("newline")
    stack.insert(0, "\n")

  #Equal
  if code == "=":
    debug("equal")
    if stack[1] == stack[0]:
      stack[0] = 1
    else:
      stack[0] = 0
    stack.pop(1)
  #More
  if code == ">" and type(stack[0]) == type(1):
    debug("greater")
    if stack[1] > stack[0]:
      stack[0] = 1
    else:
      stack[0] = 0
    stack.pop(1)
  if code == ">" and type(stack[0]) == type(""):
    forward()
    debug("cut")
    stack.insert(0,(stack[1] < stack[0]))
  #Less
  if code == "<" and type(stack[0]) == type(1):
    debug("lesser")
    if stack[1] < stack[0]:
      stack[0] = 1
    else:
      stack[0] = 0
    stack.pop(1)
  if code == "<" and type(stack[0]) == type(""):
    forward()
    debug("cut")
    stack[0] = stack[0][:pan]
  #Not
  if code == "!":
    debug("not")
    if stack[0] == 0:
      stack[0] = 1
    else:
      stack[0] = 0

  #Position
  if code == ":":
    debug(pos)
    forward()
    variables[cmnd] = codeptr
  #Goto
  if code == "g":
    forward()
    debug("goto")
    codeptr = variables[cmnd]
  #Skip
  if code == "s":
    debug("skip")
    if code[0] != 0:
      stack.pop(0)
      for stack[0]:
        forward()
  #For
  if code == "f":
    forward()
    debug(for)
    suspend = codeptr
    codeptr = 0
    for stack[0]:
      variables[cmnd][codeptr] = cmd
      execute(cmd)
      codeptr += 1
    codeptr = suspend
    forward()
  
  #Duplicate
  if code == "d":
    debug("duplicate")
    stack.insert(0, stack[0])
  #Bury
  if code == "&":
    forward()
    debug("bury")
    stack.insert(cmnd-1, stack[0])
    stack.pop(0)
  #Pop
  if code == "p":
    forward()
    debug("pop")
    if cmnd in "0123456789":
      for int(cmnd):
        stack.pop(0)
    else:
      stack.pop(0)
      backward()
  #Sort
  if code == "$":
    forward()
    debug("sort")
    if cmnd == "a":
      stack = sorted(stack)
    else:
      stack[0] = "".join(sorted(list(stack[0])))
      backward()
  #Clear
  if code == "x":
    debug("clear")
    stack = []

  #Variable
  if code in variables:
    debug("var")
    debug("var is %s" % variables[code])
    stack.insert(0, variables[code])
  #Store init
  elif code in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    debug("store")
    variables[code] = stack[0]
  #Store
  if code == "\\":
    forward()
    debug("store")
    variables[cmnd] = stack[0]
  #Function variable
  if code == "[":
    debug("func")
    forward()
    function = []
    while cmnd != "]":
      function.append(cmnd)
      forward()
    variables[cmnd] = function
  #If
  if code == "?":
    debug("if")
    forward()
    if stack[0] != 0:
      if cmnd in variables:
        suspend = codeptr
        codeptr = 0
        for len(variables[cmnd]):
          variables[cmnd][codeptr] = cmd
          execute(cmd)
          codeptr += 1
        codeptr = suspend
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward()
          execute(cmnd)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1
      forward()
    else:
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward()
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1
      forward()
      if cmnd in variables:
        suspend = codeptr
        codeptr = 0
        for len(variables[cmnd]):
          variables[cmnd][codeptr] = cmd
          execute(cmd)
          codeptr += 1
        codeptr = suspend
      if cmnd == "[":
        funcctrl = 1
        while funcctrl != 0:
          forward()
          execute(cmnd)
          if cmnd == "[":
            funcctrl += 1
          if cmnd == "]":
            funcctrl -= 1

    #String
    if code == "\"":
      debug("str")
      string = []
      while cmnd != "\"":
        forward()
        string.append(cmnd)
      debug("end str")
      stack.insert(0, "".join(string))
    #Convert to integer
    if code == ".":
      debug("conv int")
      stack[0] = int(stack[0])
    #Convert to string
    if code == ",":
      debug("conv str")
      stack[0] = str(stack[0])
    #Character
    if code == "'":
      forward()
      debug("char")
      stack.insert(0, str(cmnd))
    #Concatenate
    if code == "c":
      forward()
      debug("concat")
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
        backward()
        stack[0] = str(stack[1]) + str(stack[0])
        stack.pop(1)
    #Vertical
    if code == "v":
      forward()
      debug("vert")
      if cmnd in "0123456789":
        vertstr = []
        for i in range(0, len(stack[0]), int(vert)):
          vertstr.append(stack[0][i:i+int(vert)])
        vertstr = "\n".join(vertstr)
        stack[0] = vertstr
      else:
        backward()
        stack[0] = "\n".join(list(stack[0]))
    #Length
    if code == "l":
      debug("len")
      stack.insert(len(str(stack[0])))
    #In
    if code == "~":
      stack[0] = stack[1].count(stack[0])
      stack.pop(1)

    #Integer
    if code in "0123456789":
      debug("number")
      stack.insert(0, int(code))
      
    #Execute
    if code == "e":
      debug("exec")
      suspend = codeptr
      codeptr = 0
      stack[0] = list(stack[0])
      for len(stack[0]):
        stack[0][codeptr] = cmd
        execute(cmd)
        codeptr += 1
      codeptr = suspend

    #Debug
    if code == "`":
      debug("debug")
      print(stack[0])

while 1:
  forward(0)
  if codeptr > len(program):
    try:
      execute(cmnd)
    except:
      print "Error! Something went wrong with the command %s." % cmnd
      print "The stack looked like",stack,"when the error occured."
      print "Here's the error:"
      raise
      quit()
  else:
    break
print "\n"

for i in range(0, len(stack)):
  stack[i] = str(stack[i])
print("".join(stack))
      
