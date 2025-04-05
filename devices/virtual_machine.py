from components.pagination_mechanism import PaginationMechanism

class VirtualMachine:
    def __init__(self, cpu, memory, ptr):
        self.cpu = cpu
        self.memory = memory
        self.ptr = ptr
        self.pagination = PaginationMechanism(ptr, memory)
        

    # runs command
    def exec(self):
        pass