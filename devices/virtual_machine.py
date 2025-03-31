from utils.convertion import hex_to_dec, dec_to_hex

# TODO:
# set SF flags
# set CD register values
class VirtualMachine:
    def __init__(self, cpu, channel_device):
        self.cpu = cpu
        self.channel_device = channel_device

    def get_command(self):
        pass

    def parse_args(self, cmd):
        return cmd[2], cmd[3]
    
    # runs command
    def exec(self):
        cmd = self.get_command()

        non_parsable_cmd = 0
        if cmd == "ADD": 
            self.addition()
        elif cmd == "SUB":
            self.subtraction()
            non_parsable_cmd = 1
        elif cmd == "MUL":
            self.multiplication()
            non_parsable_cmd = 1
        elif cmd == "DIV":
            self.division()
            non_parsable_cmd = 1
        elif cmd == "XCHG":
            self.exchange()
            non_parsable_cmd = 1
        elif cmd == "CMP":
            self.compare()
            non_parsable_cmd = 1
        elif cmd == "EXIT":
            return 0

        if non_parsable_cmd:
            return 1
                    
        block_hex, word_hex = self.parse_args(cmd)
        block = hex_to_dec(block_hex)
        word = hex_to_dec(word_hex)

        if cmd.startswith("GN"):
            self.get_number(block, word)
        elif cmd.startswith("PN"):
            self.put_number(block, word)
        elif cmd.startswith("PD"):
            self.put_data(block, word)
        elif cmd.startswith("GR"):
            self.get_register(block, word)
        elif cmd.startswith("PR"):
            self.put_register(block, word)
        elif cmd.startswith("GS"):
            self.get_shared(block, word)
        elif cmd.startswith("PS"):
            self.put_shared(block, word)
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

        return 1

    # ARITHMETIC OPERATIONS
    def addition(self):       
        self.cpu.ax += self.cpu.bx

    def subtraction(self):
        self.cpu.ax -= self.cpu.bx

    def multiplication(self):
        self.cpu.ax *= self.cpu.bx

    def division(self):
        self.cpu.ax /= self.cpu.bx

    def exchange(self):
        temp = self.cpu.ax
        self.cpu.ax = self.cpu.bx
        self.cpu.bx = temp

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