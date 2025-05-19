from enums.process_states import ProcessStates

class Process:
    def __init__(self):
        self.id = None
        self.cpu_state = None
        self.resources = []
        self.required_resources = []
        self.state = None
        self.parent = None
        self.children = None
        self.priority = None
        

    def check_for_required_resources(self):
        resource_list = [resource.name for resource in self.resources]

        for name in self.required_resources:
            if name not in resource_list:
                self.mark_as_blocked()
                return
            
        self.mark_as_ready()