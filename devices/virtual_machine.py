from components.pagination_mechanism import PaginationMechanism

class VirtualMachine:
    def __init__(self, cpu, memory, ptr):
        self.cpu = cpu
        self.memory = memory
        self.pagination = PaginationMechanism(ptr, memory)
        self.ptr = ptr

    # runs command
    def exec(self):
        pass