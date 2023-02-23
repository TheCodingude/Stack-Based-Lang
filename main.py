import sys
from typing import List
from enum import Enum, auto


class Tokens(Enum):

    PUSH = auto()
    POP = auto()
    PEEK = auto()
    PRINT = auto()
    PLUS = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVISION = auto()
    EXPONENT = auto()
    FLOOR_DIV = auto()

def readFileReturnTokens(file):
    tokens = []
    with open(file, "r") as f:
        lines: List[str] = f.readlines()
        for line in lines:
            line = line.split("#")[0].strip()
            for word in line.split(" "):
                if str(word) != "\n":
                    tokens.append(str(word).removesuffix("\n"))
    return tokens


def interpret(tokens):
    stack = []
    virtual_memory = []
    c = None
    d = None
    for i, token in enumerate(tokens):
        try:
            stack.append(int(token))
        except Exception:
            if token == "push":
                stack.append(tokens[i+1])
            elif token == "pop":
                c = stack.pop()
            elif token == "peek":
                c = stack[len(stack) - 1]
            elif token == ",":
                print(stack.pop())
            elif token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                c = stack.pop()
                d = stack.pop()
                stack.append(d - c)
            elif token == "*":
                c = stack.pop()
                d = stack.pop()
                stack.append(c * d)
            elif token == "/":
                c = stack.pop()
                d = stack.pop()
                stack.append(d / c)
            elif token == "^":
                c = stack.pop()
                d = stack.pop()
                stack.append(c ** d)
            elif token == "//":
                c = stack.pop()
                d = stack.pop()
                stack.append(d // c)
            elif token == " " or "\n":
                pass
            else:
                assert False, f"Unknown Token Found: {token}"

def compile(tokens, output_file):
    with open(output_file, "w") as f:
        f.write("")



# if len(sys.argv) == 1:
#     print("ERROR")
#     print("MUST PROVIDE FILE NAME\n")
#     print("must also provide a flag:\n")
#     print("-i to interpret the program")
#     print("-c to compile the program")
#     print("if compiling, use -r to run after compilation")
#     exit(1)
# file = sys.argv[1]
# tokens = readFileReturnTokens(file)


# if "-i" in sys.argv:
#     interpret(file)
# elif "-c" in sys.argv:
#     compile(file)

tokens = readFileReturnTokens("test.txt")
interpret(tokens)

# python3 main.py test.txt -c test.asm