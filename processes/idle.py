from processes.process import *
from enums.process_states import *

class IdleProcess(Process):
    def __init__(self, parent, cpu):
        super().__init__(cpu, ProcessStates.READY, parent, 0)
        # process specific
        self.step = 1

    def exec(self):
        if self.step == 1:
            self.step = 1
            return