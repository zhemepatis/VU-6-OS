from processes.process import *
from enums.process_states import *

class InterruptProcess(Process):
    def __init__(self, parent, cpu):
        super().__init__(cpu, None, parent, 50)
        # process specific
        self.step = 1

    def exec(self):
        pass