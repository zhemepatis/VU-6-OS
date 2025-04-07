class PaginationMechanism:
    #inicializes ptr register value and real machine's memory
    def __init__(self):
        self.cpu = None
        self.memory = None # reference to the real machine memory

    def initialise_cpu(self, cpu):
        self.cpu = cpu

    def initialise_memory(self, memory):
        self.memory = memory

    # converts virtual memory address to real memory address
    def convert_address(self, virtual_block, word):
        real_block = self.memory[self.cpu.ptr][virtual_block]  #finds the block number using ptr
        return (real_block, word) #the word number remains unchanged 