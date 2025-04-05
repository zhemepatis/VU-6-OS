from devices.virtual_machine import VirtualMachine
import random

class RealMachine:
    def __init__(self, cpu):
        self.user_memory_start = 0x00
        self.shared_memory_start = 0x44 #68 decimal
        self.supervisor_memory_start = 0x46 #70 decimal
        
        self.cpu = cpu
        self.memory = [[0] * 16 for _ in range(86)] #full memory - in decimal - 86 blocks with 16 words each
        self.vm_list = [] 

        #inicialize free and occupied user blocks

        self.free_blocks = list(range(self.user_memory_start, self.shared_memory_start)) #blocks from 0 to 67 (or 0 to 43 in hex)
        random.shuffle(self.free_blocks)
        self.occupied_blocks = []

    # creates virtual machine for program execution
    def create_vm(self):
        #Allocates memory for a new VM
        required_blocks = 0x11 #17 decimal
        if len(self.free_blocks)<required_blocks:
            raise Exception ("Not enough memory to create a new VM")
        
        allocated_blocks = [self.free_blocks.pop() for _ in range(required_blocks)] #pop 17 blocks from free blocks list
        self.occupied_blocks.extend(allocated_blocks) #add these blocks to the occupied list

        page_table_block = allocated_blocks[0]
        vm_data_blocks = allocated_blocks[1:]
        
        for i in range(16):
            self.memory[page_table_block][i] = vm_data_blocks[i]  

        new_vm = VirtualMachine(self.cpu, self.memory, page_table_block)
        self.vm_list.append(new_vm)

        print(f" VM {len(self.vm_list)} created with PTR = {page_table_block:02X}")

    def test_pagination(self):
        """Test the address translation for each created VM."""
        for idx, vm in enumerate(self.vm_list):
            # Assume we're testing a virtual address (2, 5)
            real_addr = vm.pagination.convert_address(2, 5)
            print(f"VM {idx+1} (PTR = {vm.ptr:02X}) -> Virtual(2,5) translates to real address: Block {real_addr[0]:02X}, Word {real_addr[1]:02X}")
        # Optionally print the user memory blocks (0-67):
        print("User memory blocks state:")
        for i in range(self.shared_memory_start):
            formatted_block = " ".join(f"{word:02X}" for word in self.memory[i])
            print(f"Block {i:02X}: {formatted_block}")

    # checks whether interrupt is required
    # if yes, handles it
    def exec_interrupt(self):
        # cpu.ti += 1
        # if cpu.ti == 10:
        #     cpu.ti = 0
        pass

    def test_interrupt(self):
        pass

    # runs virtual machines 
    # executes interrupts
    def run(self):
        # while ...:
        #     vm = create_vm();
        #     vm.exec(cpu, );
        for vm in self.vm_list:
            vm.exec()