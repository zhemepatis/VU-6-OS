from components.cpu import CPU
from devices.real_machine import RealMachine

# Initialize CPU and RealMachine
cpu = CPU()
rm = RealMachine(cpu)

# Creating a VM
print("\n--- Creating VM ---")
rm.create_vm()

# Adding a test program to the VM memory
print("\n--- Adding test program to memory ---")
rm.memory[0][0] = "GN00"  # GN command: Input from user
rm.memory[0][1] = "PN00"  # PN command: Output to screen
rm.memory[0][2] = "EXIT"  # EXIT command

# Testing Timer Mechanism
print("\n--- Testing Timer Mechanism ---")
cpu = rm.cpu
cpu.decrement_timer("general")  # General operation timer decrement
print(f"Timer after general operation: {cpu.ti}")
cpu.decrement_timer("io")  # I/O operation timer decrement
print(f"Timer after IO operation: {cpu.ti}")

# Testing Interrupt Handling
print("\n--- Testing Interrupts ---")
cpu.ti = 0  # Simulate timer interrupt
rm.exec_interrupt()  # Handle timer interrupt

cpu.pi = 2  # Simulate program interrupt (invalid operation code)
rm.exec_interrupt()

cpu.si = 1  # Simulate supervisory interrupt (GN command)
rm.exec_interrupt()

# Testing Channel Device functionality for GN and PN commands
print("\n--- Testing GN and PN commands ---")
vm = rm.vm_list[0]  # Get the first created VM
vm.channel_device.get_number(0, 0, rm.memory)  # GN command: Input to memory
vm.channel_device.put_number(0, 0, rm.memory)  # PN command: Output from memory
