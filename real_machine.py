from virtual_machine import *
from managers.resource_allocator import *
from managers.proccess_manager import *
from components.memory import *
from components.channel_device import *
from components.pagination_mechanism import *
from components.cpu import *
from processes.start_stop import *

class RealMachine:
    def __init__(self):
        # components
        self.cpu = CPU()
        self.memory = Memory()
        self.pagination = PaginationMechanism()
        self.channel_device = ChannelDevice()
        # processes
        self.running = None
        self.ready = []
        self.blocked = []
        self.ready_stopped = []
        self.blocked_stopped = []
        # resources
        self.free_resources = []
        # managers
        self.resource_allocator = ResourceAllocator(self.free_resources)
        self.process_manager = ProcessManager(self.running, self.ready, self.blocked, self.ready_stopped, self.blocked_stopped)
        # initialisation
        self.process_manager.move_to_ready_state(StartStopProcess(self.cpu, self.memory, self.pagination, self.channel_device, self.process_manager, self.resource_allocator))


    def run(self):
        run_rm = True
        i  =  0
        while run_rm:
            self.running.exec()

            print(f'running: {self.running.__class__.__name__}')
            print(f'ready: {[process.__class__.__name__ for process in self.ready]}')
            print(f'blocked: {[process.__class__.__name__ for process in self.blocked]}')
            print()

            i += 1
            if i > 5:
                break


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
    # def handle_main_menu(self, choice):
    #     if choice == 1:
    #         return self.load_program()
        
    #     if choice == 2:
    #         self.change_mode()
    #         return False

    #     if choice == 3:
    #         self.interface.print_rm_exit()
    #         return False

    #     self.interface.print_invalid_option()

    # def load_program(self):
    #     self.create_vm()

    #     title = input("Enter program name: ")
    #     success = self.channel_device.load_program_to_supervisor_memory(title)
    #     if success:
    #         self.channel_device.load_program_to_user_memory()
    #         return True
        
    #     return False
    
    # # STEP-BY-STEP MENU
    # def handle_step_by_step_menu(self, choice):
    #     if choice == 1:
    #         return
        
    #     if choice == 2:
    #         self.interface.print_cpu(self.cpu)
    #         return
        
    #     if choice == 3:
    #         self.interface.print_real_memory(self.memory)
    #         return
        
    #     if choice == 4:
    #         self.interface.print_vm_memory(self.cpu.ptr, self.memory)
    #         return
        
    #     if choice == 5:
    #         self.remove_vm()
    #         return
        
    #     self.interface.print_invalid_option()

    # # INTERRUPTS
    # def test_interrupt(self):
    #     return (self.cpu.pi + self.cpu.si) > 0 or self.cpu.ti == 0

    # def exec_interrupt(self):
    #     if self.cpu.ti == 0:
    #         if self.cpu.get_operation_mode_flag() == 1:
    #             print("Timer interrupt triggered!")
    #         self.cpu.ti = 10

    #     if self.cpu.pi > 0:
    #         if self.cpu.get_operation_mode_flag() == 1:
    #             print(f"Program interrupt triggered: PI = {self.cpu.pi}")
    #         self.cpu.pi = 0
    #         return False

    #     if self.cpu.si > 0:
    #         if self.cpu.get_operation_mode_flag() == 1:
    #             print(f"Supervisor interrupt triggered: SI = {self.cpu.si}")
    #         result = self.handle_si_interrupt()
    #         self.cpu.si = 0
    #         return result
        
    #     return True

    # def handle_si_interrupt(self):
    #     if self.cpu.si == 4:
    #         return False
        
    #     if self.cpu.si == 5 or self.cpu.si == 6:
    #         self.cpu.put_semaphor_register()
        
    #     self.channel_device.exchange()
    #     self.cpu.raise_semaphor_register()
    #     return True
    
    # # OTHERS
    # def create_vm(self):
    #     ptr = self.memory.allocate()
    #     self.cpu.ptr = ptr

    #     self.cpu.set_ic_register(0, 0)

    #     vm = VirtualMachine(self.cpu)
    #     self.vm_list.append(vm)

    # def remove_vm(self):
    #     self.interface.print_vm_exit()
    #     self.memory.deallocate(self.cpu.ptr)
    #     self.vm_list.pop(0)