from process import Process

class SharedMemoryProcess(Process):
    def __init__(self):
        # process specific
        self.step = 1

    def exec(self):
        pass