from processes.process import *
from processes.print_line import *
from processes.read_from_interface import *
from processes.jcl import *
from processes.main_proc import *
from processes.interrupt import *
from resources.static.cpu import *
from resources.static.channel_device import *
from resources.static.shared_memory import *
from resources.static.supervisor_memory import *
from resources.static.user_memory import *
from enums.resource_names import *

class StartStopProcess(Process):
    def __init__(self, cpu, memory, pagination, channel_device, process_manager, resource_allocator):
        super().__init__()
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
            self.required_resources = [ResourceNames.OS_PABAIGA]
            pass

        if self.step == 4:
            self.step = 5 # TODO: is this okay?
            return

        if self.step == 5:
            return #  TODO: what to do with that?


    def initialise_system_resources(self):
        self.resource_allocator.add_resource(CPUResource())
        self.resource_allocator.add_resource(ChannelDeviceResource())
        self.resource_allocator.add_resource(UserMemoryResource())
        self.resource_allocator.add_resource(SupervisorMemoryResource())
        self.resource_allocator.add_resource(SharedMemoryResource())


    def initialise_permanent_processes(self):
        self.process_manager.move_to_blocked_state(ReadFromInterfaceProcess())
        self.process_manager.move_to_blocked_state(JCLProcess())
        self.process_manager.move_to_blocked_state(MainProcProcess())
        self.process_manager.move_to_blocked_state(InterruptProcess())
        self.process_manager.move_to_blocked_state(PrintLineProcess())        