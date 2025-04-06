import random

class Memory:
    def __init__(self):
        # const
        self.USER_MEMORY_START = 0x00
        self.SHARED_MEMORY_START = 0x44 # 68 decimal
        self.SUPERVISOR_MEMORY_START = 0x46 # 70 decimal
        # block lists
        self.free_blocks = list(range(self.user_memory_start, self.shared_memory_start)) # blocks from 0 to 67 (or 0 to 43 in hex)
        random.shuffle(self.free_blocks)
        self.occupied_blocks = []
        # memory list
        self.memory = [[0] * 16 for _ in range(86)] # full memory - in decimal - 86 blocks with 16 words each