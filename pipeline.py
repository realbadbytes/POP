#!/usr/bin/python3

import numpy as np
from parser import Operation

registers = ['.gp0', '.gp1', '.gp2', '.gp3', '.gp4', '.gp5', '.gp6', '.stack', '.next']


class Pipeline():

    def __init__(self, program):
        self.program = program
        print ('[+] initializing pipeline for')
        for op in program.operations:
            print (op)
        
        print ('\n[+] initializing pipeline matrix')
        self.pipeline = np.chararray((len(program)*2, len(program)*2))
        self.pipeline[:] = ''
        print (self.pipeline)

    def detect_data_hazards(self, index):
        """ look ahead one instruction and check for data hazard """
        try:
            op1 = self.program.operations[index]
            op2 = self.program.operations[index+1]
            print ('[+] checking data hazard for\n {} and \n{}'.format(op1, op2))

            if (op1.values[1] == op2.values[1]):
                print ('\n[!] data hazard between instruction {} and {}\n'.format(index, index+1))

        except IndexError:
            pass

    def generate_timing(self):
        print ('\n[+] generating timing chart')
        for i in range(len(self.program)):
            print ('[+] processing instruction {}: {}'.format(i, self.program.operations[i]))
            hazard = self.detect_data_hazards(i)







