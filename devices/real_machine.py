from devices.virtual_machine import VirtualMachine
from components.channel_device import ChannelDevice

class RealMachine:
    def __init__(self, cpu):
        self.user_memory_size = 0
        self.supervisor_memory_size = 0
        self.shared_memory_size = 0
        # 
        self.cpu = cpu
        self.channel_device = ChannelDevice()
        self.memory = [[0] * 16 for _ in range(86)] #full memory
        self.vm_list = [] 

    # creates virtual machine for program execution
    def create_vm(self):
        #Allocates memory for a new VM
        if len(self.vm_list)>=4:
            raise Exception ("Maximum number of VMs reached (4 VMs)")
        
        vm_count = len(self.vm_list)
        page_table_block = 51-(vm_count*17) #inicialize ptr value

        if page_table_block < 0:
            raise Exception("Not enough memory to allocate a new VM.")
        
        vm_start_block = page_table_block + 1
        for i in range(16):
            self.memory[page_table_block][i] = vm_start_block + i  

        new_vm = VirtualMachine(self.cpu, self.memory, page_table_block)
        self.vm_list.append(new_vm)

        print(f" VM {len(self.vm_list)} created with PTR = {page_table_block}")

    def test_pagination(self):
        """Test the address translation for each created VM."""
        for idx, vm in enumerate(self.vm_list):
            # Assume we're testing a virtual address (2, 5)
            real_addr = vm.pagination.convert_address(2, 5)
            print(f"VM {idx+1} (PTR = {vm.ptr}) -> Virtual(2,5) translates to real address: {real_addr}")
        # Optionally print the user memory blocks (0-67):
        print("User memory blocks state:")
        for i in range(68):
            print(f"Block {i}: {self.memory[i]}")

    # checks whether interrupt is required
    # if yes, handles it
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

    # runs virtual machines 
    # executes interrupts
    def run(self):
        while True:
            for vm in self.vm_list:
                vm.exec()
                self.cpu.decrement_timer()
                self.exec_interrupt()