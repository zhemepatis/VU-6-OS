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

    def initialise_pagination(self, memory):
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

    def get_from_memory(self, offset): 
        block = self.SB + offset
        word = self.SO
        return self.memory.memory[block][word]

    def put_to_memory(self, offset, value): 
        block = self.SB + offset
        word = self.DO
        self.memory.memory[block][word] = value
        
    def get_user_input(self):
        value = input(f"Enter a number: ")
        return int(value)

    def print_value(self, value):
        print(value)

    def load_program_to_supervisor_memory(self, title):
        pass

    def validate_supervisor_memory(self):
        supervisor_memory = self.memory.memory[self.memory.SUPERVISOR_MEMORY_START:]
        if not supervisor_memory or supervisor_memory[0][0] != "$AMJ":
            raise Exception("Missing '$AMJ' in supervisor memory.")
        if not supervisor_memory[-1][0] == "$END":
            raise Exception("Missing '$END' in supervisor memory.")
        
        valid_commands = {"ADD", "SUB", "MUL", "DIV", "XCHG", "CMP", "EXIT"}
        commands_with_args = {"GN", "PN", "PD", "GR", "PR", "GS", "PS",
                          "JM", "JE", "JN", "JB", "JA"}
        
        for line in supervisor_memory[2:-1]:
            full_command = line[0]
            command = full_command[:2] if full_command[:2] in commands_with_args else full_command
            args = full_command[2:] if command in commands_with_args else ""
            
            if command not in valid_commands and command not in commands_with_args:
                raise Exception(f"Invalid command '{command}' found in supervisor memory.")
            
            if command in commands_with_args and (len(args) != 2 or not args.isalnum()):
                raise Exception(f"Command '{command}' requires arguments.")
        print("Supervisor memory validated successfully.")

    def load_program_to_user_memory(self):
        pass

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