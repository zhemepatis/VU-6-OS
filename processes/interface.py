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
        title = "Main"
        menu = [
            "Execute next command",
            "Print CPU state",
            "Print VM memory state",
            "Print RM memory state",
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
        pass

    def print_vm_memory(self, memory):
        pass

    def print_invalid_option(self):
        print("Invalid choice. Try again!")

    def print_vm_exit(self):
        print("Exiting VM.")



# def test_pagination(self):
#     """Test the address translation for each created VM."""
#     for idx, vm in enumerate(self.vm_list):
#         # Assume we're testing a virtual address (2, 5)
#         real_addr = vm.pagination.convert_address(2, 5)
#         print(f"VM {idx+1} (PTR = {vm.ptr:02X}) -> Virtual(2,5) translates to real address: Block {real_addr[0]:02X}, Word {real_addr[1]:02X}")
#     # Optionally print the user memory blocks (0-67):
#     print("User memory blocks state:")
#     for i in range(self.shared_memory_start):
#         formatted_block = " ".join(f"{word:02X}" for word in self.memory[i])
#         print(f"Block {i:02X}: {formatted_block}")