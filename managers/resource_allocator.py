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

    def create_resource(self, resource):
        pass

    def request_resource(self, resource):
        self.free_resources.append(resource)

    def destroy_resource(self, resource):
        pass

    def free_resource(self, resource):
        pass


    def remove_resource(self, resource):
        self.free_resources.remove(resource)


    def add_resource(self, resource):
        self.free_resources.append(resource)


    def remove_resource(self, resource):
        self.free_resources.remove(resource)