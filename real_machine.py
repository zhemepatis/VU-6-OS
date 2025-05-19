from virtual_machine import VirtualMachine
from processes.start_stop import *

class RealMachine:
    def __init__(self):
        # components
        self.cpu = None
        self.memory = None
        self.pagination = None
        self.channel_device = None
        # other
        self.running = None
        self.blocked = []
        self.ready = []
        self.ready_stopped = []
        self.blocked_stopped = []

    def run(self):



    # def run(self):
    #     run_vm = False
    #     run_rm = True
        
    #     while run_rm:
    #         if not run_vm:
    #             choice = self.interface.main_menu()
    #             success = self.handle_main_menu(choice)

    #             if choice == 1 and success:
    #                 run_vm = True
                
    #             if choice == 3:
    #                 run_rm = False    
            
    #         while run_vm:
    #             operation_mode = self.cpu.get_operation_mode_flag()
    #             if operation_mode == 1:
    #                 choice = self.interface.step_by_step_menu()
    #                 self.handle_step_by_step_menu(choice)

    #                 if choice == 5:
    #                     run_vm = False

    #                 if choice != 1:
    #                     continue

    #             self.vm_list[0].exec()

    #             io_operation = self.cpu.si != 0 and self.cpu.si != 4
    #             self.cpu.decrement_timer(io_operation)

    #             if self.test_interrupt():
    #                 run_vm = self.exec_interrupt()

    # MAIN MENU
    def handle_main_menu(self, choice):
        if choice == 1:
            return self.load_program()
        
        if choice == 2:
            self.change_mode()
            return False

        if choice == 3:
            self.interface.print_rm_exit()
            return False

        self.interface.print_invalid_option()

    def load_program(self):
        self.create_vm()

        title = input("Enter program name: ")
        success = self.channel_device.load_program_to_supervisor_memory(title)
        if success:
            self.channel_device.load_program_to_user_memory()
            return True
        
        return False

    def change_mode(self):
        self.cpu.change_operation_mode_flag()
    
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
            if self.cpu.get_operation_mode_flag() == 1:
                print("Timer interrupt triggered!")
            self.cpu.ti = 10

        if self.cpu.pi > 0:
            if self.cpu.get_operation_mode_flag() == 1:
                print(f"Program interrupt triggered: PI = {self.cpu.pi}")
            self.cpu.pi = 0
            return False

        if self.cpu.si > 0:
            if self.cpu.get_operation_mode_flag() == 1:
                print(f"Supervisor interrupt triggered: SI = {self.cpu.si}")
            result = self.handle_si_interrupt()
            self.cpu.si = 0
            return result
        
        return True

    def handle_si_interrupt(self):
        if self.cpu.si == 4:
            return False
        
        if self.cpu.si == 5 or self.cpu.si == 6:
            self.cpu.put_semaphor_register()
        
        self.channel_device.exchange()
        self.cpu.raise_semaphor_register()
        return True
    
    # OTHERS
    def create_vm(self):
        ptr = self.memory.allocate()
        self.cpu.ptr = ptr

        self.cpu.set_ic_register(0, 0)

        vm = VirtualMachine(self.cpu)
        self.vm_list.append(vm)

    def remove_vm(self):
        self.interface.print_vm_exit()
        self.memory.deallocate(self.cpu.ptr)
        self.vm_list.pop(0)