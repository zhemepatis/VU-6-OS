from components.memory import Memory
from components.channel_device import ChannelDevice
from components.pagination_mechanism import PaginationMechanism
from components.cpu import CPU
from real_machine import RealMachine

# creating components
memory = Memory()
pagination = PaginationMechanism()
channel_device = ChannelDevice()
cpu = CPU()

# initialising commmunication between components
cpu.initialise_channel_device(channel_device)
cpu.initialise_pagination(pagination)

pagination.initialise_cpu(cpu)

channel_device.initialise_cpu(cpu)
channel_device.initialise_pagination(pagination)

# creating real machine
real_machine = RealMachine(cpu, memory, pagination, channel_device)
real_machine.run()