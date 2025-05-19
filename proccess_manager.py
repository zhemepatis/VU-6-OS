from enums.process_states import *

class ProcessManager:
    def __init__(self, running, ready, blocked, ready_stopped, blocked_stopped, free_resources):
        # processes
        self.running = running
        self.ready = ready
        self.blocked = blocked
        self.ready_stopped = ready_stopped 
        self.blocked_stopped = blocked_stopped
        # resources
        self.free_resources = free_resources


    def move_to_ready_state(self, process):
        if process.state == None:
            process.state = ProcessStates.READY
            self.ready.append(process)
            return

        if process.state == ProcessStates.BLOCKED:
            self.blocked.remove(process)
            process.state = ProcessStates.READY
            self.ready.append(process)
            return
        
        if process.state == ProcessStates.BLOCKED_STOPPED_STOPPED:
            self.blocked_stopped.remove(process)
            process.state = ProcessStates.READY_STOPPED
            self.ready_stopped.append(process)
            return


    def move_to_blocked_state(self, process):
        if process.state == None:
            process.state = ProcessStates.BLOCKED
            self.blocked.append(process)
            return

        if process.state == ProcessStates.READY:
            self.ready.remove(process)
            process.state = ProcessStates.BLOCKED
            self.blocked.append(process)
            return
        
        if process.state == ProcessStates.READY_STOPPED:
            self.ready_stopped.remove(process)
            process.state = ProcessStates.BLOCKED_STOPPED
            self.blocked_stopped.append(process)
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

