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

    
    def initialise_resource_allocator(self, resource_allocator):
        self.resource_allocator = resource_allocator

    
    def prioritise(self):
        self.ready.sort(key = lambda process: process.priority)


    def move_to_running_state(self, process):    
        if process.state == None:
            process.state = ProcessStates.RUNNING
            self.running.append(process)
            return


        if process.state == ProcessStates.READY:
            self.ready.remove(process)
            process.state = ProcessStates.RUNNING
            self.running.append(process)
            return


    def move_to_ready_state(self, process):
        if process.state == None:
            process.state = ProcessStates.READY
            self.ready.append(process)
            return

        if process.state == ProcessStates.RUNNING:
            self.running.remove(process)
            process.state = ProcessStates.READY
            self.ready.append(process)
            return

        if process.state == ProcessStates.BLOCKED:
            self.blocked.remove(process)
            process.state = ProcessStates.READY
            self.ready.append(process)
            return
        
        if process.state == ProcessStates.READY_STOPPED:
            self.ready_stopped.remove(process)
            process.state = ProcessStates.READY
            self.ready.append(process)
            return


    def move_to_blocked_state(self, process):     
        if process.state == None:
            process.state = ProcessStates.BLOCKED
            self.blocked.append(process)
            return

        if process.state == ProcessStates.RUNNING:
            self.running.remove(process)
            process.state = ProcessStates.BLOCKED
            self.blocked.append(process)
            return

        if process.state == ProcessStates.BLOCKED_STOPPED:
            self.blocked_stopped.remove(process)
            process.state = ProcessStates.BLOCKED
            self.blocked.append(process)
            return


    def move_to_stopped_state(self, process):
        if process.state == ProcessStates.READY:
            self.ready.remove(process)
            process.state = ProcessStates.READY_STOPPED
            self.ready_stopped.append(process)
            return
        
        if process.state == ProcessStates.BLOCKED:
            self.blocked.remove(process)
            process.state = ProcessStates.BLOCKED_STOPPED
            self.ready.append(process)
            return
    

    def destroy_process(self, process):
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

