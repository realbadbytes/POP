#!/usr/bin/python3

class Program:

    def __init__(self, prog_string):
        print ('[+] initializing program\n')
        self.operations = []
        self.instructions = prog_string.split('\n')
        self.inst_count = len(self.instructions)

        print ('[+] program: {0}, instruction count {1}\n'.format(repr(self.instructions), self.inst_count))

        print ('[+] generating Operation array\n')
        for instruction in self.instructions:
            self.operations.append(Operation(instruction))

        print ('[+] result: {0}\n'.format(repr(self.operations)))

    def __len__(self):
        return len(self.operations)


class Operation:

    def __init__(self, raw_op):
        print ('[+] initializing operation\n')
        self.values = raw_op.split(' ')
        # terrible way of removing comma after split
        if ',' in self.values[1]:
            self.values[1] = self.values[1].strip(',')
        self.length = len(self.values)

        print ('[+] parsed operation: {0}, size {1}\n'.format(repr(self.values), self.length))

    def __repr__(self):
        return '{}'.format(self.values)



