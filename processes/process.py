from enums.process_states import *
from enums.resource_names import *
from components.cpu import *

class Process:
    # def __init__(self, cpu, process_manager, resource_allocator, state, parent, priority):
    def __init__(self, cpu, state, parent, priority):
        # components
        self.cpu = cpu
        # descriptors
        self.cpu_state = CPU()
        self.created_resources = []
        self.owned_resources = []
        self.state = state
        self.parent = parent
        self.children = []
        self.priority = priority


    def save_cpu_state(self):
        self.exchange_cpu_states(self.cpu_state, self.cpu)

    
    def load_cpu_state(self):
        self.exchange_cpu_states(self.cpu, self.cpu_state)


    def exchange_cpu_states(self, src_cpu_ref, dst_cpu_ref):
        dst_cpu_ref.ax = src_cpu_ref.ax
        dst_cpu_ref.bx = src_cpu_ref.bx
        dst_cpu_ref.ptr = src_cpu_ref.ptr
        dst_cpu_ref.sf = src_cpu_ref.sf
        # TODO: should there be more registers?