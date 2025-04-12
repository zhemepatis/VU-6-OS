class ChannelDevice:
    def __init__(self):
        # registers
        self.ST = None  # Source Type
        self.SB = None  # Source Block
        self.SO = None  # Source Offset
        self.DT = None  # Destination Type
        self.DB = None  # Destination Block
        self.DO = None  # Destination Offset
        # other
        self.cpu = None
        self.memory = None

    def initialise_cpu(self, cpu):
        self.cpu = cpu

    def initialise_memory(self, memory):
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
        
    def handle_write(self, value):
        if self.DT == 1:
            self.put_to_memory(self.memory.USER_MEMORY_START, value)
            return

        if self.DT == 2:
            self.put_to_memory(self.memory.SUPERVISOR_MEMORY_START, value)
            return

        if self.DT == 3:
            pass

        if self.DT == 4:
            self.print_value(value)
            return

        if self.DT == 5:
            self.put_to_memory(self.memory.SHARED_MEMORY_START, value)
            return

    def get_from_memory(self, offset): 
        block = self.SB + offset
        word = self.SO
        return self.memory.memory[block][word]

    def put_to_memory(self, offset, value): 
        block = self.DB + offset
        word = self.DO
        self.memory.memory[block][word] = value
        
    def get_user_input(self):
        value = input(f"Enter a number: ")
        return int(value)

    def print_value(self, value):
        print(value)

    def read_hdd_file(self, file):
        hdd_file = open(file, "r")
        lines = hdd_file.readlines()
        hdd_file.close()
        return lines

    def load_program_to_supervisor_memory(self, title):
        lines = self.read_hdd_file("hdd.txt")
        supervisor_memory_start = self.memory.SUPERVISOR_MEMORY_START #supervisor memory index
        supervisor_index = 0
        program_index = -1 #index of the lines from the file that are being copied to supervisor

        for i, line in enumerate(lines):
            if line==title:
                program_index = i-1
                break

        program_end = False

        if program_index!=-1:
            while not program_end:
                self.memory.memory[supervisor_memory_start][supervisor_index] = lines[program_index]
                if lines[program_index]=="$END":
                    program_end = True

                if supervisor_index == 15: #if the first block of supervisor memory ends
                    supervisor_index = 0
                    supervisor_memory_start += 1
                supervisor_index += 1
                program_index += 1
                

    def validate_supervisor_memory(self):
        pass

    def load_program_to_user_memory(self):
        supervisor_memory_start = self.memory.SUPERVISOR_MEMORY_START
        vm_memory_pagination_table = self.cpu.ptr
        index = 0
        end_of_program = False

        while not end_of_program:
            memory_block = self.memory.memory[vm_memory_pagination_table][index]
            value = self.get_from_memory(supervisor_memory_start+index)
            self.put_to_memory(memory_block, value)

            if value=="$END":
                end_of_program = True
            
            index += 1

            

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