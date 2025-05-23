from enums.process_states import *
from components.cpu import *

class Process:
    def __init__(self, cpu, state, parent, priority):
        self.cpu = cpu
        # descriptors
        self.cpu_state = CPU()
        self.resources = []
        self.required_resources = []
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


    def check_for_required_resources(self):
        resource_list = [resource.name for resource in self.resources]

        for name in self.required_resources:
            if name not in resource_list:
                self.mark_as_blocked()
                return
            
        self.mark_as_ready()