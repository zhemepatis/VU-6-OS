from process import Process

class SharedMemory(Process):
    def __init__(self, cpu, memory, channel_device):
        # process specific
        self.step = 1
        self.cpu = cpu
        self.memory = memory
        self.channel_device = channel_device

    def exec(self):
        if self.step == 1:
            print("Laukiama bendrosios atminties ir kanalu irenginio resursu")
            self.step = 2
            return
        
        if self.step == 2:
            if self.cpu.si == 6:
                self.step = 3
            elif self.cpu.si == 5:
                self.step = 4
            else:
                print("Klaida: nezinomas pertraukimo tipas")
                self.step = 6
            return
        
        if self.step == 3:
            block = self.cpu.ax
            word = self.cpu.bx
            self.cpu.ax =self.memory.memory[self.memory.SHARED_MEMORY_START + block][word]
            print(f"Atminties bloko {block} zodzio {word} reiksme: {self.cpu.ax}")
            self.step = 6 #islaisvinamas
            return
        
        if self.step == 4:
            block = self.cpu.ax
            word = self.cpu.bx
            value = self.cpu.ax
            self.memory.memory[self.memory.SHARED_MEMORY_START + block][word] = value
            print(f"Atminties bloko {block} zodzio {word} reiksmes pakeitimas i {value}")
            self.step = 6
            return
        
        if self.step == 6:
            print("SharedMemory baigta")
            self.cpu.si = 0
            self.step = 1
