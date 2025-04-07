class ChannelDevice:
    def __init__(self, cpu, memory):
        # registers
        self.ST = None  # Source Type
        self.SB = None  # Source Block
        self.SO = None  # Source Offset
        self.DT = None  # Destination Type
        self.DB = None  # Destination Block
        self.DO = None  # Destination Offset
        # other
        self.cpu = cpu
        self.memory = memory

    def exchange(self):
        value = self.handle_read()
        self.handle_write(value)

    def handle_read(self):
        if self.ST == 1:
            return self.get_from_memory(self.memory.USER_MEMORY_START)

        if self.ST == 2:
            return self.get_from_memory(self.memory.SUPERVISOR_MEMORY_START)

        if self.ST == 3:
            return  # TODO:

        if self.ST == 4:
            return self.get_user_input()

        if self.ST == 5:
            return self.get_from_memory(self.memory.SHARED_MEMORY_START)

        if self.ST == 6:
            return self.get_from_register()
        
    def handle_write(self, value):
        if self.ST == 1:
            self.put_to_memory(self.memory.USER_MEMORY_START, value)

        if self.ST == 2:
            self.put_to_memory(self.memory.SUPERVISOR_MEMORY_START, value)

        if self.ST == 3:
            return  # TODO:

        if self.ST == 4:
            self.print_value(value)

        if self.ST == 5:
            self.put_to_memory(self.memory.SHARED_MEMORY_START, value)

        if self.ST == 6:
            self.put_to_register(value)

    def get_from_memory(self, offset): 
        block = self.SB + offset
        word = self.SO
        return self.memory.memory[block][word]

    def put_to_memory(self, offset, value): 
        block = self.SB + offset
        word = self.DO
        self.memory.memory[block][word] = value

    def get_from_external_memory(self):
        pass

    def get_from_register(self):
        return self.cpu.ax

    def put_to_register(self, value):
        self.cpu.ax = value

    def get_user_input(self):
        value = input(f"Enter a number: ")
        return int(value)

    def print_value(self, value):
        print(value)

    # TODO: move?
    # def put_data(self, block, word):
    #     print("Data output starting from Block {block}, Word {word}:")
    #     for i in range(10):
    #         current_word = word + i
    #         if current_word >= len(self.memory.memory[block]):
    #             break
    #         if self.memory.memory[block][current_word] == ord('$'):
    #             break
    #         print(self.memory.memory[block][current_word], end=" ")
    #     print()