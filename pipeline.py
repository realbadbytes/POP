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
            print ('\n[+] checking data hazard for\n {} and \n{}'.format(op1, op2))

            # detect operator 1 being operator 1 in previous instruction
            if ( (op1.values[1] == op2.values[1]) and (op2.values[0] not in ['LOAD', 'POP']) ):
                print ('\n[!] data hazard between instruction {} and {}'.format(index, index+1))

            # detect operator 2 being operator 1 from previous instruction
            if (len(op2) == 3):
                if (op1.values[1] == op2.values[2]):
                    print ('\n[!] data hazard between instruction {} and {}\n'.format(index, index+1))

        except IndexError:
            pass

    def generate_timing(self):
        print ('\n[+] generating timing chart')
        for i in range(len(self.program)):
            hazards = self.detect_data_hazards(i)







