class VirtualMachine:
    def __init__(self, cpu):
        self.cpu = cpu

    # runs command
    def exec(self):
        cmd = self.get_command()

        if cmd == "ADD":
            self.addition()
        elif cmd == "SUB":
            self.subtraction()
        elif cmd == "MUL":
            self.multiplication()
        elif cmd == "DIV":
            self.division()
        elif cmd == "CMP":
            self.compare()
            
        block, word = self.parse_args(cmd)
        if cmd.startswith("GN"):
            self.get_number(block, word)
        elif cmd.startswith("PN"):
            self.put_number(block, word)
        elif cmd.startswith("PD"):
            self.put_data(block, word)
        elif cmd.startswith("JM"):
            self.jump(block, word)
        elif cmd.startswith("JE"):
            self.jump_if_equal(block, word)   
        elif cmd.startswith("JN"):
            self.jump_if_not_equal(block, word)
        elif cmd.startswith("JB"):
            self.jump_if_below(block, word)
        elif cmd.startswith("JA"):
            self.jump_if_above(block, word)      

    def get_command(self):
        pass

    def parse_args(self, cmd):
        pass
    
    # ARITHMETIC OPERATIONS
    def addition(self, block, word):
        pass
    
    def subtraction(self, block, word):
        pass

    def multiplication(self, block, word):
        pass

    def division(self, block, word):
        pass

    def exchange(self):
        pass

    # INPUT / OUTPUT OPERATIONS
    def get_number(self, block, word):
        pass

    def put_number(self, block, word):
        pass

    def put_data(self, block, word):
        pass

    # DATA OPERATIONS
    def get_register(self, block, word):
        pass

    def put_register(self, block, word):
        pass

    def get_shared(self, block, word):
        pass

    def put_shared(self, block, word):
        pass

    # LOGICAL OPERATIONS
    def compare(self):
        pass

    # CONTROL MANAGEMENT OPERATIONS
    def jump(self, block, word):
        pass

    def jump_if_equal(self, block, word):
        pass

    def jump_if_not_equal(self, block, word):
        pass

    def jump_if_below(self, block, word):
        pass

    def jump_if_above(self, block, word):
        pass

    def exit(self):
        pass