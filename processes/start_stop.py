from processes.process import *
from processes.print_line import *
from processes.read_from_interface import *
from processes.jcl import *
from processes.main_proc import *
from processes.interrupt import *
from processes.idle import *
from resources.static.channel_device import *
from resources.static.shared_memory import *
from resources.static.supervisor_memory import *
from resources.static.user_memory import *
from enums.resource_names import *
from enums.process_states import *

class StartStopProcess(Process):
    def __init__(self, cpu, memory, pagination, channel_device, process_manager, resource_allocator):
        super().__init__(cpu, ProcessStates.RUNNING, None, 1000)
        # components
        self.cpu = cpu
        self.memory = memory
        self.pagination = pagination
        self.channel_device = channel_device
        # managers 
        self.process_manager = process_manager
        self.resource_allocator = resource_allocator
        # process specific
        self.step = 1


    def exec(self):
        if self.step == 1:
            self.initialise_system_resources()
            self.step = 2
            return

        if self.step == 2:
            self.initialise_permanent_processes()
            self.step = 3
            return

        if self.step == 3:
            self.resource_allocator.request_resource(self, ResourceNames.OS_PABAIGA)

            if self.state == ProcessStates.READY:
                self.step = 4
            
            return

        if self.step == 4:
            self.destroy_permanent_processes()
            self.step = 5
            return

        if self.step == 5:
            self.destroy_system_resources()
            return


    # INITIALISATION

    def initialise_system_resources(self):
        self.initialise_components()
        self.initialise_managers()

        resource = ChannelDeviceResource()
        self.resource_allocator.create_resource(resource)
        self.created_resources.append(resource)

        resource = UserMemoryResource()
        self.resource_allocator.create_resource(resource)
        self.created_resources.append(resource)

        resource = ChannelDeviceResource()
        self.resource_allocator.create_resource(resource)
        self.created_resources.append(resource)

        resource = SupervisorMemoryResource()
        self.resource_allocator.create_resource(resource)
        self.created_resources.append(resource)

        resource = SharedMemoryResource()
        self.resource_allocator.create_resource(resource)
        self.created_resources.append(resource)


    def initialise_permanent_processes(self):
        process = ReadFromInterfaceProcess(self, self.cpu, self.process_manager, self.resource_allocator)
        self.children.append(process)
        self.process_manager.create_process(process)

        process = JCLProcess(self, self.cpu)
        self.children.append(process)
        self.process_manager.create_process(process)

        process = MainProcProcess(self, self.cpu)
        self.children.append(process)
        self.process_manager.create_process(process)

        process = InterruptProcess(self, self.cpu)
        self.children.append(process)
        self.process_manager.create_process(process)

        process = PrintLineProcess(self, self.cpu)
        self.children.append(process)
        self.process_manager.create_process(process)

        process = IdleProcess(self, self.cpu)
        self.children.append(process)
        self.process_manager.create_process(process)


    def initialise_components(self):
        self.cpu.initialise_channel_device(self.channel_device)
        self.cpu.initialise_pagination(self.pagination)
        self.cpu.initialise_memory(self.memory)

        self.pagination.initialise_cpu(self.cpu)
        self.pagination.initialise_memory(self.memory)

        self.channel_device.initialise_cpu(self.cpu)
        self.channel_device.initialise_memory(self.memory)

    
    def initialise_managers(self):
        self.process_manager.initialise_resource_allocator(self.resource_allocator)
        self.resource_allocator.initialise_process_manager(self.process_manager)


    # DESTRUCTION

    def destroy_permanent_processes(self):
        self.process_manager.destroy_process(self)

    
    def destroy_system_resources(self):
        for item in self.resource_allocator.free_resources:
            self.resource_allocator.destroy_resource(item)