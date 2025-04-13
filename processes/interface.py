class Interface:
    # MENU
    def print_menu_list(self, title, list):
        length = len(list)

        if title != None:
            print(f"\n{title} menu:")

        for idx in range(length):
            print(f"{idx+1}. {list[idx]}")

    def get_menu_choice(self):
        choice = input("Choose an option: ")
        try:
            choice = int(choice)
        except: 
            return -1
        
        return choice
    
    def main_menu(self):
        title = "Main"
        menu = [
            "Run a program",
            "Change operation mode",
            "Exit"
        ]

        self.print_menu_list(title, menu)
        return self.get_menu_choice()
    
    def step_by_step_menu(self):
        title = "Step-by-step"
        menu = [
            "Execute next command",
            "Print CPU state",
            "Print RM memory state",
            "Print VM memory state",
            "Exit step-by-step mode"
        ]

        self.print_menu_list(title, menu)
        return self.get_menu_choice()
    
    # OTHER PRINTING
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

    def print_invalid_option(self):
        print("Invalid choice. Try again!")

    def print_vm_exit(self):
        print("Exiting VM.")

    def print_rm_exit(self):
        print("Exiting system. Thank you, come again!")