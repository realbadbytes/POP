#!/usr/bin/python

from parser import Program, Operation

ASM = """LOAD .stack, i10
LOAD .stack, i10
POP .gp0
POP .gp1
ADD .gp1, .gp2
XOR .gp1, m40
LOAD .stack, .gp1"""

def main():

    p = Program(ASM)

if __name__ == '__main__':
    main()
