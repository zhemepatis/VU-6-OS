from virtual_machine import VirtualMachine
from utils.interface import Interface

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
        ptr = self.memory.allocate();
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
        while True:
            self.interface.main_menu()

            # if choice == 1:
            #     print("\n--- Creating VM and testing memory allocation ---")
            #     rm.create_vm()

            #     vm = rm.vm_list[0]
            #     print("Select execution mode:")
            #     print("1. Run program automatically")
            #     print("2. Run program step-by-step")
            #     execution_mode = input("Choose an option: ")

            #     if execution_mode == "1":
            #         vm.exec()
            #     elif execution_mode == "2":
            #         step_by_step_menu(vm)

            # elif choice == 2:
            #     current_mode = "Supervisor" if cpu.mode == 0 else "User"
            #     print(f"Current operation mode: {current_mode}")
            #     new_mode = input("Enter new mode (Supervisor/User): ")
            #     cpu.mode = 0 if new_mode.lower() == "supervisor" else 1

            # elif choice == 3:
            #     print("Exiting system. Goodbye!")
            #     break

            # else:
            #     print("Invalid choice. Try again!")

    def handle_main_menu(self, choice):
        if choice == 1:
            return
        
        if choice == 2:
            return
        
        if choice == 3:
            return
        
    def handle_step_by_step_menu(self, choice):
        if choice == 1:
            return
        
        if choice == 2:
            return
        
        if choice == 3:
            return
        
        if choice == 4:
            return
        
        if choice == 5:
            return