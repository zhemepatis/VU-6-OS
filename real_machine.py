from virtual_machine import VirtualMachine
from processes.interface import Interface

class RealMachine:
    def __init__(self, cpu, memory, pagination, channel_device):
        # components
        self.cpu = cpu
        self.memory = memory
        self.pagination = pagination
        self.channel_device = channel_device
        # other
        self.interface = Interface()
        self.vm_list = []

    def create_vm(self):
        ptr = self.memory.allocate()
        self.cpu.ptr = ptr

        vm = VirtualMachine(self.cpu)
        self.vm_list.append(vm)

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

    def exec_interrupt(self):
        if self.cpu.ti == 0:
            print("Timer interrupt triggered!")
            self.cpu.ti = 10
        if self.cpu.pi > 0:
            print(f"Program interrupt triggered: PI = {self.cpu.pi}")
            self.cpu.pi = 0
        if self.cpu.si > 0:
            print(f"Supervisor interrupt triggered: SI = {self.cpu.si}")
            self.cpu.si = 0
    
    def test_interrupt(self):
        pass

    def run(self):
        run_vm = False

        while True:
            if not run_vm:
                choice = self.interface.main_menu()
                run_vm = self.handle_main_menu(choice)
                continue
            
            while run_vm:
                next_cmd = True
                if self.cpu.get_operation_mode_flag == 1:
                    choice = self.interface.step_by_step_menu()
                    next_cmd = self.handle_step_by_step_menu(choice)

                    if not next_cmd:
                        continue

                if next_cmd:
                    self.vm_list[0].exec()
                    self.exec_interrupt()

    def handle_main_menu(self, choice):
        if choice == 1:
            self.load_program()
            return True
        
        if choice == 2:
            self.change_mode()
            return False

        if choice == 3:
            self.exit()
            return False
        
        self.interface.print_invalid_option()
        return False

    def load_program(self):
        title = input("Enter program name: ")
        self.channel_device.load_program_to_supervisor_memory(title)
        self.channel_device.validate_supervisor_memory()
        self.channel_device.load_program_to_user_memory()
        self.create_vm()

    def change_mode(self):
        self.cpu.change_operation_mode_flag()

    def exit(self):
        print("Exiting system. Thank you, come again!")
        exit(0)
        
    def handle_step_by_step_menu(self, choice):
        if choice == 1:
            return True
        
        if choice == 2:
            self.interface.print_cpu()
            return False
        
        if choice == 3:
            self.interface.print_real_memory(self.memory)
            return False
        
        if choice == 4:
            self.interface.print_vm_memory(self.memory)
            return False
        
        if choice == 5:
            return False
        
        self.interface.print_invalid_option()