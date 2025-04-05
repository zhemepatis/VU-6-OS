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
    
    # PI INTERRUPT
    def set_invalid_address(self):
        self.pi = 0x1

    def set_invalid_operation(self):
        self.pi = 0x2

    def set_division_by_zero(self):
        self.pi = 0x3

    def set_overflow(self):
        self.pi = 0x4

    # SI INTERRUPT
    def set_get_number(self):
        self.si = 0x1

    def set_put_number(self):
        self.si = 0x2

    def set_put_data(self):
        self.si = 0x3

    def set_exit(self):
        self.si = 0x4

    def set_put_shared(self):
        self.si = 0x5

    def set_get_shared(self):
        self.si = 0x6

    # TI INTERRUPT
    def decrement_timer(self):
        if self.ti > 0:
            self.ti -= 1

    # SF REGISTER
    def reset_sf_register(self):
        self.sf >>= 2
        self.sf <<= 2

    def set_zero_flag(self):
        self.cpu.sf |= 0x2 # 0b010

    def set_carry_flag(self):
        self.cpu.sf |= 0x1 # 0b001

    def change_operation_mode_flag(self):
        self.cpu.sf ^= 0x3 # 0b100