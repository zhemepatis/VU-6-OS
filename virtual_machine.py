from utils.convertion import hex_str_to_int

class VirtualMachine:
    def __init__(self, cpu):
        self.cpu = cpu

    def parse_args(self, cmd):
        return cmd[2], cmd[3]
    
    def exec(self):
        cmd = self.cpu.get_command()
        print(f"\nCurrent command: {cmd}")
        self.cpu.reset_sf_register()

        valid_cmd = self.handle_non_parsable(cmd)
        if valid_cmd:
            self.cpu.increment_ic_register()
            return
        
        block_hex, word_hex = self.parse_args(cmd)
        block = hex_str_to_int(block_hex)
        word = hex_str_to_int(word_hex)

        valid_cmd, control_transfer_cmd= self.handle_parsable(cmd, block, word)
        if valid_cmd:
            increment = 0 if control_transfer_cmd else 1
            self.cpu.increment_ic_register(increment)
            return
    
        self.cpu.set_invalid_operation()
        return
    
    def handle_non_parsable(self, cmd):
        if cmd == "ADD": 
            self.cpu.addition()
            return True
        
        if cmd == "SUB":
            self.cpu.subtraction()
            return True
        
        if cmd == "MUL":
            self.cpu.multiplication()
            return True
        
        if cmd == "DIV":
            self.cpu.division()
            return True
        
        if cmd == "XCHG":
            self.cpu.exchange()
            return True
        
        if cmd == "CMP":
            self.cpu.compare()
            return True

        if cmd == "EXIT":
            self.cpu.set_exit()
            return True
        
        return False
    
    def handle_parsable(self, cmd, block, word):
        if cmd.startswith("GN"):
            self.cpu.get_number(block, word)
            return (True, False)
        
        if cmd.startswith("PN"):
            self.cpu.put_number(block, word)
            return (True, False)
        
        if cmd.startswith("PD"):
            self.cpu.put_data(block, word)
            return (True, False)
        
        if cmd.startswith("GR"):
            self.cpu.get_register(block, word)
            return (True, False)
        
        if cmd.startswith("PR"):
            self.cpu.put_register(block, word)
            return (True, False)
        
        if cmd.startswith("GS"):
            self.cpu.get_shared(block, word)
            return (True, False)
        
        if cmd.startswith("PS"):
            self.cpu.put_shared(block, word)
            return (True, False)
        
        if cmd.startswith("JM"):
            self.cpu.jump(block, word)
            return (True, True)
        
        if cmd.startswith("JE"):
            self.cpu.jump_if_equal(block, word)
            return (True, True)
        
        if cmd.startswith("JN"):
            self.cpu.jump_if_not_equal(block, word)
            return (True, True)
        
        if cmd.startswith("JB"):
            self.cpu.jump_if_below(block, word)
            return (True, True)
        
        if cmd.startswith("JA"):
            self.cpu.jump_if_above(block, word)
            return (True, True)
        
        return (False, None)