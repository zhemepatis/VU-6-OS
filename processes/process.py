from enums.process_states import ProcessStates

class Process:
    def __init__(self):
        self.id = None
        self.cpu_state = None
        self.resource_list = []
        self.required_resources = []
        self.state = None
        self.parent = None
        self.children = None
        self.priority = None


    def mark_as_blocked(self):
        if self.state == ProcessStates.READY_STOPPED or self.state == ProcessStates.BLOCKED_STOPPED:
            self.state = ProcessStates.BLOCKED_STOPPED
        else:
            self.state = ProcessStates.BLOCKED


    def mark_as_ready(self):
        if self.state == ProcessStates.READY_STOPPED or self.state == ProcessStates.BLOCKED_STOPPED:
            self.state = ProcessStates.READY_STOPPED
        else:
            self.state = ProcessStates.READY


    def mark_as_stopped(self):
        if self.state == ProcessStates.BLOCKED or self.state == ProcessStates.BLOCKED_STOPPED:
            self.state = ProcessStates.BLOCKED_STOPPED
        else:
            self.state = ProcessStates.READY_STOPPED


    def check_for_required_resources(self):
        resource_list = [resource.name for resource in self.resource_list]

        for name in self.required_resources:
            if name not in resource_list:
                self.mark_as_blocked()
                return
            
        self.mark_as_ready()