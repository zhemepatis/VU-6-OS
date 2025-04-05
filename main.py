from devices.real_machine import RealMachine
from components.cpu import CPU
from devices.virtual_machine import VirtualMachine

cpu = CPU()
rm = RealMachine(cpu)

def main_menu():
    print("1. Run a program")
    print("2. Change operation mode")
    print("3. Exit")
    choice = input("Choose an option: ")
    return int(choice)

def step_by_step_menu(vm):
    while True:
        print("\nStep-by-step Menu:")
        print("1. Execute next command")
        print("2. Print CPU state")
        print("3. Print Memory state")
        print("4. Exit step-by-step mode")
        choice = input("Choose an option: ")

        if choice == "1":
            vm.exec()
        elif choice == "2":
            print(f"CPU state: AX={vm.cpu.ax}, BX={vm.cpu.bx}, IC={vm.cpu.ic}, TI={vm.cpu.ti}")
        elif choice == "3":
            print("Memory state:")
            for idx, block in enumerate(vm.memory[:10]):
                print(f"Block {idx}: {block}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again!")

while True:
    choice = main_menu()

    if choice == 1:
        print("\n--- Creating VM and testing memory allocation ---")
        rm.create_vm()

        vm = rm.vm_list[0]
        print("Select execution mode:")
        print("1. Run program automatically")
        print("2. Run program step-by-step")
        execution_mode = input("Choose an option: ")

        if execution_mode == "1":
            vm.exec()
        elif execution_mode == "2":
            step_by_step_menu(vm)

    elif choice == 2:
        current_mode = "Supervisor" if cpu.mode == 0 else "User"
        print(f"Current operation mode: {current_mode}")
        new_mode = input("Enter new mode (Supervisor/User): ")
        cpu.mode = 0 if new_mode.lower() == "supervisor" else 1

    elif choice == 3:
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again!")
        
#rm.run()