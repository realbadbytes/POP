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
        """ Look ahead one instruction and check for data hazard """
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
                    print ('\n\t ***** data hazard between instruction {} and {}\n'.format(index, index+1))

        except IndexError:
            pass

    def detect_structural_hazards(self, index):
        """ Look ahead one instruction and check for structural hazard on memory bus """
        try:
            op1 = self.program.operations[index]
            op2 = self.program.operations[index+1]
            print ('\n[+] checking structural hazard for\n {} and \n{}'.format(op1, op2))

            # handle safe cases where all operands are either regs or immediates in first operation
            # these can be interleaved
            if (len(op1) == 3):
                if ((op1.values[1][:3] == '.gp' or op1.values[1][0] == 'i') and 
                        (op1.values[2][:3] == '.gp' or op1.values[2][0] == 'i')):
                    return

            # handle safe cases where all operands are either regs or immediates in second operation
            # these can be interleaved
            if (len(op2) == 3):
                if ((op2.values[1][:3] == '.gp' or op2.values[1][0] == 'i') and 
                        (op2.values[2][:3] == '.gp' or op2.values[2][0] == 'i')):
                    return

            # there is a memory hazard otherwise
            print ('\n\t ***** structural hazard (memory bus) between instruction {} and {}'.format(index, index+1))


        except IndexError:
            pass

    def generate_timing(self):
        print ('\n[+] generating timing chart')
        for i in range(len(self.program)):
            print("\n#############################")
            data_hazards = self.detect_data_hazards(i)
            structural_hazards = self.detect_structural_hazards(i)






