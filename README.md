Warning! Basilisk is in beta and is *highly buggy*! I miss a lot of things. If you use the interpreter, please send any complaints to bestc@brpsk12.org.

# Basilisk
Basil is a coding language based somewhat off of CJam. The interpreter, named `Basilisk Interpreter.py`, should be run with `python [file pathe to interpreter] [file path to .bsl file]`.

# Overview
Basilisk is stack-based, meaning that all data is stored in a stack. The Basilisk stack can have numbers, strings or functions stored in it. The following is a simple program that prints 9:

    45+
Basilisk reads the 4 and puts it into the stack. The 4 is stored there until it is needed. Then Basilisk reads the 5 and puts it into the stack on top of the 4, so that the stack looks like this: `[5, 4]`. The + command takes the top two items on the stack (in this case 5 and 4), pops (deletes) them, adds them, and pushes (puts onto the top of the stack) the result, leaving the stack as `[9]`. Since the stack is printed when the program ends, it spits out 9.

    "Hello, World!"
This is another basic program that prints "Hello, World!".

# Commands
Here is a list of valid Basilisk commands and what they do:

+ ) Increments the top of the stack by 1.

+ ( Decrements the top of the stack by 1.

+ \+ Pops the top 2 values in stack as A and B, pushes B + A.

+ \- Pops the top 2 values in stack as A and B, pushes B - A.

+ \* Pops the top 2 values in stack as A and B, pushes B * A. String compatible.

+ / Pops the top 2 values in stack as A and B, pushes B / A as an integer.

+ % Pops the top 2 values in stack as A and B, pushes the remainder of B / A.

+ ^ Pops the top 2 values in stack as A and B, pushes B to the A power.

+ | Pops the top value in stack as A, pushes the absolute value of A.

+ @ Pops the top two values in stack as A and B, pushes a random integer between B - 1 and A + 1.


+ i(a/r) Takes user input given at the beginning of the program. If a exists, reads the entire input and pushes it as a string. If r exists, resets the input. Otherwise, reads the first item in the input (items are separated by spaces) and pushes it as a string.

+ o Pops the top value in stack and outputs it to STDOUT.

+ n Pushes a newline.


+ = Pops top 2 values in stack as A and B, pushes 1 if B = A and 0 otherwise. If k exists, keeps the top two values on stack.

+ \> If the top of the stack is not a string, pops top 2 values in stack as A and B, pushes 1 if B > A and 0 otherwise. If the top or next to top of the stack is a string, with N as an integer in the first two items in the stack, cuts N letters off the string and pushes the result, popping the number and original string.

+ < Pops top 2 values in stack as A and B, pushes 1 if B < A and 0 otherwise. If the top or next to top of the stack is a string, with N as an integer in the first two items in the stack, cuts the string starting from N letters and pushes the result, popping the number and original string.

+ ! Pops top value in stack as A, pushes 0 if A is nonzero and 1 otherwise. If k exists, keeps top value on stack.


+ :X With X as a capital character, defines a position in the code as X.

+ gX With X as a capital character, if the top of the stack is nonzero, jumps to predefined position X in the code and continues executing code from there.

+ s Pops top value in stack as A, if A is nonzero, pops top value in stack as B and does not execute next B characters in the code.

+ fX With X as a predefined function variable and A as an integer on top of stack, executes function X A times.


+ d Pushes the top of the stack.

+ &X Pops top value in stack as A, and, with X as an integer, inserts A into the stack X positions down.

+ pX If X is an integer, pops the top X values from stack. Otherwise pops the top value from the stack.

+ $(a) If a exists, sorts the stack, putting the higher values on top and lower values on bottom. Otherwise, sorts the top of the stack.

+ x Pops the entire stack.

+ X If X as a predefined variable or function, pushes X. If X is not already defined, stores the top of the stack in X as a variable.

+ \\X Stores the top of the stack in X as a variable.

+ [Y]X With Y as a string of valid Basil code and X as a capital character, stores Y in X as a function.

+ ?XY If the top value in stack is 0, executes function Y, otherwise executes function X. X and/or Y can be pre-defined functions, single commands or a function defined within the command (enclosed in brackets).


+ "X" With X as a string, pushes X.

+ . Pops top value in stack as A, pushes A as an integer.

+ , Pops top value in stack as A, pushes A as a string.

+ 'X Pushes X as a string, regardless of what X is.

+ c(>,<) Concatenates two strings. If > exists, performs a normal concatenation. If < exists, performs a concatenation that preserves newlines.

+ v(X) If X exists, inserts a newline after every X characters in the top of the stack. Otherwise, inserts a newline after each character in the top of the stack.

+ l Pops the top value in stack as A, pushes the length of A.

+ ~ Pops top 2 strings on stack as A and B. Pushes how many of A there are in B.

+ X With X as an integer, pushes X.

+ e Executes the top of the stack as Basil code.

+ ` Prints the entire stack as a list (used for debugging).


Any other character does nothing.
