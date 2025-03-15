class VirtualMachineCPU:
    def __init__(self):
        # registers
        self.ax = 0
        self.bx = 0
        self.sf = 0
        self.ic = 0