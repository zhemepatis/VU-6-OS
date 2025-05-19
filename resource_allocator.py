class ResourceAllocator:
    def __init__(self, running, ready, blocked, ready_stopped, blocked_stopped, free_resources):
        # processes
        self.running = running
        self.ready = ready
        self.blocked = blocked
        self.ready_stopped = ready_stopped 
        self.blocked_stopped = blocked_stopped
        # resources
        self.free_resources = free_resources


    def add_resource(self, resource):
        self.free_resources.append(resource)


    def remove_resource(self, resource):
        self.free_resources.remove(resource)