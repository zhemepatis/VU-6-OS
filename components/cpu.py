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
        self.sf |= 0x2 # 0b010

    def set_carry_flag(self):
        self.sf |= 0x1 # 0b001

    def change_operation_mode_flag(self):
        self.sf ^= 0x3 # 0b100

    # ARITHMETIC OPERATIONS
    def addition(self):
        self.ax += self.bx

        if self.ax == 0:
            self.set_zero_flag()
            return
        
        if self.ax > self.MAX_WORD:
            self.ax -= (self.ax / self.MAX_WORD) * self.MAX_WORD
            self.set_carry_flag()
            return

    def subtraction(self, set_ax = True):
        self.ax -= self.bx

        if self.ax == 0:
            self.set_zero_flag()
            return
        
        if self.ax < self.MIN_WORD:
            if set_ax: 
                self.ax += ((self.ax / self.MAX_WORD) + 1) * self.MAX_WORD
            self.set_carry_flag()
            return

    def multiplication(self):
        self.ax *= self.bx

        if self.ax == 0:
            self.set_zero_flag()
            return
        
        if (self.ax >> 16) ^ 0xFFFF == 0:
            self.set_carry_flag()
            return 

    def division(self):
        self.ax /= self.bx

        if self.bx == 0:
            self.set_division_by_zero()
            return

        elif self.ax == 0:
            self.set_zero_flag()
            return

    def exchange(self):
        temp = self.ax
        self.ax = self.bx
        self.bx = temp

    # INPUT / OUTPUT OPERATIONS
    def get_number(self, block, word):
        self.set_get_number()
        # TODO:

    def put_number(self, block, word):
        self.set_put_number()
        # TODO:

    def put_data(self, block, word):
        self.set_put_data()
        # TODO:

    # DATA OPERATIONS
    def get_register(self, block, word):
        # TODO:
        # value = self.ax
        # self.pagination.put_value(block, word, value)
        pass

    def put_register(self, block, word):
        # TODO:
        # value = self.pagination.get_value(block, word, value)
        # self.ax = value
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
        self.set_exit()