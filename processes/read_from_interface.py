class ReadFromInterface:
    def __init__(self, cpu):
        self.cpu = cpu

        self.step = 1
        self.input = None

    def exec(self):
        if self.step == 1:
            self.step = 2
            return

        if self.step == 2:
            self.input = input()
            self.step = 3
            return

        if self.step == 3:
            result = self.parse_run() # TODO: where to save program name?
            self.step = 5 if result == None else 4
            return

        if self.step == 4:
            pass

        if self.step == 5:
            pass

        if self.step == 6:
            success = self.parse_one_word("SWITCHMODE")
            self.step = 7 if success else 8
            return

        if self.step == 7:
            self.cpu.change_operation_mode_flag()
            self.step = 5
            return

        if self.step == 8:
            success = self.parse_one_word("EXIT")
            self.step = 8 if success else 10
            return

        if self.step == 9:
            pass

        if self.step == 10:
            step_by_step_mode = self.cpu.get_operation_mode_flag() == 1
            self.step = 11 if step_by_step_mode else 13
            return

        if self.step == 11:
            success = self.parse_one_word("PRINTCPU")
            self.step = 12 if success else 13
            return

        if self.step == 12:
            self.print_cpu()
            self.step = 4
            return

        if self.step == 13:
            success = self.parse_one_word("PRINTVM")
            self.step = 14 if success else 15
            return

        if self.step == 14:
            self.print_vm_memory()
            self.step = 4
            return

        if self.step == 15:
            success = self.parse_one_word("PRINTRM")
            self.step = 16 if success else 17
            return

        if self.step == 16:
            self.print_vm_memory()
            self.step = 4
            return

        if self.step == 17:
            pass


    # PARSING
    def parse_run(self):
        if self.input.startswith("RUN"):
            trimmed = self.input[3:].replace(" ", "")
            return trimmed
        
        return None
    
    def parse_one_word(self, cmd):
        if self.input.startswith(cmd):
            return True
        
        return False
    
    # PRINTING
    def print_cpu(self, cpu):
        print("\nGeneral use registers")
        print(f"AX: {hex(cpu.ax)}")
        print(f"BX: {hex(cpu.bx)}")

        print("\nOther registers")
        print(f"PTR: {hex(cpu.ptr)}")
        print(f"SM: {hex(cpu.sm)}")
        print(f"MODE: {hex(cpu.mode)}")
        print(f"SF: {hex(cpu.sf)}")
        print(f"IC: {hex(cpu.ic)}")

        print("\nInterrupts")
        print(f"SI: {hex(cpu.si)}")
        print(f"PI: {hex(cpu.pi)}")
        print(f"TI: {hex(cpu.ti)}")


    def print_real_memory(self, memory):
        for i in range(memory.MEMORY_END + 1):
            if i == memory.USER_MEMORY_START:
                print("\nUser memory:")

            if i == memory.SHARED_MEMORY_START:
                print("\nShared memory:")

            if i == memory.SUPERVISOR_MEMORY_START:
                print("\nSupervisor memory:")

            formatted_block = self.get_block_str(memory, i)
            self.print_block(i, formatted_block)

    def print_vm_memory(self, ptr, memory):
        print("\nVM memory:")
        for i in range(memory.BLOCK_LENGTH):
            block_num = memory.memory[ptr][i]
            block_str = self.get_block_str(memory, block_num)
            self.print_block(i, block_str)


    def print_block(self, block_num, block_str):
        print(f"Block {block_num:04X}: {block_str}")


    def get_block_str(self, memory, block_num): 
        return " ".join(f"{word:04X}" if isinstance(word, int) else str(word) for word in memory.memory[block_num])
    

    def print_invalid_command(self):
        print("Invalid command.")


    def print_rm_exit(self):
        print("Exiting system. Thank you, come again!")