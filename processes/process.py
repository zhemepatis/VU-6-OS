from enums.process_states import *
from enums.resource_names import *
from components.cpu import *

class Process:
    # def __init__(self, cpu, process_manager, resource_allocator, state, parent, priority):
    def __init__(self, cpu, state, parent, priority):
        # components
        self.cpu = cpu
        # managers
        # self.process_manager = process_manager
        # self.resource_allocator = resource_allocator
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


    def request_resource_once(self, resource):
        print([self.resources, self.required_resources])
        # TODO: wont ever work because of types
        if resource not in [self.resources, self.required_resources]:
            self.required_resources.append(resource)
            self.process_manager.move_to_blocked_state(self)
            return


    def check_for_required_resources(self):
        resource_list = [resource.name for resource in self.resources]

        for name in self.required_resources:
            if name not in resource_list:
                self.mark_as_blocked()
                return
            
        self.mark_as_ready()