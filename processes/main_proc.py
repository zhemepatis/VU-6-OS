from processes.process import *
from enums.process_states import *

class MainProcProcess(Process):
    def __init__(self, parent, cpu):
        super().__init__(cpu, ProcessStates.BLOCKED, parent, 30)
        # process specific
        self.step = 1

    def exec(self):
        pass