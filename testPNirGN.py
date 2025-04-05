from components.cpu import CPU
from devices.real_machine import RealMachine

cpu = CPU()
rm = RealMachine(cpu)

print("\n--- Creating VM ---")
rm.create_vm()

print("\n--- Adding test program to memory ---")
rm.memory[0][0] = "GN00"
rm.memory[0][1] = "PN00"
rm.memory[0][2] = "EXIT"

print("\n--- Testing GN and PN commands ---")
vm = rm.vm_list[0]  # Paimkite pirmą sukurtą VM
vm.channel_device.get_number(0, 0, rm.memory)  # GN komanda
vm.channel_device.put_number(0, 0, rm.memory)  # PN komanda
