import sys
from typing import List

def readFileReturnTokens(file):
    tokens = []
    with open(file, "r") as f:
        lines: List[str] = f.readlines()
        for line in lines:
            for word in line.split(" "):
                if str(word) != "\n":
                    tokens.append(str(word).removesuffix("\n"))
    return tokens


def interpret(file):
    stack = []
    tokens = readFileReturnTokens(file)
    for i, token in enumerate(tokens):
        if token == "push":
            stack.append(tokens[i+1])
        elif token == "pop":
            c = stack.pop()
        elif token == ",":
            print(c, end="")
        elif token == "20":
            pass
        else:
            assert False, f"Unknown Token Found: {token}, type: {type(token)}"

def compile(file):
    pass



# if len(sys.argv) == 1:
#     print("ERROR")
#     print("MUST PROVIDE FILE NAME\n")
#     print("must also provide a flag:\n")
#     print("-i to interpret the program")
#     print("-c to compile the program")
#     print("if compiling, use -r to run after compilation")
#     exit(1)
# file = sys.argv[1]

# if "-i" in sys.argv:
#     interpret(file)
# elif "-c" in sys.argv:
#     compile(file)

interpret("test.txt")

