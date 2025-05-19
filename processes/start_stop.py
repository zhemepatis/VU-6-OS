from processes.process import *
from processes.print_line import *
from processes.read_from_interface import *
from processes.jcl import *
from processes.main_proc import *
from processes.interrupt import *
from resources.static.channel_device import *
from resources.static.shared_memory import *
from resources.static.supervisor_memory import *
from resources.static.user_memory import *
from enums.resource_names import *
from enums.process_states import *

class StartStopProcess(Process):
    def __init__(self, cpu, memory, pagination, channel_device, process_manager, resource_allocator):
        super().__init__(cpu, None, None, 1000)
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
            if ResourceNames.OS_PABAIGA not in self.resources and ResourceNames.OS_PABAIGA not in self.required_resources:
                self.required_resources.append(ResourceNames.OS_PABAIGA)
                self.process_manager.move_to_blocked_state(self)
                return
            
            if ResourceNames.OS_PABAIGA in self.resources:
                self.process_manager.move_to_ready_state(self)
                self.step = 4
                return

        if self.step == 4:
            self.step = 5 # TODO: is this okay?
            return

        if self.step == 5:
            return #  TODO: what to do with that?


    def initialise_system_resources(self):
        self.initialise_components()
        self.initialise_managers()

        self.resource_allocator.add_resource(ChannelDeviceResource())
        self.resource_allocator.add_resource(UserMemoryResource())
        self.resource_allocator.add_resource(SupervisorMemoryResource())
        self.resource_allocator.add_resource(SharedMemoryResource())


    def initialise_permanent_processes(self):
        self.process_manager.move_to_blocked_state(ReadFromInterfaceProcess(self, self.cpu, self.process_manager, self.resource_allocator))
        self.process_manager.move_to_blocked_state(JCLProcess(self, self.cpu))
        self.process_manager.move_to_blocked_state(MainProcProcess(self, self.cpu))
        self.process_manager.move_to_blocked_state(InterruptProcess(self, self.cpu))
        self.process_manager.move_to_blocked_state(PrintLineProcess(self, self.cpu))


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
