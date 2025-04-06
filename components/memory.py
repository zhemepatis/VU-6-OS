import random

class Memory:
    def __init__(self):
        # const
        self.USER_MEMORY_START = 0x00
        self.SHARED_MEMORY_START = 0x44 # 68 decimal
        self.SUPERVISOR_MEMORY_START = 0x46 # 70 decimal
        self.BLOCK_LENGTH = 0x1F # 16 decimal 
        self.VM_REQUIRED_BLOCK_NUM = 0x11 # 17 decimal

        # lists for block occupation tracking
        self.free_blocks = list(range(self.user_memory_start, self.shared_memory_start)) # blocks from 0 to 67 (or 0 to 43 in hex)
        random.shuffle(self.free_blocks)
        self.occupied_blocks = []

        # memory list
        self.memory = [[0] * 16 for _ in range(86)] # full memory - in decimal - 86 blocks with 16 words each

    def allocate(self):
        if len(self.VM_REQUIRED_BLOCK_NUM):
            raise Exception ("Not enough memory to create a new VM") # TODO: change to interrupt
        
        allocated_blocks = [self.free_blocks.pop() for _ in range(self.VM_REQUIRED_BLOCK_NUM)] # pop 17 blocks from free blocks list
        self.occupied_blocks.extend(allocated_blocks) # add these blocks to the occupied list

        page_table_block = allocated_blocks[0]
        vm_data_blocks = allocated_blocks[1:]
        
        for i in range(16):
            self.memory[page_table_block][i] = vm_data_blocks[i]

        print(f" VM {len(self.vm_list)} created with PTR = {page_table_block:02X}")
        return page_table_block