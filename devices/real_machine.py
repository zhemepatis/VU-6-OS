class RealMachine:
    def __init__(self, cpu):
        self.user_memory_size = 0
        self.supervisor_memory_size = 0
        self.shared_memory_size = 0
        # 
        self.cpu = cpu
        self.memory = [] # matrix mb? https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg
        self.vm_list = [] 

    # creates virtual machine for program execution
    def create_vm(self):
        pass

    # checks whether interrupt is required
    # if yes, handles it
    def exec_interrupt(self):
        # cpu.ti += 1
        # if cpu.ti == 10:
        #     cpu.ti = 0
        pass

    def test_interrupt(self):
        pass

    # runs virtual machines 
    # executes interrupts
    def run(self):
        # while ...:
        #     vm = create_vm();
        #     vm.exec(cpu, );
        pass