from process import Process
from enums.process_states import *

class JobGovernorProcess(Process):
    def __init__(self, parent, cpu):
        super().__init__(cpu, ProcessStates.BLOCKED, parent, 30)
        # process specific
        self.step = 1

    def exec(self):
        pass