#!/usr/bin/python3

from parser import Program, Operation
from pipeline import Pipeline

ASM = """LOAD .stack, i10
POP .gp0
POP .gp1
LOAD .gp1, .stack
ADD .gp1, .gp2
ADD .gp3, .gp4
XOR .gp1, m40
LOAD .stack, .gp1"""

def main():

    program = Program(ASM)
    pipeline = Pipeline(program)
    pipeline.generate_timing()

if __name__ == '__main__':
    main()
