class ResourceAllocator:
    def __init__(self, free_resources):
        # managers
        self.process_manager = None
        # resources
        self.free_resources = free_resources

    
    def allocate(self):
        pass

    
    def initialise_process_manager(self, process_manager):
        self.process_manager = process_manager


    def add_resource(self, resource):
        self.free_resources.append(resource)


    def remove_resource(self, resource):
        self.free_resources.remove(resource)