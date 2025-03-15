from real_machine import RealMachine
from components.real_machine_cpu import RealMachineCPU

rm_cpu = RealMachineCPU()
rm = RealMachine(rm_cpu)

rm.run();