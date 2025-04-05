class PaginationMechanism:
    #inicializes ptr register value and real machine's memory
    def __init__(self, ptr_register, memory):
        self.ptr = ptr_register
        self.memory = memory #reference to the real machine memory

    # converts virtual memory address to real memory address
    def convert_address(self, virtual_block, word):
        real_block = self.memory[self.ptr][virtual_block]  #finds the block number using ptr
        return (real_block, word) #the word number remains unchanged 