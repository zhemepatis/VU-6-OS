# from devices.real_machine import RealMachine
# from components.cpu import CPU

# cpu = CPU()
# rm = RealMachine(cpu)

# rm.run()

from virtual_machine import VirtualMachine
from components.cpu import CPU

def print_cpu(cpu):
    print("General use register values.")
    print(f"AX: {hex(cpu.ax)}")
    print(f"BX: {hex(cpu.bx)}")

    print("Other register values.")
    print(f"PTR: {hex(cpu.ptr)}")
    print(f"SM: {hex(cpu.sm)}")
    print(f"MODE: {hex(cpu.mode)}")
    print(f"SF: {hex(cpu.sf)}")
    print(f"IC: {hex(cpu.ic)}")

    print("Interrupt values.")
    print(f"SI: {hex(cpu.si)}")
    print(f"PI: {hex(cpu.pi)}")
    print(f"TI: {hex(cpu.ti)}")

cpu = CPU()
vm = VirtualMachine(cpu, None, None, None)

vm.exec("ADD")

print_cpu(cpu)
