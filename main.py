# from devices.real_machine import RealMachine
# from components.cpu import CPU

# cpu = CPU()
# rm = RealMachine(cpu)

# rm.run()



hexs = 0xFFFF0000
sf = hexs >> 16
print(hex(sf))
print(hex(sf ^ 0xFFFF))