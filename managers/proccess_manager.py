from enums.process_states import *

class ProcessManager:
    def __init__(self, running, ready, blocked, ready_stopped, blocked_stopped):
        # processes
        self.running = running
        self.ready = ready
        self.blocked = blocked
        self.ready_stopped = ready_stopped 
        self.blocked_stopped = blocked_stopped
        # managers
        self.resource_allocator = None


     # INITIALISATION

    def initialise_resource_allocator(self, resource_allocator):
        self.resource_allocator = resource_allocator


    # PRIMITIVES
    
    def get_next_process(self):
        next_process = self.ready[0]
        self.ready.remove(next_process)
        self.running.append(next_process)


    def create_process(self, process):
        if process.state == ProcessStates.RUNNING:
            self.running.append(process)
            return

        if process.state == ProcessStates.READY:
            idx = 0
            for item in self.ready:
                if item.priority > process.priority:
                    self.ready.insert(idx, process)
                    return
                idx += 1

            self.ready.append(process)
        
        if process.state == ProcessStates.BLOCKED:
            self.blocked.append(process)
            return
        
        if process.state == ProcessStates.READY_STOPPED:
            self.ready_stopped.append(process)
            return
        
        if process.state == ProcessStates.BLOCKED_STOPPED:
            self.blocked_stopped.append(process)
            return


    def destroy_process(self, process):
        # destroy all of created resources
        for resource in process.created_resources:
            self.resource_allocator.destroy(resource)

        # destroy all of created processes
        for child in process.children:
            self.destroy_process(child)
            self.children.remove(child)

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

