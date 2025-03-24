from devices.real_machine import RealMachine
from components.cpu import CPU

cpu = CPU()
rm = RealMachine(cpu)

rm.run();