# Start Symbol:
# <EXP>

# Terminal Symbols:
# {+,-,*,/,(,),NUM}, where "NUM" is any number

# Production Rules:
# <EXP> -> NUM
# <EXP> -> -<EXP>
# <EXP> -> (<EXP>)
# <EXP> -> <EXP> + <EXP>
# <EXP> -> <EXP> - <EXP>
# <EXP> -> <EXP> * <EXP>
# <EXP> -> <EXP> / <EXP>

import sys

class Parser:
    def __init__(self, text):
        self.text = text
        self.stack = []
        self.a = ""
        self.action = "SHIFT"
        self.stackString = ""
        self.inputElement = 0
        self.ac = "REDUCE TO EXP -> "
        self.stacklength = len(self.stack)

    def popandstuff(self, x):
        for i in range(x):
            self.stack.pop()
        self.stack.append("<EXP>")
        self.stackString = ""
        for i in range(len(self.stack)):
            self.stackString = self.stackString + self.stack[i]
        print("$" + self.stackString + "\t" + self.a + "$" + "\t", end='')
    
    def twopart(self, first, last):
        self.stacklength = len(self.stack)
        if self.stacklength > 2 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == first:
                if self.stack[self.stacklength - 3] != "<EXP>":
                    print(self.ac + first + last)
                    self.popandstuff(2)
        elif self.stacklength > 1 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == first:
                print(self.ac + first + last)
                self.popandstuff(2)

                
    def threepart(self, first, middle, last):
        self.stacklength = len(self.stack)
        if self.stacklength > 2 and self.stack[self.stacklength - 1] == last:
            if self.stack[self.stacklength - 2] == middle:
                if self.stack[self.stacklength - 3] == first:
                    print(self.ac + first + middle + last)
                    self.popandstuff(3)

    def number(self):
        # Check <EXP> -> NUM
        self.stacklength = len(self.stack)
        if self.stack[self.stacklength - 1].isnumeric():
            print(self.ac + "NUM")
            self.popandstuff(1)

    def checkrules(self):
        # Checking for production rules in the stack
        self.number()
        self.twopart("-", "<EXP>")
        self.threepart("(","<EXP>",")")
        self.threepart("<EXP>", "+", "<EXP>")
        self.threepart("<EXP>", "-", "<EXP>")
        self.threepart("<EXP>", "*", "<EXP>")
        self.threepart("<EXP>", "/", "<EXP>")

    def checkvalid(self):
        self.stacklength = len(self.stack)
        if (self.stacklength == 1 and self.stack[self.stacklength - 1] == "<EXP>"):
            print("Accept")
            print("Syntax Analysis complete. The equation is syntactically correct.")
        else:
            print("Reject")
            print("Syntax Analysis complete. The equation is syntactically wrong.")
            sys.exit()

    def maincheck(self):
        for x in range(len(self.text)):
            # Reset variables
            self.a = ""
            self.stackString = ""

            # Print action
            print(self.action)

            # Pushing into stack
            self.stack.append(self.text[x][0])
            # Make all the elements in the stack a string
            # so that it is easier to print
            for i in range(len(self.stack)):
                self.stackString = self.stackString + self.stack[i]

            # Move forward the pointer for the input string
            self.inputElement = self.inputElement + 1
            # Make all the elements in the the input array a
            # string so that it is easier to print
            for i in range(len(self.text) - self.inputElement):
                self.a = self.a + self.text[i + self.inputElement][0]

            # Print stack and input
            print("$" + self.stackString + "\t" + self.a + "$" + "\t", end='')

            self.checkrules()

    def parser(self):
        for x in range(len(self.text) - self.inputElement):
            self.a = self.a + self.text[x + self.inputElement][0]
        print("stack \t input \t action")
        print("$ \t" + self.a + "$" + "\t", end='')

        # Main function for shift reduce parser
        self.maincheck()

        # Check for production rules one last time
        self.checkrules()

        # Check if syntax is correct or not
        self.checkvalid()


            



