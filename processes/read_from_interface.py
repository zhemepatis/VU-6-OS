from processes.process import *
from resources.dynamic.create_file import *
from resources.dynamic.exit_os import * 
from resources.dynamic.string_in_memory import * 
from enums.resource_names import * 

class ReadFromInterfaceProcess(Process):
    def __init__(self, parent, cpu, process_manager, resource_allocator):
        super().__init__(cpu, None, parent, 20)
        # components
        self.cpu = cpu
        # managers
        self.process_manager = process_manager
        self.resource_allocator = resource_allocator
        # process specific
        self.step = 1
        self.buffer = None


    def exec(self):
        if self.step == 1:
            self.resource_allocator.request_resource()
            self.step = 2
            return

        if self.step == 2:
            self.buffer = input()
            self.step = 3
            return

        if self.step == 3:
            result = self.parse_run()
            if result == None:
                self.step = 5
            else:
                self.buffer = result
                self.step = 4
            return

        if self.step == 4:
            resource = CreateFileResource(self.buffer)
            self.resource_allocator.add_resource(resource)
            self.step = 1
            return 

        if self.step == 5:
            success = self.parse_one_word("SWITCHMODE")
            self.step = 6 if success else 7
            return

        if self.step == 6:
            self.cpu.change_operation_mode_flag()
            self.step = 1
            return

        if self.step == 7:
            success = self.parse_one_word("EXIT")
            self.step = 8 if success else 9
            return

        if self.step == 8:
            resource = ExitOSResource()
            self.resource_allocator.add_resource(resource)
            self.step = 1
            return

        if self.step == 9:
            step_by_step_mode = self.cpu.get_operation_mode_flag() == 1
            self.step = 10 if step_by_step_mode else 16
            return

        if self.step == 10:
            success = self.parse_one_word("PRINTCPU")
            self.step = 11 if success else 12
            return

        if self.step == 11:
            self.print_cpu()
            self.step = 1
            return

        if self.step == 12:
            success = self.parse_one_word("PRINTVM")
            self.step = 13 if success else 14
            return

        if self.step == 13:
            self.print_vm_memory()
            self.step = 1
            return

        if self.step == 14:
            success = self.parse_one_word("PRINTRM")
            self.step = 15 if success else 16
            return

        if self.step == 15:
            self.print_vm_memory()
            self.step = 1
            return

        if self.step == 16:
            resource = StringInMemoryResource("Invalid command.")
            self.resource_allocator.add_resource(resource)
            self.step = 1
            return
        

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