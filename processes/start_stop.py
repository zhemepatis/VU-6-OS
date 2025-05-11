from components.memory import Memory
from components.channel_device import ChannelDevice
from components.pagination_mechanism import PaginationMechanism
from components.cpu import CPU

class StartStop:
    def __init__(self):
        # components
        self.memory = None
        self.pagination = None
        self.channel_device = None
        self.cpu = None
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
        # initialise resources
        self.memory = Memory() # TODO: figure how to pass them to RM
        self.pagination = PaginationMechanism()
        self.channel_device = ChannelDevice()
        self.cpu = CPU()

        # initialise commmunication between components
        self.cpu.initialise_channel_device(self.channel_device)
        self.cpu.initialise_pagination(self.pagination)
        self.cpu.initialise_memory(self.memory)

        self.pagination.initialise_cpu(self.cpu)
        self.pagination.initialise_memory(self.memory)

        self.channel_device.initialise_cpu(self.cpu)
        self.channel_device.initialise_memory(self.memory)


    def initialise_permanent_processes(self):
        pass