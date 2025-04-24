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
        if self.cpu.si == 3:
            self.put_data()
            return 

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

    def put_data(self):
        print("Data output starting from Block {block}, Word {word}:")
        result_str = ""

        block = self.SB + self.memory.USER_MEMORY_START
        word = self.SO

        for _ in range(10):
            char = chr(self.memory.memory[block][word])

            if char == '$':
                break

            result_str += char

            block += int((word + 1) / self.memory.BLOCK_LENGTH)
            word = (word + 1) % self.memory.BLOCK_LENGTH

        print(result_str)
        
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
            if line==title+'\n':
                if i == 0 or lines[i-1].strip() != "$AMJ":
                    return False #$AMJ not found
                program_index = i+1
                break

        if program_index==-1:
            return False #Title not found

        program_end = False
        data_section = False
        memory_end = 0x55
        data_block = supervisor_memory_start + self.memory.DATA_BLOCK_START
        data_word = 0
        

        while not program_end and program_index < len(lines):
            current_line = lines[program_index].strip()

            if supervisor_memory_start >= data_block: #if commands do not fit in memory and fill in data segment part
                return False #not enough supervisor memory 
            
            if data_block > memory_end:
                return False #data does not fit in memory
            
            if current_line=="$AMJ":
                return False #$END is not found and another program begins
            
            if current_line=="$END":
                program_end = True
                break

            if current_line=="DATA":
                data_section = True
                program_index += 1
                continue

            #Commands writing part
            if not data_section:
                self.memory.memory[supervisor_memory_start][supervisor_index] = current_line

                if supervisor_index == 15: #if one block of supervisor memory ends
                    supervisor_index = 0
                    supervisor_memory_start += 1
                else:
                    supervisor_index += 1
            #Data segment writing part
            else:
                i=0
                data_word = 0

                while i < len(current_line):
                    chunk = current_line[i:i+4].ljust(4)
                    self.memory.memory[data_block][data_word] = chunk

                    data_word += 1
                    i += 4

                    if data_word == 16:
                        data_word = 0
                        data_block += 1
                data_block += 1

            program_index += 1

        if not program_end:
            return False #there is no $END for this program until the end of file
        
        return True

    def load_program_to_user_memory(self):
        supervisor_memory_start = self.memory.SUPERVISOR_MEMORY_START
        vm_memory_pagination_table = self.cpu.ptr
        
        for i in range(16):
            supervisor_block = supervisor_memory_start + i
            vm_block = self.memory.memory[vm_memory_pagination_table][i]
            
            self.memory.memory[vm_block] = self.memory.memory[supervisor_block]