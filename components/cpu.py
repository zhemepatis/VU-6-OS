class CPU:
    def __init__(self):
        # const
        self.MIN_WORD = 0
        self.MAX_WORD = 4294967295
        # registers
        self.ax = 56
        self.bx = 0
        self.ptr = 0
        self.sm = 0
        self.mode = 0
        self.sf = 0x4
        self.ic = 0
        # interrupts
        self.si = 0
        self.pi = 0
        self.ti = 10
        # others
        self.memory = None
        self.pagination = None
        self.channel_device = None

    def initialise_memory(self, memory):
        self.memory = memory

    def initialise_pagination(self, pagination):
        self.pagination = pagination

    def initialise_channel_device(self, channel_device):
        self.channel_device = channel_device

    def get_command(self):
        vm_block = self.ic >> 8
        vm_word = (vm_block << 8) ^ self.ic
        block, word = self.pagination.convert_address(vm_block, vm_word)
        
        return self.memory.memory[block][word]
    
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

    # TI INTERRUPT
    def decrement_timer(self, io_operation = False):
        if io_operation:
            self.ti = max(self.ti - 3, 0)
        else:
            self.ti = max(self.ti - 1, 0)

    # SM REGISTER
    def put_semaphor_register(self):
        self.sm = 1

    def raise_semaphor_register(self):
        self.sm = 0

    # SF REGISTER
    def reset_sf_register(self):
        self.sf >>= 2
        self.sf <<= 2

    def get_zero_flag(self):
        return (self.sf & 0x2) >> 1 # 0b010

    def set_zero_flag(self):
        self.sf |= 0x2 # 0b010

    def get_carry_flag(self):
        return (self.sf & 0x1) # 0b010

    def set_carry_flag(self):
        self.sf |= 0x1 # 0b001

    def get_operation_mode_flag(self):
        return self.sf >> 2

    def change_operation_mode_flag(self):
        self.sf ^= 0x4 # 0b100 

    # IC REGISTER
    def set_ic_register(self, vm_block, vm_word):
        self.ic = vm_block << 8 | vm_word

    def increment_ic_register(self, increment = 1):
        block = self.ic >> 8
        word = (block << 8) ^ self.ic

        block += int((word + increment) / self.memory.BLOCK_LENGTH)
        word = (word + increment) % self.memory.BLOCK_LENGTH

        self.set_ic_register(block, word)

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
        dividend = self.ax
        divisor = self.bx

        self.ax = int(dividend / divisor) << 8 | (dividend % divisor)

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
    def get_number(self, vm_block, vm_word):
        block, word = self.pagination.convert_address(vm_block, vm_word)

        # source - keyboard input
        self.channel_device.ST = 4
        # destination - user memory
        self.channel_device.DB = block
        self.channel_device.DO = word
        self.channel_device.DT = 1

        self.set_get_number()

    def put_number(self, vm_block, vm_word):
        block, word = self.pagination.convert_address(vm_block, vm_word)

        # source - user memory
        self.channel_device.ST = 1
        self.channel_device.SB = block
        self.channel_device.SO = word
        # destination - monitor
        self.channel_device.DT = 4

        self.set_put_number()

    def put_data(self, vm_block, vm_word):
        block, word = self.pagination.convert_address(vm_block, vm_word)

        # source - user memory
        self.channel_device.ST = 1
        self.channel_device.SB = block
        self.channel_device.SO = word
        # destination - monitor
        self.channel_device.DT = 4

        self.set_put_data()

    # DATA OPERATIONS
    def get_register(self, vm_block, vm_word):
        block, word = self.pagination.convert_address(vm_block, vm_word)
        self.memory.memory[block][word] = self.ax

    def put_register(self, vm_block, vm_word):
        block, word = self.pagination.convert_address(vm_block, vm_word)
        self.ax = self.memory.memory[block][word]

    def get_shared(self, block, word):
        offset = self.memory.SHARED_MEMORY_START
        self.ax = self.memory.memory[offset + block][word]

    def put_shared(self, block, word):
        offset = self.memory.SHARED_MEMORY_START
        self.memory.memory[offset + block][word] = self.ax

    # LOGICAL OPERATIONS
    def compare(self):
        self.subtraction(False)

    # CONTROL MANAGEMENT OPERATIONS
    def jump(self, vm_block, vm_word):
        # block, word = self.pagination.convert_address(vm_block, vm_word)
        self.set_ic_register(vm_block, vm_word)

    def jump_if_equal(self, vm_block, vm_word):
        zero_flag = self.get_zero_flag()
        
        if zero_flag == 1:
            block, word = self.pagination.convert_address(vm_block, vm_word)
            self.set_ic_register(block, word)

    def jump_if_not_equal(self, vm_block, vm_word):
        zero_flag = self.get_zero_flag()

        if zero_flag == 0:
            block, word = self.pagination.convert_address(vm_block, vm_word)
            self.set_ic_register(block, word)

    def jump_if_below(self, vm_block, vm_word):
        carry_flag = self.get_carry_flag()

        if carry_flag == 1:
            block, word = self.pagination.convert_address(vm_block, vm_word)
            self.set_ic_register(block, word)

    def jump_if_above(self, vm_block, vm_word):
        zero_flag = self.get_zero_flag()
        carry_flag = self.get_carry_flag()

        if zero_flag == 0 and carry_flag == 0:
            block, word = self.pagination.convert_address(vm_block, vm_word)
            self.set_ic_register(block, word)