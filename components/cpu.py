class CPU:
    def __init__(self):
        # const
        self.MIN_WORD = 0
        self.MAX_WORD = 4294967295
        # registers
        self.ax = 0
        self.bx = 0
        self.ptr = 0
        self.sm = 0
        self.mode = 0
        self.sf = 0
        self.ic = 0
        # interrupts
        self.si = 0
        self.pi = 0
        self.ti = 10

    def reset_sf_register(self):
        self.sf ^= 0b011

    def set_zero_flag(self):
        self.cpu.sf |= 0b010

    def set_carry_flag(self):
        self.cpu.sf |= 0b001

    def change_operation_mode(self):
        self.cpu.sf ^= 0b100
        
    def decrement_timer(self):
        if self.ti > 0:
            self.ti -= 1
