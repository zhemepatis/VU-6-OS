from utils.convertion import hex_to_dec, dec_to_hex
from components.pagination_mechanism import PaginationMechanism

class VirtualMachine:
    def __init__(self, cpu, channel_device, memory, ptr):
        self.cpu = cpu
        self.memory = memory
        self.channel_device = channel_device
        self.ptr = ptr
        self.pagination = PaginationMechanism(ptr, memory)

    def parse_args(self, cmd):
        return cmd[2], cmd[3]
      
    def get_command(self):
        pass
    
    def exec(self):
        cmd = self.get_command()
        self.cpu.reset_sf_register()

        valid_cmd = self.handle_non_parsable(cmd)
        if not valid_cmd:
            block_hex, word_hex = self.parse_args(cmd)
            block = hex_to_dec(block_hex)
            word = hex_to_dec(word_hex)

            valid_cmd = self.handle_parsable(cmd, block, word)

        if not valid_cmd:
            self.cpu.set_invalid_operation()
    
    def handle_non_parsable(self, cmd):
        if cmd == "ADD": 
            self.addition()
            return True
        
        if cmd == "SUB":
            self.subtraction()
            return True
        
        if cmd == "MUL":
            self.multiplication()
            return True
        
        if cmd == "DIV":
            self.division()
            return True
        
        if cmd == "XCHG":
            self.exchange()
            return True
        
        if cmd == "CMP":
            self.compare()
            return True

        if cmd == "EXIT":
            self.exit()
            return True
        
        return False
        
    def handle_parsable(self, cmd, block, word):
        if cmd.startswith("GN"):
            self.get_number(block, word)
            return True
        
        if cmd.startswith("PN"):
            self.put_number(block, word)
            return True
        
        if cmd.startswith("PD"):
            self.put_data(block, word)
            return True
        
        if cmd.startswith("GR"):
            self.get_register(block, word)
            return True
        
        if cmd.startswith("PR"):
            self.put_register(block, word)
            return True
        
        if cmd.startswith("GS"):
            self.get_shared(block, word)
            return True
        
        if cmd.startswith("PS"):
            self.put_shared(block, word)
            return True
        
        if cmd.startswith("JM"):
            self.jump(block, word)
            return True
        
        if cmd.startswith("JE"):
            self.jump_if_equal(block, word)
            return True
        
        if cmd.startswith("JN"):
            self.jump_if_not_equal(block, word)
            return True
        
        if cmd.startswith("JB"):
            self.jump_if_below(block, word)
            return True
        
        if cmd.startswith("JA"):
            self.jump_if_above(block, word)
            return True
        
        return False

    # ARITHMETIC OPERATIONS
    def addition(self):
        self.cpu.ax += self.cpu.bx

        if self.cpu.ax == 0:
            self.cpu.set_zero_flag()
            return
        
        if self.cpu.ax > self.cpu.MAX_WORD:
            self.cpu.ax -= (self.cpu.ax / self.cpu.MAX_WORD) * self.cpu.MAX_WORD
            self.cpu.set_carry_flag()
            return

    def subtraction(self, set_ax = True):
        self.cpu.ax -= self.cpu.bx

        if self.cpu.ax == 0:
            self.cpu.set_zero_flag()
            return
        
        if self.cpu.ax < self.cpu.MIN_WORD:
            if set_ax: 
                self.cpu.ax += ((self.cpu.ax / self.cpu.MAX_WORD) + 1) * self.cpu.MAX_WORD
            self.cpu.set_carry_flag()
            return

    def multiplication(self):
        self.cpu.ax *= self.cpu.bx

        if self.cpu.ax == 0:
            self.cpu.set_zero_flag()
            return
        
        if (self.cpu.ax >> 16) ^ 0xFFFF == 0:
            self.set_carry_flag()
            return 

    def division(self):
        self.cpu.ax /= self.cpu.bx

        if self.cpu.bx == 0:
            self.cpu.set_division_by_zero()
            return

        elif self.cpu.ax == 0:
            self.cpu.set_zero_flag()
            return

    def exchange(self):
        temp = self.cpu.ax
        self.cpu.ax = self.cpu.bx
        self.cpu.bx = temp

    # INPUT / OUTPUT OPERATIONS
    def get_number(self, block, word):
        self.cpu.set_get_number()
        # TODO:

    def put_number(self, block, word):
        self.cpu.set_put_number()
        # TODO:

    def put_data(self, block, word):
        self.cpu.set_put_data()
        # TODO:

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
        self.subtraction(False)

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
        self.cpu.set_exit()