class Process:
    def __init__(self):
        self.id = None
        self.cpu_state = None
        self.resource_list = [] # TODO: do we need this here?
        self.state = None # TODO: do we need this here?
        self.parent = None # TODO: do we need this?
        self.children = None # TODO: do we need this?
        self.priority = None
