from processes.process import Process
from enums.process_states import *

class PrintLineProcess(Process):
    def __init__(self, parent, cpu):
        super().__init__(cpu, None, parent, 10)
        # process specific
        self.step = 1

    def exec(self):
        pass