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

class StartStop(Process):
    def __init__(self, cpu, memory, pagination, channel_device, process_manager, resource_allocator):
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
            pass

        if self.step == 4:
            self.step = 5 # TODO: is this okay?
            return

        if self.step == 5:
            return #  TODO: what to do with that?


    def initialise_system_resources(self):
        # initialise commmunication between components
        self.cpu.initialise_channel_device(self.channel_device)
        self.cpu.initialise_pagination(self.pagination)
        self.cpu.initialise_memory(self.memory)

        self.pagination.initialise_cpu(self.cpu)
        self.pagination.initialise_memory(self.memory)

        self.channel_device.initialise_cpu(self.cpu)
        self.channel_device.initialise_memory(self.memory)

        # add resources
        self.resource_allocator.add_resource(CPU())
        self.resource_allocator.add_resource(ChannelDevice())
        self.resource_allocator.add_resource(UserMemory())
        self.resource_allocator.add_resource(SupervisorMemory())
        self.resource_allocator.add_resource(SharedMemory())


    def initialise_permanent_processes(self):
        self.process_manager()

        blocked_processes = [
            ReadFromInterface(),
            JCL(),
            MainProc(),
            Interrupt(),
            PrintLine(),
        ]

        self.free_resources.append(blocked_processes)



        