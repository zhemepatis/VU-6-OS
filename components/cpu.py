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
        self.ti = 0

    def reset_sf(self):
        self.sf = 0b00