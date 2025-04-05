from components.cpu import CPU
from devices.real_machine import RealMachine

cpu = CPU()
rm = RealMachine(cpu)

print("\n--- Creating VMs and testing memory allocation ---")
rm.create_vm()  # Create first VM
rm.create_vm()  # Create second VM
rm.create_vm()  # Create third VM
rm.create_vm()  # Create fourth VM

print("\n--- Testing address translation ---")
rm.test_pagination()  # Convert an address for the first VM
