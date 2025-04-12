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

    def run(self):
        run_vm = False

        while True:
            if not run_vm:
                choice = self.interface.main_menu()
                run_vm = self.handle_main_menu(choice)
                continue
            
            while run_vm:
                if self.cpu.get_operation_mode_flag() == 1:
                    choice = self.interface.step_by_step_menu()
                    self.handle_step_by_step_menu(choice)

                    if choice == 5:
                        run_vm = False

                    if choice != 1:
                        continue

                self.vm_list[0].exec()
                self.cpu.decrement_timer()

                if self.test_interrupt():
                    run_vm = self.exec_interrupt()

    # MAIN MENU
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
    
    # STEP-BY-STEP MENU
    def handle_step_by_step_menu(self, choice):
        if choice == 1:
            return
        
        if choice == 2:
            self.interface.print_cpu(self.cpu)
            return
        
        if choice == 3:
            self.interface.print_real_memory(self.memory)
            return
        
        if choice == 4:
            self.interface.print_vm_memory(self.cpu.ptr, self.memory)
            return
        
        if choice == 5:
            self.remove_vm()
            return
        
        self.interface.print_invalid_option()

    # INTERRUPTS
    def test_interrupt(self):
        return (self.cpu.pi + self.cpu.si) > 0 or self.cpu.ti == 0

    def exec_interrupt(self):
        if self.cpu.ti == 0:
            print("Timer interrupt triggered!")
            self.cpu.ti = 10

        if self.cpu.pi > 0:
            print(f"Program interrupt triggered: PI = {self.cpu.pi}")
            self.cpu.pi = 0
            return False

        if self.cpu.si > 0:
            print(f"Supervisor interrupt triggered: SI = {self.cpu.si}")
            result = self.handle_si_interrupt()
            self.cpu.si = 0
            return result
        
        return True

    def handle_si_interrupt(self):
        if self.cpu.si == 4:
            return False
        
        self.channel_device.exchange()
        return True
    
    # OTHERS
    def create_vm(self):
        ptr = self.memory.allocate();
        self.cpu.ptr = ptr

        vm = VirtualMachine(self.cpu)
        self.vm_list.append(vm)

    def remove_vm(self):
        self.interface.print_vm_exit()
        self.memory.deallocate()
        self.vm_list.pop(0)