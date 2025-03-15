class RealMachine:
    def __init__(self, cpu):
        self.cpu = cpu
        self.vm_list = []

    # creates virtual machine for program execution
    def create_vm(self):
        pass

    # checks whether interrupt is required
    # if yes, handles it
    def exec_interrupt(self):
        pass

    # runs virtual machines 
    # executes interrupts
    def run(self):
        pass