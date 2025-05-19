from enum import Enum

class ProcessStates(Enum):
    RUNNING = 0
    READY = 1
    BLOCKED = 2
    READY_STOPPED = 3
    BLOCKED_STOPPED = 4