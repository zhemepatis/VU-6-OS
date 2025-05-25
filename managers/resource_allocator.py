from enums.resource_types import *
from enums.process_states import *

class ResourceAllocator:
    def __init__(self, running, ready, blocked, ready_stopped, blocked_stopped, free_resources):
        # managers
        self.process_manager = None
        # lists
        self.running = running
        self.ready = ready
        self.blocked = blocked
        self.ready_stopped = ready_stopped 
        self.blocked_stopped = blocked_stopped
        # resources
        self.free_resources = free_resources


    # INITIALISATION

    def initialise_process_manager(self, process_manager):
        self.process_manager = process_manager


    # PRIMITIVES
    
    def create_resource(self, resource):
        self.free_resources.append(resource)


    def free_resource(self, resource):
        if resource.type == ResourceTypes.DYNAMIC:
            return

        if resource.type == ResourceTypes.STATIC:
            self.free_resources.append(resource)

    
    def destroy_resource(self, resource):
        self.free_resources.remove(resource)


    def request_resource(self, process, resource_name):
        for item in self.free_resources:
            if item.name == resource_name:
                self.free_resources.remove(item)
                process.owned_resources.append(item)
                self.move_to_ready_state(process)
                return
            
        self.move_to_blocked_state(process)


    def move_to_running_state(self, process):
        self.ready.remove(process)

        process.state = ProcessStates.RUNNING
        self.running.append(process)


    def move_to_ready_state(self, process):
        self.remove_from_current_list(process)

        process.state = ProcessStates.READY
        for i in range(self.ready.len()):
            if self.ready[i].priority > process.priority:
                self.ready.insert(i, process)
                return


    def move_to_blocked_state(self, process):
        self.remove_from_current_list(process)
        
        process.state = ProcessStates.BLOCKED
        self.blocked.append(process)


    def move_to_stopped_state(self, process):
        self.remove_from_current_list(process)

        if process.state == ProcessStates.READY:
            process.state = ProcessStates.READY_STOPPED
            self.ready_stopped.append(process)
            return
        
        if process.state == ProcessStates.BLOCKED:
            process.state = ProcessStates.BLOCKED_STOPPED
            self.blocked_stopped.append(process)
            return


    def remove_from_current_list(self, process):
        if process.state == ProcessStates.RUNNING:
            self.running.remove(process)
            return
        
        if process.state == ProcessStates.READY:
            self.ready.remove(process)
            return
        
        if process.state == ProcessStates.BLOCKED:
            self.blocked.remove(process)
            return
        
        if process.state == ProcessStates.READY_STOPPED:
            self.ready_stopped.remove(process)
            return
        
        if process.state == ProcessStates.BLOCKED_STOPPED:
            self.blocked_stopped.remove(process)
            return