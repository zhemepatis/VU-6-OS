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
                program_index = i-1
                break

        program_end = False

        if program_index!=-1:
            while not program_end:
                current_line = lines[program_index].strip()
                self.memory.memory[supervisor_memory_start][supervisor_index] = current_line
                if current_line=="$END":
                    program_end = True

                if supervisor_index == 15: #if the first block of supervisor memory ends
                    supervisor_index = 0
                    supervisor_memory_start += 1
                else:
                    supervisor_index += 1
                program_index += 1

    def validate_supervisor_memory(self):
        supervisor_memory = self.memory.memory[self.memory.SUPERVISOR_MEMORY_START:]

        words = [word for block in supervisor_memory for word in block]

        if "$AMJ" not in words:
            print("Missing '$AMJ' in supervisor memory.")
            return False
        if "$END" not in words:
            print("Missing '$END' in supervisor memory.")
            return False
        
        start_index = words.index("$AMJ") + 2 #plus 2 because skip the title
        end_index = words.index("$END")

        program_words = words[start_index:end_index]
        
        valid_commands = {"ADD", "SUB", "MUL", "DIV", "XCHG", "CMP", "EXIT"}
        commands_with_args = {"GN", "PN", "PD", "GR", "PR", "GS", "PS",
                          "JM", "JE", "JN", "JB", "JA"}
        
        for word in program_words:
            
            command = word[:2] if word[:2] in commands_with_args else word
            args = word[2:] if command in commands_with_args else ""
            
            if command not in valid_commands and command not in commands_with_args:
                print(f"Invalid command '{command}' found in supervisor memory.")
                return False
            
            if command in commands_with_args and (len(args) != 2 or not args.isalnum()):
                print(f"Command '{command}' requires arguments.")
                return False
        print("Supervisor memory validated successfully.")
        return True

    def load_program_to_user_memory(self):
        supervisor_memory_start = self.memory.SUPERVISOR_MEMORY_START #block number of supervisor memory
        vm_memory_pagination_table = self.cpu.ptr #pagination table address
        supervisor_index = 2 #index of words in supervisor - begin from commands, skip amj and title
        vm_index = 0
        end_of_program = False
        vm_block_index = 0 #index of which block of vm memory to take
        vm_memory_block = self.memory.memory[vm_memory_pagination_table][vm_block_index] #take block from pagination

        while not end_of_program:
            value = self.memory.memory[supervisor_memory_start][supervisor_index] #get value from supervisor

            if value=="$END":
                end_of_program = True
                break

            self.memory.memory[vm_memory_block][vm_index] = value #write value to vm memory

            supervisor_index += 1
            vm_index += 1

            if supervisor_index == 16: #if the first block of supervisor memory ends
                    supervisor_index = 0
                    supervisor_memory_start += 1
                    
            if vm_index == 16:
                    vm_index = 0
                    vm_block_index += 1
                    vm_memory_block = self.memory.memory[vm_memory_pagination_table][vm_block_index]