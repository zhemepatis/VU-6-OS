from components.memory import Memory
from components.channel_device import ChannelDevice
from components.pagination_mechanism import PaginationMechanism
from components.cpu import CPU
from real_machine import RealMachine

# creating real machine components
memory = Memory()
channel_device = ChannelDevice()
pagination_mechanism = PaginationMechanism()
cpu = CPU()

# creating real machine
real_machine = RealMachine(cpu)
real_machine.run()